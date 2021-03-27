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
    url: "*://*.mozilla.org/*"
}).then((tabs) => {
    console.log(tabs);
    if (tabs.length) {
        ui.url.value = tabs[0].url;
        ui.title.value = tabs[0].title;
        ui.date.value = now();
    }
});

ui.form.addEventListener("submit", (e) => {
    e.preventDefault();
    const FD = new FormData(ui.form);
    console.log(Object.fromEntries(FD.entries()));
    browser.runtime.sendNativeMessage(
        "meeting_manager_pipe",
        JSON.stringify(Object.fromEntries(FD.entries())));
    // send new event request to python service
    // display success info
    // option to delete/update event?
});
