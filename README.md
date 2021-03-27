## Windows Setup


### Manifest

if `app\pipe\manifest.json` insert value to _path_ property - path to `launch.bat` script

In javascript add connect with following line:

``` js
var port = browser.runtime.connectNative("meeting_manager_pipe");
```

### Registry

Add to registry:

keys:
- `Computer\HKEY_CURRENT_USER\Software\Mozilla\NativeMessagingHosts\meeting_manager_pipe`
- `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Mozilla\NativeMessagingHosts\meeting_manager_pipe`
    
with value equal to `app\pipe\manifest.json` full path 