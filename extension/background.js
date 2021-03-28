browser.webRequest.onCompleted.addListener(
    (details) => {
        //TODO: check if url is a meeting
        console.log(details);
        browser.browserAction.setPopup(
            {
                tabId: details.tabId,
                popup: browser.runtime.getURL("new_meeting_popup.html")
            }
        );
        browser.browserAction.setBadgeText(
            {
                text: "*",
                tabId: details.tabId
            }
        );
    },
    {urls: ["*://*.mozilla.org/*"], types:["main_frame"]}
);

var port = browser.runtime.connectNative("meeting_manager_pipe");

/*
Listen for messages from the app.
*/
port.onMessage.addListener((response) => {
    console.log("Received: " + JSON.stringify(response));
    browser.runtime.sendMessage({
        action: "RECV",
        data: response
    });
});

browser.runtime.onMessage.addListener((msg) => {
    if (msg.action === 'SEND') {
        port.postMessage({
                cmd: msg.cmd,
                data: msg.data
            }
        );
    }
});
