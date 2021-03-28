
# Meeting Manager

🌎 Web extension to automate process of joing scheduled online meetings. 

💖 Made by BigBlueBoys with love for Hacknarock 5-th edition.


## Python Setup

Meeting Menager comes with `setup.py` script, for installing run:

``` 
python setup.py
```

It runs through instructions needed to set up _nativeMessaging_ with _Firefox_.
Proper ouput should look like this:

```
1. set user REG_KEY [True]
2. set machine REG_KEY [False] (need admin privileges)
3. change app\pipe\manifest.json path to win_launch.bat
```

Admin privilieges are _**not need**_, but running script as admin will create setup not only for current user.

## firefox web-extension setup

Our web extension works only on _firefox_, so here we will show how to install it in debugging mode for testing purposes.

1. Open _Firefox_ and type `about:debugging` in search bar
2. Proceed to `This Firefox` tab on the left side
3. Add temporary extension using `Load Temporary Add-on`
4. Browse and open `...\meeting-manager\extension\manifest.json`

Currently we are assuming _firefox_ is installed under `C:\Program Files\Mozilla Firefox\firefox.exe`. If Firefox is installed elsewhere, `mozilla_path` variable in `app\runner\launch_meeting.py` should be changed accordingly.

``` python 
def launch_meeting(url, browser=None):
    mozilla_path="path to firefox.exe"
```