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
<div id='accordion' class='media'>\
{{~it.data :value:index}}\
<h4 class='media-heading'>{{=value.name}}</h4>\
<div>\
{{~value.comments :val: index}}\
<div class='item'>\
<h4 class='media-heading'>{{=val.commenter_name}}</h4>\
<p class='media-body'>{{=val.comment}}</p>\
<span><i class='icon-thumbs-up'></i> {{=val.up_votes}} | <i class='icon-thumbs-down'></i> {{=val.down_votes}}</span>\
{{~}}\
</div>\
<div class='enterItem'>\
    <label for='comment'>Comments</label>\
    <textarea id='comment' placeholder='Add Comment' rows='3' cols='20'>\
    </textarea>\
    <button id='commentSubmit' class='btn'>Add Comment</button>\
</div>\
</div>\
</div>\
");