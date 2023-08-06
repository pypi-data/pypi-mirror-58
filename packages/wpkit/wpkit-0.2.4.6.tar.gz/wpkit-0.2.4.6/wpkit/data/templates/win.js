winjs = function () {
    var FullScreenSwitch = swjs.FullScreenSwitch;
    var {
        genUid, isdefined, makeDraggable, simpleMakeResizable
    } = wpjs;

    class QWedget {
        constructor(className) {
            className = className || 'QWedget';
            this.uid = className + genUid();
            this.active = false;
            this.visible = true;
            this.onCreate = [];

        }
        help() {
            var doc = `
            Please re-implement these methods:
                activate()
                source()
            `;
            console.log(doc);
            return doc;
        }

        el() {
            return $("#" + this.uid);
        }

        find(arg) {
            return this.el().find(arg);
        }

        hide() {
            this.visible = false;
            return this.el().hide();
        }

        show() {
            this.visible = true;
            return this.el().show();
        }

        remove() {
            this.el().remove();
        }

        promise(func) {
            if (this.active) func();
            else this.onCreate.push(() => {
                func();
            })
        }

        listenEvent(eventName, callback) {
            this.promise(() => {
                this.el().on(eventName, callback);
            });
            return this;
        }

        listenClick(callback) {
            return this.listenEvent("click", callback);
        }

        listenKeydown(key, callback) {
            return this.listenEvent("keydown", (e) => {
                var match = false;
                if (typeof key === "number") {
                    if (e.keyCode === key) match = true;
                } else if (typeof key === "string") {
                    if (e.key === key) match = true;
                }
                if (match) callback(e);
            });
        }

        listenCtrlKeydown(arg1, arg2) {
            if (arguments.length === 2) {
                return this.listenKeydown(arg1, (e) => {
                    if (e.ctrlKey && typeof arg2 === 'function') arg2(e);
                })
            } else {
                return this.listenEvent("keydown", (e) => {
                    if (e.ctrlKey && (typeof arg1 === "function")) arg1(e);
                })
            }
        }

        activate() {
            this.active = true;
            for (var i in this.onCreate) {
                if (typeof this.onCreate[i] == 'function') this.onCreate[i]();
            }
            // console.log("The method 'activate' must be re-implemented by subclasses.'");
        }

        hookParent(el) {
            return this.appendTo(el);
        }

        appendTo(el) {
            console.log("active:",this.active,
                this.uid,"appendtTo:",$(el),
                "this.el().parent():",this.el().parent());
            if (el) {
                if (this.active) {
                    $(el).append(this.el());
                    return;
                }
                $(el).append($(this.toString()));
            }
            this.activate();
        }

        hook(el) {
            if (el) {
                if (this.active) {
                    $(el).append(this.el());
                    return;
                }
                $(el).replaceWith(this.toString());
            }
            this.activate();
        }

        update() {
            if (this.active) {
                var el = this.el();
                el.replaceWith(this.toString());
                this.activate();
            }
        }

        source() {
            throw "The method 'source()' must be re-implemented bu subclasses.";
            return {
                template: ``,
                style: ``,
                script: ``
            }
        }

        toString() {
            var src = this.source();
            var str = src.template + (src.style || '') + (src.script || '');
            // console.log(str)
            return str;
        }
    }

    // class Q
    class QMenubar extends QWedget {
        constructor(items) {
            super("QMenubar");
            this.items = [];
            if (isdefined(items)) {
                var keys = Object.keys(items);
                for (var k in keys) {
                    this.addItem(k, items[k]);
                }
            }
        }

        itemsToString() {
            var s = '';
            this.items.map((v, i) => {
                s += v;
            });
            return s;
        }

        addItem(name, callback) {
            var item = this.newItem(name, callback);
            this.items.push(item);
            console.log("add item", item)
        }

        newItem(name, callback) {
            var cbname = `callback_${genUid()}`;
            window[cbname] = callback;
            var el = `<span onclick="${cbname}()" class="label-public menu-item">${name}</span>`;
            return el;
        }

        source() {
            return {
                template:
                    `\
            <div class="text-info qmenubar" id="${this.uid}">
            ${this.itemsToString()}
        </div>\
            `,
                style:
                    `\
                <style>
                 #${this.uid} {
            flex: 0 1 40px;
            width: 100%;
            background-color: white;color: orange;
            /*border-bottom: black dotted 2px;*/
        }
        #${this.uid} .menu-item{
            margin:auto 3px auto 3px;
            border-top: dotted black 2px;
            border-left: dotted black 2px;
            border-right: dotted black 2px;
            border-bottom: dotted black 2px;
        }\
            </style>\
                `
            }
        }
    }

    emitQEvent = function (name, params) {
        dispatchEvent(new CustomEvent("qevent-" + name, {
            detail: params
        }));
    };

    class QDialog extends QWedget {
        constructor(content) {
            super("Dialog");
            if ($.isPlainObject(content)) {
                var obj = content;
                this.content = obj.content;
            } else if (typeof content != "undefined") {
                this.content = content;
            }
        }

        activate() {
            this.active = true;
            var el = this.el();
            el.find(".handle-close").click(() => {
                el.remove();
            });
        }

        close() {
            return this.remove();
        }

        setContent(content) {
            this.content = content;
            this.update();
        }

        getContent() {
            if (!this.content) return '';
            else return this.content;
        }

        source() {
            return {
                template:
                    `
<div id="${this.uid}">
            <div class="head"><span class="handle-close">✖</span></div>
            <div class="body">${this.getContent()}</div>
</div>
            `,
                style:
                    `
                <style>
            #${this.uid} .head{
                display: flex;flex-flow: row-reverse;
            }
            #${this.uid}{
            display: block;
            width: 100%;
            min-height: 100px;
            /*z-index: 10;*/
                background-color:darkgray;
            }
</style>
                `
            }
        }
    }

    class QWindow extends QWedget {
        constructor(title, width, height, content) {
            super("QWindow");
            if ($.isPlainObject(title)) {
                var el = title;
                this.title = el.title;
                this.init_width = el.width;
                this.init_height = el.height;
                this.init_content = el.content;
            } else {
                this.title = title;
                this.init_width = width;
                this.init_height = height;
                this.init_content = content;
            }
            this.title = this.title || 'Window';
            this.init_width = this.init_width || 450;
            this.init_height = this.init_height || 400;
            this.init_content = this.init_content || '';
            this.left = 0;
            this.top = 0;
            this.zIndex = 1;
            this.init();
        }

        init() {
            var self = this;
            this.doClose = function (e) {
                self.remove();
            };
            this.doMinimize = function (e) {
                self.hide();
            };
        }

        activate() {
            super.activate();
            var self = this;
            simpleMakeResizable(this.el()[0]);
            makeDraggable(this.el()[0], this.getHead()[0]);
            this.el().find('.window-close').click(function () {
                self.close();
            });
            this.el().find('.window-minimize').click(function () {
                self.minimize();
            });
            new FullScreenSwitch(this.el().find('.window-fullscreen'), this.el());
        }

        close() {
            this.doClose();
        }

        minimize() {
            this.doMinimize();
        }

        maximize() {

        }

        restore() {

        }


        inputFile(msg, callback) {
            return this.input(msg, callback, 'file');
        }

        inputText(msg, callback) {
            return this.input(msg, callback, 'text');
        }

        input(msg, callback, type) {
            type = type || 'text';
            var content = `
            <div style="text-align: center">
            <label >${msg}</label>
            <input class="input" type="${type}">
            <button class="btn-submit">submit</button>
</div>
            `;
            var dialog = this.dialog(content);
            dialog.el().find(".btn-submit").click(() => {
                var input = dialog.el().find(".input");
                if (type === 'file') {
                    callback(input.val(), input[0].files);
                } else {
                    callback(input.val());
                }
                dialog.remove();
            });
            $(document).keydown((e) => {
                if (e.keyCode === 13) {
                    dialog.el().find(".btn-submit").click();
                }
            })

        }

        confirm(msg, callback) {
            var content = `
                <div style="text-align: center"><label>${msg}</label></div>
                <div style="text-align: center">
                <button class="btn-yes">YES</button><button class="btn-no">NO</button>
</div>
            `;
            var dialog = this.dialog(content);
            $(document).keydown((e) => {
                if (e.keyCode === 13) {
                    dialog.el().find(".btn-yes").click();
                }
            });
            dialog.el().find(".btn-yes").click((e) => {
                if (callback) {
                    callback()
                }
                dialog.remove();
            });
            dialog.el().find(".btn-no").click((e) => {
                dialog.remove();
            })
        }

        success(msg) {
            return this.msg(msg);
        }

        warn(msg) {
            return this.msg(msg);
        }

        info(msg) {
            return this.msg(msg);
        }

        msg(msg) {
            var content = `
                <div style="text-align: center"><label>${msg}</label></div>
                <div style="text-align: center" class="btn-ok" onclick="">OK</div>
            `;
            var dialog = this.dialog(content);
            dialog.el().find(".btn-ok").click((e) => {
                dialog.close();
            });
            $(document).keydown((e) => {
                if (e.keyCode === 13) {
                    dialog.el().find(".btn-ok").click();
                }
            })
        }

        dialog(content) {
            var dialog = new QDialog();
            dialog.setContent(content);
            dialog.appendTo(this.getDialog());
            return dialog;
        }

        getHead() {
            return this.el().find(".qwindow-head");
        }

        getDialog() {
            return this.el().find(".qwindow-dialog");
        }

        clearDialog() {
            this.getDialog().html("");
        }

        getBody() {
            return this.el().find(".qwindow-body");
        }
        getInner() {
            return this.getBody().find(".qwindow-inner");
        }
        setTitle(title){
            this.promise(()=>{
                this.find(".qwindow-title").html(title);
            })
        }
        getTitle(){
            if(this.active){
                return this.find(".qwindow-title").html();
            }
        }
        setContent(content) {
            this.promise(()=>{
                this.getInner().html(content);
            });
        }

        getContent() {
            if (!this.active) {
                return this.init_content;
            } else {
                return this.getInner().html();
            }
        }

        setPosition(x, y) {
            this.left = x;
            this.top = y;
            if (this.active) {
                this.el()[0].style.left = x + "px";
                this.el()[0].style.top = y + "px";
            }
        }

        getPosition() {
            if (this.active) {
                return [this.el()[0].offsetLeft, this.el()[0].offsetTop];
            } else {
                return [this.left, this.top];
            }
        }

        setZIndex(zIndex) {
            this.promise(() => {
                this.zIndex = zIndex;
                this.el()[0].style.zIndex = zIndex;
            })
        }

        getZIndex() {
            if (this.active) return Number.parseInt(this.el().css("z-index"));
            else return Number.parseInt(this.zIndex);
        }

        source() {
            return {
                template:
                    `
                <div id="${this.uid}">
                <div class="qwindow-head">
                <span class="qwindow-bar window-close">☒</span>
        <span class="qwindow-bar window-fullscreen"><span class=" switch-on">☐</span><span class="switch-off">❐</span></span>
        <span class="qwindow-bar window-minimize">▣</span>
        <span class="qwindow-title">${this.title}</span>
</div>
                <div class="qwindow-dialog">
                
</div>
                <div class="qwindow-body">
                <div class="qwindow-inner">
                ${this.getContent()}          
</div>
</div>


<style>
           #${this.uid} .qwindow-head{
           display: block;
           }
    #${this.uid} .qwindow-title{
           display: flex;flex-flow: row;flex: 1 1 200px;margin-left: 5px;color: whitesmoke;
    }
    #${this.uid} .qwindow-bar{
           margin: auto 3px auto 3px;
    }
    #${this.uid} {
        background-color: #ff4a37;
        width: ${this.init_width}px;
        height: ${this.init_height}px;
        display: flex;
        flex-flow: column;
        resize:both;
        overflow: auto;
        position: absolute;
        left: ${this.left}px;
        top: ${this.top}px;
        z-index: ${this.zIndex};
    }
    #${this.uid}  .qwindow-head {
        flex: 0 0 30px;
        background-color: deepskyblue;
        width: 100%;
        display: flex;
        flex-flow: row-reverse;
    }

    #${this.uid}  .qwindow-body {
        flex: auto;
        overflow: auto;
        padding: 5px;
        width: 100%;
        background-color: #f1f1f1;

    }

    #${this.uid}  .qwindow-inner {
        box-sizing: border-box;
        overflow: auto;
        flex: 1 0 auto;
        height: 100%;
        width: 100%;
        background-color: white;
        padding: 5px;
    }
</style>
           
</div>


                `,
                style:
                    `
             `
            }
        }
    }


    return {
        QWedget: QWedget,
        QDialog: QDialog,
        QMenubar: QMenubar,
        QWindow: QWindow
    }
}();