
winjs = function () {
    var FullScreenSwitch = swjs.FullScreenSwitch;
    var genUid = wpjs.genUid;
    var isdefined = wpjs.isdefined;
    var makeDraggable = wpjs.makeDraggable;
    var simpleMakeResizable = wpjs.simpleMakeResizable;

    class QWedget{
        constructor(className) {
            className=className||'QWedget';
            this.uid=className+genUid();
            this.active=false;
        }
        help(){
            var doc=`
            Please re-implement these methods:
                activate()
                source()
            `;
            console.log(doc);
            return doc;
        }
        el(){
            return $("#"+this.uid);
        }
        find(arg){
            return this.el().find(arg);
        }
        hide(){
            return this.el().hide();
        }
        show(){
            return this.el().show();
        }
        remove(){
            this.el().remove();
        }
        activate(){
            this.active=true;
            // console.log("The method 'activate' must be re-implemented by subclasses.'");
        }
        hookParent(el){
            return this.appendTo(el);
        }
        appendTo(el){
            if(el){
                $(el).append(this.toString());
            }
            this.activate();
        }
        hook(el){
            if(el){
                $(el).replaceWith(this.toString());
            }
            this.activate();
        }
        update(){
            if(this.active){
                var el=this.el();
                el.replaceWith(this.toString());
                this.activate();
            }
        }
        source(){
            throw "The method 'source()' must be re-implemented bu subclasses.";
            return {
                template: ``,
                style: ``,
                script: ``
            }
        }
        toString(){
            var src=this.source();
            return src.template+src.style||''+src.script||'';
        }
    }

    class QMenubar extends QWedget{
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
    emitQEvent=function (name,params) {
        dispatchEvent(new CustomEvent("qevent-"+name,{
            detail:params
        }));
    };
    class QDialog extends QWedget{
        constructor(content) {
            super("Dialog");
            if($.isPlainObject(content)){
                var obj=content;
                this.content=obj.content;
            }else if(typeof content!="undefined"){
                this.content=content;
            }
        }
        activate(){
            this.active=true;
            var el=this.el();
            el.find(".handle-close").click(()=>{
                    el.remove();
            });
        }
        close(){
            return this.remove();
        }
        setContent(content){
            this.content=content;
            this.update();
        }
        getContent(){
           if(!this.content)return '';
           else return this.content;
        }
        source(){
            return{
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
    class QWindow extends QWedget{
        constructor(title,width,height,content) {
            super("QWindow");
            if($.isPlainObject(title)){
                var el=title;
                this.title=el.title;
                this.init_width=el.width;
                this.init_height=el.height;
                this.init_content=el.content;
            }else{
                this.title=title;
                this.init_width=width;
                this.init_height=height;
                this.init_content=content;
            }
            this.title=this.title||'Window';
            this.init_width=this.init_width||450;
            this.init_height=this.init_height||400;
            this.init_content=this.init_content||'';
        }
        activate() {
            super.activate();
            var self = this;
            simpleMakeResizable(this.el()[0]);
            makeDraggable(this.el()[0], this.getHead()[0]);
            this.el().find('.window-close').click(function () {
                self.hide();
            });
            new FullScreenSwitch(this.el().find('.window-fullscreen'), this.el());
        }
        minimize(){

        }
        maximize(){

        }
        restore(){

        }
        inputFile(msg,callback){
            return this.input(msg,callback,'file');
        }
        inputText(msg,callback){
            return this.inputText(msg,callback,'text');
        }
        input(msg,callback,type){
            type=type||'text';
            var content=`
            <div style="text-align: center">
            <input class="input" type="${type}">
            <button class="btn-submit">submit</button>
</div>
            `;
            var dialog=this.dialog(content);
            dialog.el().find(".btn-submit").click(()=>{
                var input=dialog.el().find(".input");
                if(type==='file'){
                    callback(input.val(),input[0].files);
                }else{
                    callback(input.val());
                }
                dialog.remove();
            });
            $(document).keydown((e)=>{
                if(e.keyCode===13){
                    dialog.el().find(".btn-submit").click();
                }
            })

        }
        confirm(msg,callback){
            var content=`
                <div style="text-align: center"><label>${msg}</label></div>
                <div style="text-align: center">
                <button class="btn-yes">YES</button><button class="btn-no">NO</button>
</div>
            `;
            var dialog=this.dialog(content);
            $(document).keydown((e)=>{
                if(e.keyCode===13){
                    dialog.el().find(".btn-yes").click();
                }
            });
            dialog.el().find(".btn-yes").click((e)=>{
                if(callback){callback()}
                dialog.remove();
            });
            dialog.el().find(".btn-no").click((e)=>{
                dialog.remove();
            })
        }
        success(msg){
            return this.msg(msg);
        }
        warn(msg){
            return this.msg(msg);
        }
        info(msg){
            return this.msg(msg);
        }
        msg(msg){
            var content=`
                <div style="text-align: center"><label>${msg}</label></div>
                <div style="text-align: center" class="btn-ok" onclick="">OK</div>
            `;
            var dialog=this.dialog(content);
            dialog.el().find(".btn-ok").click((e)=>{
                dialog.close();
            });
            $(document).keydown((e)=>{
                if(e.keyCode===13){
                    dialog.el().find(".btn-ok").click();
                }
            })
        }
        dialog(content){
            var dialog=new QDialog();
            dialog.setContent(content);
            dialog.appendTo(this.getDialog());
            return dialog;
        }
        getHead(){
            return this.el().find(".qwindow-head");
        }
        getDialog(){
            return this.el().find(".qwindow-dialog");
        }
        getBody(){
            return this.el().find(".qwindow-body");
        }
        getInner(){
            return this.getBody().find(".qwindow-inner");
        }
        setContent(content){
            if(!this.active){
                this.init_content=content;
            }else{
                this.getInner().html(content);
            }
        }
        getContent(){
            if(!this.active){
                return this.init_content;
            }else{
                return this.getInner().html();
            }
        }
        source(){
            return {
                template:
                `
                <div id="${this.uid}">
                <div class="qwindow-head">
                <span class="window-bar window-close">☒</span>
        <span class="window-bar window-fullscreen"><span class=" switch-on">☐</span><span class="switch-off">❐</span></span>
        <span class="window-bar window-minimize">▣</span>
        <span class="window-title">${this.title}</span>
</div>
                <div class="qwindow-dialog">
                
</div>
                <div class="qwindow-body">
                <div class="qwindow-inner">
                ${this.getContent()}          
</div>
</div>
</div>
                `,
                style:
                `
            <style>
           #${this.uid} .qwindow-head{
           display: block;
           }
    #${this.uid} .window-title{
           display: flex;flex-flow: row;flex: 1 1 200px;margin-left: 5px;color: whitesmoke;
    }
    #${this.uid} .window-bar{
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
            `
            }
        }
    }


    return {
        QWedget:QWedget,
        QDialog:QDialog,
        QMenubar: QMenubar,
        QWindow: QWindow
    }
}();