
console.log("background started");
injected_ids = [];
injected_ids_map = {};
chrome.runtime.onMessage.addListener(
function(request, sender, sendResponse) {
console.log(sender.tab ?
            "from a content script:" + sender.tab.url :
            "from the extension");
   if (request.site_url === "dominos_co_in") {
        console.log("hello");
        chrome.browserAction.setPopup({"popup":"site_handlers/dominos_co_in.html"});
        injected_ids.push(sender.tab.id);
        injected_ids_map[sender.tab.id] = "dominos_co_in";
      sendResponse({farewell: "good"});
    }

    else if (request.site_url === "mcdonaldsindia_com") {
        console.log("hello");
        chrome.browserAction.setPopup({"popup":"site_handlers/mcdonaldsindia_com.html"});
        injected_ids.push(sender.tab.id);
        injected_ids_map[sender.tab.id] = "mcdonaldsindia_com";
      sendResponse({farewell: "good"});
    }


    else if (request.site_url === "dom_in_leba") {
        console.log("hello");
        chrome.browserAction.setPopup({"popup":"site_handlers/dom_in_leba.html"});
        injected_ids.push(sender.tab.id);
        injected_ids_map[sender.tab.id] = "dom_in_leba";
      sendResponse({farewell: "good"});
    }

    else {
        chrome.browserAction.setPopup({"popup":"site_handlers/common.html"});
      sendResponse({farewell: "bye"});
    }
});


chrome.tabs.onActivated.addListener(function(activeInfo) {
    console.log(activeInfo);    
    if(injected_ids.indexOf(activeInfo.tabId) == -1) {
        chrome.runtime.sendMessage({"site_url": "other"});
    }
    else {
        chrome.browserAction.setPopup({"popup":"site_handlers/"+injected_ids_map[activeInfo.tabId]+".html"});
    }
});

chrome.tabs.onRemoved.addListener(function( tabId,  removeInfo) {
    if(injected_ids.indexOf(activeInfo.tabId) == -1) {
        injected_ids.splice(injected_ids.indexOf(tabId), 1);
    }
    else {
        injected_ids_map.remove(tabId);
    }
});
