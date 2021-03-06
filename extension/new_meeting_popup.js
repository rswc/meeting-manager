function padZero(num) {
    return ("0" + num).slice(-2);
}

function now() {
    const date = new Date();
    return `${padZero(date.getDate())}/${padZero(date.getMonth())}/${date.getFullYear()} ${padZero(date.getHours())}:${padZero(date.getMinutes())}`;
}

const ui = document.getElementsByTagName('*');

browser.tabs.query({
    active: true,
    currentWindow: true,
    url: ["*://*.mozilla.org/*", "*://*.zoom.us/*"]
}).then((tabs) => {
    if (tabs.length) {
        ui.url.value = tabs[0].url;
        ui.title.value = tabs[0].title;
        ui.date.value = now();
    }
});

ui.btn_back.addEventListener("click", () => {
    browser.tabs.query({
        active: true,
        currentWindow: true
    }).then((tabs) => {
        browser.browserAction.setPopup(
            {
                tabId: tabs[0].id,
                popup: null
            }
        ).then(() => {
            browser.browserAction.setBadgeText(
                {
                    text: "",
                    tabId: tabs[0].id
                }
            ).then(() => {
                window.location.replace(browser.runtime.getURL("popup.html"));
            });
        });
    });
});

browser.runtime.onMessage.addListener((msg) => {
    if (msg.action === 'RECV' && !Array.isArray(msg.data)) {
        console.log(msg.data);
        ui.resp.innerText = msg.data;
    }
});

ui.form.addEventListener("submit", (e) => {
    e.preventDefault();
    const FD = new FormData(ui.form);
    // send new event request to python service
    browser.runtime.sendMessage({
        action: "SEND",
        cmd: "ADD",
        data: Object.fromEntries(FD.entries())
    });
    // display success info
    // option to delete/update event?
});
