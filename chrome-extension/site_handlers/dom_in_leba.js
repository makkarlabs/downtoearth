$(function() {
    showDialogOnSite("Check the reviews for this site by clicking on the extension above.");
    chrome.runtime.sendMessage({"site_url": "dom_in_leba"}, function(response) {
        console.log(response);
    });
    console.log($("#GrapeVineFrame").attr('src'));
});
