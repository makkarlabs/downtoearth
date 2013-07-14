$(function() {
    showDialogOnSite("Did you know that the McD. Veg Nuggets is not as big as it looks?.");
    chrome.runtime.sendMessage({"site_url": "mcdonaldsindia_com"}, function(response) {
        console.log(response);
    });
    console.log($("#GrapeVineFrame").attr('src'));
});
