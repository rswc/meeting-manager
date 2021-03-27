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
    console.log(e);
    const FD = new FormData(ui.form);
});
