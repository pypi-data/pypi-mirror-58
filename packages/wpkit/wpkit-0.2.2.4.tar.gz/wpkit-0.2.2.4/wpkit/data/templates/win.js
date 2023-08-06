winjs = function () {
    var FullScreenSwitch = swjs.FullScreenSwitch;
    var genUid = wpjs.genUid;
    var isdefined = wpjs.isdefined;
    var makeDraggable = wpjs.makeDraggable;
    var simpleMakeResizable = wpjs.simpleMakeResizable;

    class QMenubar {
        constructor(items) {
            this.uid = 'q-menubar-'+genUid();
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
            console.log("add item",item)
        }

        newItem(name, callback) {
            var cbname = `callback_${genUid()}`;
            window[cbname] = callback;
            var el = `<span onclick="${cbname}()" class="label-public menu-item">${name}</span>`;
            return el;
        }

        toString() {
            var obj = this.source();
            return obj.template + obj.style;
        }

        source() {
            return {
                template:
                    `\
            <div class="text-info q-menubar" id="${this.uid}">
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
            border-bottom: black dotted 2px;
        }
        #${this.uid} .menu-item{
            margin:auto 3px auto 3px;
            padding: auto 3px auto 3px !important;
            border-top: dotted black 2px;
            border-left: dotted black 2px;
            border-right: dotted black 2px;
        }\
            </style>\
                `
            }
        }
    }

    class QWindow {
        constructor(el, height, width, content, title, styles) {
            if ((el != null) && ($.isPlainObject(el))) {
                this.el = el.el;
                this.init_height = el.height || 400;
                this.init_width = el.width || 400;
                this.init_content = el.content;
                this.title = el.title || 'window';
                this.init_styles = el.styles || {};

            } else {
                this.el = el;
                this.init_height = height || 400;
                this.init_width = width || 400;
                this.init_content = content;
                this.title = title || 'window';
                this.init_styles = styles || {};
            }
            this.init_style();
            this.init_js();
        }

        warn(msg, callback) {
            var uid = 'warn-dialog-' + genUid();
            var el = `<div id="${uid}" style="text-align: center;color: white;">\
            <div class="msg-box" >${msg}</div>\
            <button class="btn-confirm">Confirm</button>`;
            var dialog = this.dialog(el);
            var el = this.toolbox.find('#' + uid);
            el.find('.btn-confirm').click(function () {
                dialog.remove();
                if (typeof callback == "function") {
                    callback
                }
            });
        }

        info(msg, callback) {
            var uid = 'warn-dialog-' + genUid();
            var el = `<div id="${uid}" style="text-align: center;color: white;">\
            <div class="msg-box" >${msg}</div>\
            <button class="btn-confirm">Confirm</button>`;
            var dialog = this.dialog(el);
            var el = this.toolbox.find('#' + uid);
            el.find('.btn-confirm').click(function () {
                dialog.remove();
                if (typeof callback == "function") {
                    callback
                }
            });
        }

        confirm(msg, callback) {
            var uid = 'confirm-dialog-' + genUid();
            var el = `<div id="${uid}" style="text-align: center;color: white;">\
            <div class="msg-box" >${msg}</div>\
            <button class="btn-yes">Yes</button><button class="btn-no">No</button></div>`;
            var dialog = this.dialog(el);
            var el = this.toolbox.find('#' + uid);
            el.find('.btn-yes').click(function () {
                callback();
                dialog.remove();
            });
            el.find('.btn-no').click(function () {
                dialog.remove();
            });
        }

        input(msg, callback) {
            var uid = 'input-dialog-' + genUid();
            var el = `<div id="${uid}" style="text-align: center;color: white;"><div class="msg-box" >${msg}</div><input class="text-input" type="text"><button class="btn-submit">Submit</button></div>`
            var dialog = this.dialog(el);
            var el = this.toolbox.find('#' + uid);
            el.find('.btn-submit').click(function () {
                var text = el.find('.text-input').val();
                callback(text);
                el.find('.text-input').val();
                dialog.remove();
            });
        }

        dialog(el) {
            var uid = 'dialog-' + genUid();
            el = el || '';
            this.toolbox.append($(`
            <div id="${uid}">
            <div class="head"><span class="tool-close">✖</span></div>
            <div class="body">${el}</div>
</div>
            <style>
            #${uid} .head{
                display: flex;flex-flow: row-reverse;
            }
            #${uid}{
            display: block;
            width: 100%;
            min-height: 100px;
            /*z-index: 10;*/
                background-color: rgba(0,0,0,0.7);
            }
</style>
        `));
            var dialog = $('#' + uid);
            dialog.find('.tool-close').click(() => {
                dialog.remove();
            });
            return dialog;
        }

        hide() {
            this.el.hide();
        }

        show() {
            this.el.show();
        }

        content(cont) {
            if (cont) {
                this.inner.html(cont)
            } else {
                return this.inner.html();
            }
        }

        fill(cont) {
            if (cont) {
                this.inner.html(cont)
            }
        }

        init_js() {
            var self = this;
            simpleMakeResizable(this.el[0]);
            makeDraggable(this.el[0], this.drag_head[0]);
            this.el.find('.window-close').click(function () {
                self.el.hide()
            });
            new FullScreenSwitch(this.el.find('.window-fullscreen'), this.el)
        }

        config_style(styles) {
            var els = Object.keys(styles);
            for (var i in els) {
                var el = els[i];
                var sty = styles[el];
                var keys = Object.keys(sty);
                for (var j in keys) {
                    var key = keys[j];
                    this[el][0].style[key] = sty[key];
                }
            }
        }

        init_style() {
            this.uclass = 'window-' + genUid();
            this.el.addClass(this.uclass);
            this.el.addClass('window');
            var style = this.getStyleString();
            var content = this.el.html();
            this.init_content = this.init_content || content || 'this is window inner.';
            this.el.html($(style));
            this.el.append(this.getHtmlString());

            this.drag_head = this.el.find('.window-header');
            this.header = this.el.find('.window-header');
            this.body = this.el.find('.window-body');
            this.inner = this.el.find('.window-inner');
            this.toolbox = this.el.find('.window-toolbox');
            this.config_style(this.init_styles);
        }

        getHtmlString() {
            return `
        <div class="window-header">
        <span class="window-bar window-close">☒</span>
        <span class="window-bar window-fullscreen"><span class=" switch-on">☐</span><span class="switch-off">❐</span></span>
        <span class="window-bar window-minimize">▣</span>
        <span class="window-title">${this.title}</span>
</div><div class="window-toolbox"></div>
        <div class="window-body">
            <div  class="window-inner">
                ${this.init_content}
            </div>
        </div>
            `
        }

        getStyleString() {
            var style = `
            <style>
           .${this.uclass} .toolbox{
           display: block;
           }
    .${this.uclass} .window-title{
           display: flex;flex-flow: row;flex: 1 1 200px;margin-left: 5px;color: whitesmoke;
    }
    .${this.uclass} .window-bar{
           margin: auto 3px auto 3px;
    }
    .${this.uclass} {
        background-color: #ff4a37;
        width: ${this.init_width}px;
        height: ${this.init_height}px;
        display: flex;
        flex-flow: column;
        resize:both;
        overflow: auto;
    }
    .${this.uclass}  .window-header {
        flex: 0 0 30px;
        background-color: deepskyblue;
        width: 100%;
        display: flex;
        flex-flow: row-reverse;
    }

    .${this.uclass}  .window-body {
        flex: auto;
        overflow: auto;
        padding: 5px;
        width: 100%;
        background-color: #f1f1f1;

    }

    .${this.uclass}  .window-inner {
        box-sizing: border-box;
        overflow: auto;
        flex: 1 0 auto;
        height: 100%;
        width: 100%;
        background-color: white;
        padding: 5px;
    }
</style>
            `
            return style;
        }
    }

    return {
        QMenubar: QMenubar,
        QWindow: QWindow
    }
}();