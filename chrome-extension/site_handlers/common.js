console.log("inside commons");
function showDialogOnSite(dialog_text) {
	console.log(dialog_text);

        $.pnotify.defaults.history = false;
	$.pnotify({
		title: 'GrapeVine',
		text: dialog_text,
		hide: false
	});
}
