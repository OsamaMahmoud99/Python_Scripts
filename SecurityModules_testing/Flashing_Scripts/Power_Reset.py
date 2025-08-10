import time
import subprocess

# Path to the executable file
exe_path = "D:\\tools\\usrr_power_control\\usrr_power_control.exe"

# Parameter to pass to the executable
parameter_value = "4"

# Construct the command as a list
command = [exe_path, parameter_value]

# Execute the command
subprocess.run(command)

time.sleep(10)

# Parameter to pass to the executable
parameter_value = "1"

# Construct the command as a list
command = [exe_path, parameter_value]

# Execute the command
subprocess.run(command)