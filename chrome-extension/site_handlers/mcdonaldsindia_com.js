$(function() {
    showDialogOnSite("Check the reviews for this site by clicking on the extension above.");
    chrome.runtime.sendMessage({"site_url": "mcdonaldsindia_com"}, function(response) {
        console.log(response);
    });
    console.log($("#GrapeVineFrame").attr('src'));
    //$("#GrapeVineFrame").src = "http://localhost:5000/restaurants/kfc";
    //$("#GrapeVineFrame").attr("src", function ( i, val ) { return val; });
    //console.log("You are hAcKeD! ha ha");
});
