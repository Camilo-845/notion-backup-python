import os
import win32com.client

def create_shortcut_to_directory(target_directory, shortcut_name):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_name)
    shortcut.TargetPath = target_directory
    shortcut.WorkingDirectory = os.path.dirname(target_directory)
    shortcut.Save()
    print(f"Se ha creado el acceso directo '{shortcut_name}' al directorio '{target_directory}'.")