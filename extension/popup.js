const ui = document.getElementsByTagName('*');

document.getElementById('btn_add').addEventListener('click', () => {
    window.location.replace(browser.runtime.getURL("new_meeting_popup.html"));
});

browser.runtime.sendMessage({
    action: "SEND",
    cmd: "GET",
    data: 5
});
