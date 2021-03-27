document.getElementById('btn_calendar').addEventListener('click', () => {
    browser.tabs.create({
        url: browser.runtime.getURL("pages/calendar.html")
    });
});
document.getElementById('btn_add').addEventListener('click', () => {
    window.location.replace(browser.runtime.getURL("new_meeting_popup.html"));
});
