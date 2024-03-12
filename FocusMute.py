import time
import psutil
import pygetwindow as gw
import win32process
from pycaw.pycaw import AudioUtilities

def muteProgram(process_name):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == process_name:
            volume.SetMute(1, None)

def unmuteProgram(process_name):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == process_name:
            volume.SetMute(0, None)

def get_active_process_id():
    active_window = gw.getActiveWindow()
    if active_window is not None:
        try:
            _, pid = win32process.GetWindowThreadProcessId(active_window._hWnd)
            return pid
        except:
            pass
    return None

def check_window_focus(process_name):
    while True:
        active_process_id = get_active_process_id()
        if active_process_id is not None:
            process = psutil.Process(active_process_id)
            if process.name() == process_name:
                unmuteProgram(process_name)
            else:
                muteProgram(process_name)
        time.sleep(1)

if __name__ == "__main__":
    process_name = "Polaris-Win64-Shipping.exe"  # Replace this with the name of your process
    check_window_focus(process_name)
    
