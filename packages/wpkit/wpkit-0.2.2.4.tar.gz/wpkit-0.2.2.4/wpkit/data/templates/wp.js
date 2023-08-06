
wpjs=function () {

console.log('my.js loaded.');
var debug=true;
var tlog= function(text) {
    if(debug){
        console.log(message="tlog message:");
        console.log(text);
    }
};
var isdefined=function (obj) {
    return typeof obj != "undefined";
};
var postJson=function (url, data) {
    return $.ajax({
        type: "POST",
        contentType: "application/json; charset=utf-8",
        url: url,
        data: JSON.stringify(data),
        async: false,
        dataType: "json"
    });
};
var myjs = 'Myjs is loaded;';
var disable_ctrl_s=function() {
    document.onkeydown = function (e) {
        e = e || window.event;//Get event

        if (!e.ctrlKey) return;

        var code = e.which || e.keyCode;//Get key code

        switch (code) {
            case 83://Block Ctrl+S
            case 87://Block Ctrl+W -- Not work in Chrome and new Firefox
                e.preventDefault();
                e.stopPropagation();
                break;
        }
    };
};

var T = {
    NOT_FOUND: "NOT_FOUND",
    NOT_EXISTS: "NOT_EXISTS",
    NO_VALUE: "NO_VALUE",
    NOT_IMPLEMENTED: "NOT_IMPLEMENTED",
    NOT_ALLOWED: "NOT_ALLOWED",
    EMPTY: "EMPTY",
    NO_SUCH_VALUE: "NO_SUCH_VALUE",
    NO_SUCH_ATTR: "NO_SUCH_ATTR",
    NOT_GIVEN: "NOT_GIVEN",
    FILE: "FILE",
    DIR: "DIR",
    LINK: "LINK",
    MOUNT: "MOUNT"
};
var genUid=function(){
    return Math.random().toString().slice(2,-1);
};

var simpleMakeResizable=function(el){
    el.style.resize='both';
    el.style.overflow='auto';
};
var makeDraggable = function (el,head) {
    // Make the DIV element draggable:
    dragElement(el);
    function dragElement(elmnt) {
        elmnt.style.position='absolute';
        var ofx=0,ofy=0;var ox1,ox2,oy1,oy2=0;
        if (head) {
            // if present, the header is where you move the DIV from:
            head.onmousedown = dragMouseDown;
        } else {
            // otherwise, move the DIV from anywhere inside the DIV:
            elmnt.onmousedown = dragMouseDown;
        }

        function dragMouseDown(e) {
            e = e || window.event;
            e.preventDefault();
            ox1=elmnt.offsetLeft;
            oy1=elmnt.offsetTop;
            ox2=e.clientX;oy2=e.clientY;
            document.onmouseup = closeDragElement;
            document.onmousemove = elementDrag;
        }

        function elementDrag(e) {
            e = e || window.event;
            e.preventDefault();
            ofx=e.clientX-ox2,ofy=e.clientY-oy2;
            elmnt.style.top=(oy1 +ofy) + "px";
            elmnt.style.left = (ox1 + ofx) + "px";
            res={
                ox1:ox1,oy1:oy1,ox2:ox2,oy2:oy2,x:e.clientX,y:e.clientY, ofx:ofx,ofy:ofy,
                offsetTop:elmnt.offsetTop,offsetLeft:elmnt.offsetLeft
            }
            // console.log(res)
        }

        function closeDragElement() {
            // stop moving when mouse button is released:
            document.onmouseup = null;
            document.onmousemove = null;
        }
    }
};

return {
    genUid:genUid,
    disable_ctrl_s:disable_ctrl_s,
    T:T,
    simpleMakeResizable:simpleMakeResizable,
    makeDraggable:makeDraggable,
    isdefined:isdefined,
    postJson:postJson
}
}();