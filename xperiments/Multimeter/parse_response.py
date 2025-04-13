from dataclasses import dataclass
from typing import List, Union


@dataclass
class Identity:
    manufacturer: str
    model: str
    serial: str
    firmware: str


@dataclass
class ErrorResponse:
    code: int
    message: str


def parse_idn_response(response: str) -> Identity:
    """Parse *IDN? response into Identity dataclass."""
    parts = response.strip().split(",")
    if len(parts) < 4:
        raise ValueError("Unexpected *IDN? response format")
    return Identity(
        manufacturer=parts[0], model=parts[1], serial=parts[2], firmware=parts[3]
    )


def parse_error_response(response: str) -> ErrorResponse:
    """Parse SYST:ERR? response "code,<message>" into code and message."""
    text = response.strip()
    code_str, msg = text.split(",", 1)
    code = int(code_str)
    # Remove surrounding quotes from message
    message = msg.strip()
    if message.startswith('"') and message.endswith('"'):
        message = message[1:-1]
    return ErrorResponse(code=code, message=message)


def parse_reading_response(response: str) -> Union[float, List[float]]:
    """Parse a measurement reading string into float or list of floats."""
    data = response.strip()
    if not data:
        raise ValueError("Empty response")
    # Some responses may have multiple comma-separated readings
    parts = data.split(",")
    values = [float(x) for x in parts]
    return values[0] if len(values) == 1 else values


# Examples of parsing:
idn_str = "HEWLETT-PACKARD,34401A,0,12-34-56"
id_info = parse_idn_response(idn_str)
print(id_info.model, id_info.firmware)
# Output: 34401A 12-34-56

err_str = '-113,"Undefined header"'
err = parse_error_response(err_str)
print(err.code, err.message)
# Output: -113 Undefined header

reading_str = "1.2345E+01\n"
val = parse_reading_response(reading_str)
print(val)
# Output: 12.345

# If multiple readings were returned in one response:
multi_str = "2.500E-03,2.501E-03,2.498E-03"
vals = parse_reading_response(multi_str)
print(vals)
# Output: [0.0025, 0.002501, 0.002498]

# Handling raw bytes from instrument (e.g., via serial or socket):
raw_bytes = b"5.000E+00\r\n"
reading = parse_reading_response(raw_bytes.decode("utf-8"))
print(reading)
# Output: 5.0
