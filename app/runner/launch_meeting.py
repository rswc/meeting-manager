import webbrowser

def launch_meeting(url, browser=None):
    webbrowser.get(browser).open_new_tab(url)

if __name__ == '__main__':
    # Add firefox to path

    mozilla_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(mozilla_path))
    url = "https://us02web.zoom.us/j/2732874617#success"
    launch_meeting(url, browser='firefox')

    
