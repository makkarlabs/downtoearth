$(function() {
    showDialogOnSite("Mahesh says the Lebanese Rolls are not as big as shown in the picture.");
    chrome.runtime.sendMessage({"site_url": "dom_in_leba"}, function(response) {
        console.log(response);
    });
    console.log($("#GrapeVineFrame").attr('src'));
});
