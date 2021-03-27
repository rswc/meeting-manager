listener = browser.webRequest.onBeforeRequest.addListener(
    (details) => {
        console.log(details);
    },
    {urls: ["*://*.mozilla.org/*"], types:["main_frame"]}
);