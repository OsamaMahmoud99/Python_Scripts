import subprocess

def open_winidea_workspace(workspace_path):
    # Replace "winidea.exe" with the actual name of the winIDEA executable
    winidea_executable = "C:\\iSYSTEM\\winIDEA9\\winIDEA.exe"

    # Launch winIDEA with the workspace file as an argument
    subprocess.Popen([winidea_executable, workspace_path])

# Example usage
workspace_path = "D:\\Brose\\dcu_validation\\Winidea\\Flashing.xjrf"
open_winidea_workspace(workspace_path)