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

var port = browser.runtime.connectNative("meeting_manager");

/*
Listen for messages from the app.
*/
port.onMessage.addListener((response) => {
  console.log("Received: " + response);
});

/*
On a click on the browser action, send the app a message.
*/
browser.browserAction.onClicked.addListener(() => {
  console.log("Sending:  ping");
  port.postMessage("ping");
});
