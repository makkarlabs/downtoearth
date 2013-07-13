var res_list = doT.template("\
<div class='media item'>\
    {{~it.data :value: index}}\
    <a class='pull-left' href='#'><img src='{{=value.photo_url}}' class='media-object resize' data-src='holder.js/64x64'/></a>\
    <div class='media-body'>\
        <h4 class='media-heading'>{{=value.name}}</h4>\
        <p>{{=value.location}}</p>\
    </div>\
    {{~}}\
</div>\
");

var items_list = doT.template("\
<div class='media-item'>\
{{~it.data :value: index}}

{{~}}
");