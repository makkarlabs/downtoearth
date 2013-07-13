$(function() {
    showDialogOnSite("write your html here");
    chrome.runtime.sendMessage({"site_url": "dominos_co_in"}, function(response) {
        console.log(response);
    });
    console.log($("#GrapeVineFrame").attr('src'));
    //$("#GrapeVineFrame").src = "http://localhost:5000/restaurants/kfc";
    //$("#GrapeVineFrame").attr("src", function ( i, val ) { return val; });
    console.log("You are hAcKeD! ha ha");
});
