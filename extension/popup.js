const ui = document.getElementsByTagName('*');
var interval;

REC_TRANS = {
    "": "",
    "EVERY_WEEK": "Weekly",
    "EVERY_OTHER_WEEK": "Every other week",
    "DAILY": "Daily",
    "MONTHLY": "Monthly"
}

function timeDiff(timestamp, date) {
    let td = Math.floor(timestamp - Date.now() / 1000);
    if (Math.abs(td) <= 60) {
        return `${td}s`;
    }
    td = Math.floor(td / 60);
    if (Math.abs(td) <= 60) {
        return `${td}min`;
    }
    return `${date}`;
}

function timeFormat() {
    for (const el of ui.events.getElementsByClassName("evt_time")) {
        el.innerText = timeDiff(el.dataset.timestamp, el.dataset.date);
    }
}

document.getElementById('btn_add').addEventListener('click', () => {
    window.location.replace(browser.runtime.getURL("new_meeting_popup.html"));
});

browser.runtime.onMessage.addListener((msg) => {
    if (msg.action === 'RECV' && Array.isArray(msg.data)) {
        console.log(msg.data);
        for (const evt of msg.data) {
            let el = document.createElement("div");
            el.classList.add("evt");
            el.innerHTML = `<div class="evt_title">${evt.Title}</div><div class="evt_time" data-date="${evt.Date}" data-timestamp="${evt.Timestamp}">00</div><div class="evt_misc">${REC_TRANS[evt.Recurring || '']}</div>`;
            ui.events.appendChild(el);
        }
        interval = window.setInterval(timeFormat, 500);
    }
});

browser.runtime.sendMessage({
    action: "SEND",
    cmd: "GET",
    data: 5
});
