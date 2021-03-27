listener = browser.webRequest.onBeforeRequest.addListener(
    (details) => {
        console.log(details);
    },
    {urls: ["*://*.mozilla.org/*"], types:["main_frame"]}
);

var port = browser.runtime.connectNative("meeting-manager");

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
