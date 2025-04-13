from multimeter import ConfigCurrentAC, DisplayText, MeasureVoltageDC

# Example: Construct a MEAS:VOLT:DC? command with range and resolution
cmd = MeasureVoltageDC(range=10, resolution=0.001)
print(cmd.command())
# Output: MEAS:VOLT:DC? 10,0.001

# If we try to specify a resolution without a range, it will raise an error:
try:
    bad_cmd = MeasureVoltageDC(resolution=0.001)
except ValueError as e:
    print("Error:", e)
# Output: Error: Resolution specified without a range. Please specify a range or use 'DEF'.

# Construct a CONF:CURR:AC command (e.g., autorange with maximum resolution)
conf_cmd = ConfigCurrentAC(range="DEF", resolution="MAX")
print(conf_cmd.command())
# Output: CONF:CURR:AC MAX   (note: "DEF" range omitted yields instrument default (autorange))

# Construct a DISP:TEXT command
msg = DisplayText("TEST")
print(msg.command())
# Output: DISP:TEXT 'TEST'

# Including a quote in the message:
msg2 = DisplayText("Don't")
print(msg2.command())
# Output: DISP:TEXT 'Don''t'
