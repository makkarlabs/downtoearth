console.log("inside commons");
function showDialogOnSite(dialog_text) {
	console.log(dialog_text);

        $.pnotify.defaults.history = false;
	$.pnotify({
		title: 'Regular Notice',
		text: dialog_text
	});
}
