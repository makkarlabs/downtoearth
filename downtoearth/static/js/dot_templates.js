var res_list = doT.template("\
<div class='media'>\
    {{~it.data :value: index}}\
    <div class='enclosure item' data-name='{{=value.name}}'>\
    <a class='pull-left' href='#'><img src='{{=value.photo_url}}' class='media-object resize' data-src='holder.js/64x64'/></a>\
    <div class='media-body'>\
        <h4 id='resName + ' class='media-heading'>{{=value.name}}</h4>\
        <p>{{=value.location}}</p>\
    </div>\
    </div>\
    {{~}}\
</div>\
");

var search_res_list = doT.template("\
<div class='media'>\
    <h2 class='media-heading'>Search Results</h2>\
    {{~it.data :value: index}}\
    <div class='enclosure item' data-name='{{=value.name}}'>\
    <div class='media-body'>\
        <h4 id='resName + ' class='media-heading'>{{=value.name}}</h4>\
    </div>\
    </div>\
    {{~}}\
</div>\
");

var items_list = doT.template("\
<div class='media'>\
    {{~it.data :value: index}}\
    <div class='item'>\
        <h5 class='media-heading'>{{=value.data.name}}</h4>\
    </div>\
    {{~}}\
</div>\
");

var comments_list = doT.template("\
<div class='accordion' id='accordion'>\
{{~it.data :value:index}}\
<div class='accordion-group'>\
<div class='accordion-heading'>\
<a class='accordion-toggle' data-toggle='collapse' data-parent='#accordion' href='#collapse{{=value.id}}'>\
{{=value.name}}\
</a>\
</div>\
<div id='collapse{{=value.id}}' class='accordion-body collapse'>\
<div class='accordion-inner'>\
{{~value.comments :val:ind}}\
<div class='itemCom'>\
<p>{{=val.comment}}</p>\
<span><a class='thumbs' href='#' title='Vote For this answer' data-item-id={{=value.id}} data-c-id={{=val.c_id}} data-can-vote={{=val.can_vote}} data-ud='up'><i class='icon-thumbs-up thumbs'></i> <em id='voteup{{=val.c_id}}'>{{=val.up_votes}}</em></a> \
| <a href='#' class='thumbs' data-item-id={{=value.id}} data-c-id={{=val.c_id}} data-ud='down' title='Vote Against this answer' data-can-vote={{=val.can_vote}}><i class='icon-thumbs-down'></i> <em id='votedown{{=val.c_id}}'>{{=val.down_votes}}</em></a></span>\
</div>\
{{~}}\
</div>\
<div class='enterItem'>\
    <label for='comment'>Comments</label>\
    <input id='{{=value.id}}comment' type='text' class='comm' placeholder='Add Comment' />\
    <br>\
    <button class='btn commentSub' data-item-id={{=value.id}} >Add Comment</button>\
</div>\
</div>\
{{~}}\
</div>\
");

var comment = doT.template("\
    <div class='itemCom'>\
    <p>{{=it.comment}}</p>\
    <span><a class='thumbs' href='#' title='Vote For this answer' data-item-id={{=it.item_id}} data-c-id={{=it.comment_id}} data-can-vote='true' data-ud='up'><i class='icon-thumbs-up thumbs'></i> <em id='voteup{{=it.comment_id}}'>0</em></a> \
    | <a href='#' class='thumbs' data-item-id={{=it.item_id}} data-c-id={{=it.comment_id}} data-ud='down' title='Vote Against this answer' data-can-vote='true'><i class='icon-thumbs-down'></i> <em id='votedown{{=it.comment_id}}'>0</em></a></span>\
");