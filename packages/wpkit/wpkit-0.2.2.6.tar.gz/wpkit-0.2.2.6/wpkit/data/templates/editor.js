edjs = function () {
    var {QWindow, QMenubar} = winjs;
    var {genUid, isdefined} = wpjs;
    var {registerOpener, QDesktopApplication, QEvent} = sysjs;

    class Editor extends QDesktopApplication {
        constructor(el, content, pan, location, filename) {
            super();
            if ((el != null) && ($.isPlainObject(el))) {
                this.el = el.el;
                this.init_content = el.content;
                this.pan = el.pan;
                this.location = el.location;
                this.filename = el.filename;
            } else {
                this.el = el;
                this.init_content = content;
                this.pan = pan;
                this.location = location;
                this.filename = filename;
            }
            this.window.title = 'Editor';
            this.onStart.push(() => {
                this.init();
            });
            this.onDisplay.push(() => {
                console.log(this)
                this.initStyles();
            })
        }

        addEventListeners() {
            super.addEventListeners();
            this.window.listenCtrlKeydown(83, (e) => {
                this.saveFile((res)=>{
                    if(res)this.window.clearDialog();
                });
            })
        }

        initStyles() {
            var el = this.window.find('#' + this.uid);
            el.css({
                "height": "100%",
                "display": "flex",
                "flex-flow": "column",
            });
            el.find(".taskbar").css({
                "flex": "0 0"
            });
            el.find(".body").css({
                "flex": "1 0 auto",
                "display": "flex",
                "flex-flow": "column"
            })

        }

        init() {
            this.menubar = new QMenubar({});
            if (isdefined(this.menubar)) {
                var self = this;
                this.menubar.addItem('save', () => {
                    self.saveFile();
                })
            }
            this.init_content = this.init_content || 'Write some thing here...';
            this.window.setContent(this.html());
            this.content_box = this.window.find('.edit-area');
        }

        info(msg) {
            this.window.info(msg);
        }

        saveFile(callback) {
            var self=this;
            console.log({
                location: self.location,
                filename: self.filename,
                content: self.getContent()
            });
            var res = self.pan.saveFile(self.location, self.filename, self.getContent());
            if (res) self.info("Succeeded to save file!");
            if(typeof callback==='function')callback(res);
        }

        openFile(pan, location, filename) {
            console.log('open', filename);
            this.pan = pan;
            this.location = location;
            this.filename = filename;
            var content = pan.getFile(location, filename);
            this.add_content(content);
        }

        add_content(cont) {
            return this.content_box.html(cont);
        }

        getContent() {
            var content = this.content_box.val();
            return content
        }

        html() {
            return `<div id="${this.uid}">
                ${this.menubar.toString()}
        <div class="body" style="display: flex;flex-flow: column;background-color: dimgray">
        <textarea class="edit-area" style="flex:1 0 auto;width: 100%;overflow: auto">
        ${this.init_content}
</textarea>
        </div>
                </div>`
        }
    }

    if (typeof sysjs != "undefined") {
        registerOpener('.txt', Editor);
        registerOpener('.py', Editor);
    }
    return {
        Editor: Editor
    }
}();