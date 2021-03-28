import webbrowser
from win10toast import ToastNotifier 

import os

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))[:-10]

def notify(message: str, duration=5):
    icon_path = PROJECT_PATH + r"app\runner\bingus.ico"
    toast = ToastNotifier()
    toast.show_toast("Meeting Manager", message, duration=duration, icon_path=icon_path)

def launch_meeting(url, browser=None):
    webbrowser.get(browser).open_new_tab(url)

ZOOM_URL = "https://zoom.us/j/6866658590?pwd=Y0d3c29OakpKQk1MT01ZbW5GVWpudz09"
ZOOM_JOIN = "https://zoom.us/wc/6866658590/start" 

if __name__ == '__main__':
    # Add firefox to path
    # th = threading.Thread(target=notify)

    notify("Hello its Bingus")

    mozilla_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(mozilla_path))
    url = "https://us02web.zoom.us/j/2732874617#success"

    launch_meeting(ZOOM_JOIN, browser='firefox')
    