$(function() {
    showDialogOnSite("write your html here");
    $("#GrapeVineFrame").src = "http://localhost:5000/restaurants/kfc";
    $("#GrapeVineFrame").attr("src", function ( i, val ) { return val; });
    console.log("You are hAcKeD! ha ha");
});
