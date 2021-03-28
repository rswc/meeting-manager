import webbrowser
import os
from win10toast import ToastNotifier 

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))[:-10]
FIREFOX_PATH = r"C:\Program Files\Mozilla Firefox\firefox.exe" 
ZOOM_URL = "https://zoom.us/wc/6866658590/join?pwd=Y0d3c29OakpKQk1MT01ZbW5GVWpudz09"

def notify(message: str, duration=5):
    icon_path = PROJECT_PATH + r"app\runner\bingus.ico"
    toast = ToastNotifier()
    toast.show_toast("Meeting Manager", message, duration=duration, icon_path=icon_path)

def launch_meeting(url, browser=None):
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(FIREFOX_PATH))
    webbrowser.get(browser).open_new_tab(url)

if __name__ == '__main__':
    notify("Hello its Bingus")
    launch_meeting(ZOOM_URL, browser='firefox')
    