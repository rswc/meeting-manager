"""
Set windows registers keys to allow Web Extension pipe
"""

import json
import os
import re
import winreg
import ctypes

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
REG_PATH_USER = r"Software\Mozilla\NativeMessagingHosts\meeting_manager_pipe"
REG_PATH_MACHINE = r"SOFTWARE\Mozilla\NativeMessagingHosts\meeting_manager_pipe"
MANIFEST_PATH =  PROJECT_PATH + r"\app\pipe\manifest.json"

def set_windows_registers(winreg_type, key_path, value):
    try:
        winreg.CreateKey(winreg_type, key_path)
        registry_key = winreg.OpenKey(winreg_type, key_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, "", 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

if __name__ == "__main__":
    # is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    result = set_windows_registers(winreg.HKEY_CURRENT_USER, REG_PATH_USER, MANIFEST_PATH)
    print(f"1. set user REG_KEY [{result}]")

    result = set_windows_registers(winreg.HKEY_LOCAL_MACHINE, REG_PATH_MACHINE, MANIFEST_PATH)
    print(f"2. set machine REG_KEY [{result}] (need admin privileges)")
        
    with open(MANIFEST_PATH, 'r') as manifest_file: 
        manifest_content = json.loads(manifest_file.read())

    win_launch_path = PROJECT_PATH + r"\app\pipe\win_launch.bat"
    manifest_content['path'] = win_launch_path

    changed_manifest = json.dumps(manifest_content)
    changed_manifest = changed_manifest.replace(",", ",\n").replace("{", "{\n").replace("}", "\n}")

    with open(MANIFEST_PATH, 'w') as manifest_file:
        manifest_file.write(changed_manifest)

    print(r"3. change app\pipe\manifest.json path to win_launch.bat")


