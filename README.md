
# Meeting Manager

🌎 Web extension to automate the process of joining scheduled online meetings. 

💖 Made by _**BigBlueBoys**_ with love for _Hacknarock 5th edition_.

## Python Setup

Simply run `setup.py`:

``` 
python setup.py
```

It runs through instructions needed to set up _nativeMessaging_ with _Firefox_.
Command ouput should look like this:

```
1. set user REG_KEY [True]
2. set machine REG_KEY [False] (need admin privileges)
3. change app\pipe\manifest.json path to win_launch.bat
```

Admin privilieges are _**not necessary**_, but running script as admin will create setup not only for current user.

## Mozilla Firefox Setup

Currently our web extension works only on _firefox_, so here we show how to install it in _**debugging mode**_ for testing purposes.

1. Open _Firefox_ and type `about:debugging` in search bar
2. Proceed to `This Firefox` tab on the left side
3. Add temporary extension using `Load Temporary Add-on`
4. Browse and open `...\meeting-manager\extension\manifest.json`

Currently we assume _firefox_ is installed under `C:\Program Files\Mozilla Firefox\firefox.exe`. 
If Firefox is installed elsewhere, the `FIREFOX_PATH` variable in `app\runner\launch_meeting.py` should be changed accordingly.

``` python 
FIREFOX_PATH="path to firefox.exe"
```