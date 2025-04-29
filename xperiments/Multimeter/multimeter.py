from dataclasses import dataclass
from typing import Literal

ParamVal = Literal["MIN", "MAX", "DEF"]
# Define the allowed literals for parameter keywords.
ParamType = float | ParamVal


def _validate_param(
    value: ParamType, name: str
) -> ParamType:
    """
    Validate and normalize a parameter value.

    Args:
        value: The parameter value as either a numeric value (float or int)
               or one of the literal strings "MIN", "MAX", "DEF".
        name: The name of the parameter (for error messages).

    Returns:
        The normalized value (for strings, converted to uppercase) or the numeric value.

    Raises:
        ValueError: If the value is invalid or of an unexpected type.
    """
    match value:
        case str(s):
            s = s.upper()
            if s not in ParamVal:
                raise ValueError(
                    f"Invalid {name} parameter: {s}"
                )
            return s
        case int() | float() as numeric if numeric > 0:
            return numeric
        case _:
            raise ValueError(
                f"Unexpected type for {name} parameter: {value}"
            )


@dataclass
class MeasureVoltageDC:
    """
    Models the MEASure:VOLTage:DC? command for the Keysight 34401A.

    Attributes:
        range: Voltage measurement range as a float or a special keyword ("MIN", "MAX", "DEF").
        resolution: Voltage resolution as a float or a special keyword ("MIN", "MAX", "DEF").

    The __post_init__ method validates the fields using pattern matching via _validate_param.
    """

    range: ParamType = "DEF"
    resolution: ParamType = "DEF"

    def __post_init__(self) -> None:
        self.range = _validate_param(self.range, "range")
        self.resolution = _validate_param(
            self.resolution, "resolution"
        )

        # Enforce that if resolution is non-default, range must also be non-default.
        if (
            isinstance(self.range, str)
            and self.range == "DEF"
            and (
                isinstance(self.resolution, str)
                and self.resolution != "DEF"
            )
        ):
            raise ValueError(
                "Resolution specified without a valid (non-'DEF') range."
            )

    def command(self) -> str:
        """
        Constructs the SCPI command string for measuring DC voltage.

        Returns:
            A string representing the SCPI command.
        """
        base = "MEAS:VOLT:DC?"
        if self.range == "DEF" and self.resolution == "DEF":
            return base

        parts = []
        if self.range != "DEF":
            parts.append(str(self.range))
        if self.resolution != "DEF":
            parts.append(str(self.resolution))

        return f"{base} {','.join(parts)}"


@dataclass
class ConfigCurrentAC:
    """
    Models the CONFigure:CURRent:AC command for the Keysight 34401A.

    Attributes:
        range: Current measurement range as a float or a special keyword ("MIN", "MAX", "DEF").
        resolution: Current resolution as a float or a special keyword ("MIN", "MAX", "DEF").

    The __post_init__ method validates the fields using pattern matching via _validate_param.
    """

    range: ParamType = "DEF"
    resolution: ParamType = "DEF"

    def __post_init__(self) -> None:
        self.range = _validate_param(self.range, "range")
        self.resolution = _validate_param(
            self.resolution, "resolution"
        )

        # Enforce that if resolution is non-default, the range must also be non-default.
        if (
            isinstance(self.range, str)
            and self.range == "DEF"
            and (
                isinstance(self.resolution, str)
                and self.resolution != "DEF"
            )
        ):
            raise ValueError(
                "Resolution specified without a valid (non-'DEF') range."
            )

    def command(self) -> str:
        """
        Constructs the SCPI command string for configuring AC current measurement.

        Returns:
            A string representing the SCPI configuration command.
        """
        base = "CONF:CURR:AC"
        if self.range == "DEF" and self.resolution == "DEF":
            return base

        parts = []
        if self.range != "DEF":
            parts.append(str(self.range))
        if self.resolution != "DEF":
            parts.append(str(self.resolution))

        return f"{base} {','.join(parts)}"


# Demonstration of usage:
if __name__ == "__main__":
    # Valid command with numeric parameters.
    mv_cmd = MeasureVoltageDC(range=10.0, resolution=0.001)
    print("MeasureVoltageDC command:", mv_cmd.command())

    # Valid command using special keywords (input as lower case, normalized to uppercase).
    cc_cmd = ConfigCurrentAC(range="min", resolution="max")
    print("ConfigCurrentAC command:", cc_cmd.command())

    # An attempt that should fail: specifying a non-default resolution while leaving range as default.
    try:
        bad_cmd = MeasureVoltageDC(resolution=0.001)
    except ValueError as error:
        print("Error:", error)
