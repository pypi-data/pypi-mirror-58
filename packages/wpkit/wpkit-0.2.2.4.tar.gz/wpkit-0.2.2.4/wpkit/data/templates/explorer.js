explorerjs = function () {
    var QWindow = winjs.QWindow;
    var pan=new panjs.Pan("http://127.0.0.1:8000/fs/cmd");
    var Editor = edjs.Editor;
    var T = wpjs.T;
    var genUid = wpjs.genUid;
    class FSItem{
        constructor(type,name) {
            this.type=type;
            this.name=name;
        }
        init(){
        }
        appendTo(parent){
        }
        source(){
        }
    }
    class Explorer {
        constructor(el) {
            if ($.isPlainObject(el)) {
                this.el = el.el;
            } else {
                this.el = el;
            }
            this.init();
        }

        init() {
            this.uclass = 'explorer-' + genUid();
            this.uid = this.uclass;
            this.window = new QWindow({
                el: this.el, title: 'Explorer'
            });
            this.window.fill(this.source().template);
            this.viewbox = $('#' + this.uid);
            this.vm = this.init_vm();
            this.window.show();
        }

        init_vm() {

            var vm= new Vue({
                el: `#${this.uid}`,
                delimiters: ['<%', '%>'],
                data: {
                    items: pan.getDir('./', './'),
                    location: "./",
                    root_path: './',
                    loc_history: ['./'],
                    window:null
                },
                methods: {
                    log: function (text) {
                        text = text || 'expolorer info....';
                        console.log(text);
                    },
                    dialog:function(e){
                        console.log('window:',this.window);
                        // this.window.dialog();
                        this.window.input((text)=>{
                            console.log('get text:',text);
                        });
                        console.log('dialog sent...');
                    },
                    input:function(msg,callback){
                      this.window.input(msg,(text)=>{callback(text);})
                    },
                    confirm:function(msg,callback){
                      this.window.confirm(msg,callback);
                    },
                    info:function(msg,callback){
                      this.window.confirm(msg,callback);
                    },
                    warn:function(msg,callback){
                      this.window.confirm(msg,callback);
                    },
                    forward: function (name) {
                        this.loc_history.push(this.location + '/' + name);
                        this.refresh();
                    },
                    backward: function () {
                        if (this.loc_history.length <= 1) {
                            return false;
                        }
                        this.loc_history.pop();
                        this.refresh();
                    },
                    goTo:function(path){
                        this.loc_history.push(path);this.refresh();
                    },
                    goHome:function(){
                        this.goTo(this.loc_history[0]);
                    },
                    refresh: function () {
                        var loc = this.loc_history.slice(-1)[0];
                        this.items = pan.getDir(this.root_path, loc);
                        this.location = loc;
                    },
                    tryNewFile: function (e) {
                        var self=this;
                        this.input('What is the file name?',function (fn) {
                            pan.newFile(self.location,fn);self.refresh();
                        })
                    },
                    tryNewDir: function (e) {
                        var self=this;
                        this.input('What is the directory name?',function (dn) {
                            pan.newDir(self.location,dn);self.refresh();
                        })
                    },
                    trySaveFile: function (location,filename,content) {
                        var res=pan.saveFile(location,filename,content);
                        if(!res){this.warn("Cannot save file! An error occured!")}
                        else{this.info("Succeeded!")}

                    },
                    tryDeleteFile: function (name) {
                        var self=this;
                        this.confirm(`Are You sure to delete the file ${name}?`,function () {
                            pan.deleteFile(self.location, name);
                            self.refresh();
                        })
                    },
                    tryDeleteDir: function (name) {
                        var self=this;
                        this.confirm('Are You sure to delete the directory?',function () {
                            pan.deleteDir(self.location, name);
                            self.refresh();
                        })
                    },
                    tryDelete:function(e){
                        var selected=this.selected();
                        console.log(e,selected)
                        selected.map((v,i)=>{
                            var item=$(v);
                            var type=item.attr("itemtype");
                            var name=item.attr("itemname");
                            if(type==T.DIR)this.tryDeleteDir(name);
                            else if(type==T.FILE)this.tryDeleteFile(name);
                        })
                    },
                    unselectAllItems:function(){
                        var el=$(this.$el);
                        var items=el.find(".flist-item");
                        items.map((v,i)=>{
                            var item=$(i);
                            // item.attr("item-selected","false");
                            item.removeClass("fitem-selected");
                        });
                    },
                    selectItem:function(e){
                        e.preventDefault();
                        e.stopPropagation();
                        //console.log(e)
                        var obj = $(e.target).parent();
                        this.unselectAllItems();
                        // obj.attr("item-selected","true");
                        obj.addClass("fitem-selected");
                    },
                    selected:function(){
                        var el=$(this.$el);
                        var items=el.find(".flist-item");
                        var selected=[];
                        items.map((i,v)=>{
                           var item=$(v);
                           // if(item.attr("item-selected")=="true"){selected.push(v)}
                           if(item.hasClass("fitem-selected")){selected.push(v)}
                        });
                        return selected;
                    },
                    updateView: function (e) {
                        console.log(e.target);
                        var obj = $(e.target).parent('.flist-item');
                        var name = obj.attr('itemname');
                        var type = obj.attr('itemtype');
                        switch (type) {
                            case T.DIR:
                                this.forward(name);
                                break;
                            case T.FILE:
                                var content = pan.getFile(this.location, name);
                                var ed=new Editor({
                                    pan:pan,
                                    location:this.location,
                                    filename:name
                                });
                                ed.add_content(content);
                                ed.show();
                                break;
                            default:
                                null;
                                break;
                        }

                    }
                }
            });
            vm.$data.window=this.window;
            console.log('window init:',vm.$window)
            return vm;
        }

        source() {
            return {
                template: `<div class="w-100 h-100 explorer" id="${this.uid}" @click="unselectAllItems">
        <div class="text-info head">
            <span class="label-primary menu-item" @click="goHome">Home</span><span @click="backward" class="label-public menu-item">Back</span>
            <span class="label-primary menu-item" @click="tryNewFile">New File</span><span class="label-public menu-item" @click="tryNewDir">New Dir</span>
            <span @click="tryDelete" class="label-primary menu-item">Delete</span><span @click="refresh" class="label-primary menu-item">Refresh</span>
        </div>
        <div class="body" >
            <div class="flist-item" v-bind:itemname="fileitem.name" v-bind:itemtype="fileitem.type" 
                 v-for="fileitem in items">
                <label @dblclick="updateView" @click="selectItem" ><%fileitem.name%></label>
                <label><%fileitem.type%></label>
            </div>
        </div>
    </div>
    <style>
        #${this.uid} {
            display: flex;
            flex-flow: column;
        }
        #${this.uid} .head {
            flex: 0 1 40px;
            width: 100%;
            background-color: white;color: orange;
            border-bottom: black dotted 2px;
        }
        #${this.uid} .head .menu-item{
            margin:auto 3px auto 3px;
            padding: auto 3px auto 3px !important;
            border: solid gray 2px;
        }
        #${this.uid} .flist-item{
            border-bottom: dotted 2px black;
        }
        #${this.uid} .body {
            flex: 1 0 auto;
            max-height: calc(90% - 40px);
            /*height: 300px;*/
            width: 100%;
            background-color: white;
            color: orange;
            overflow: auto;
        }
        #${this.uid} .fitem-selected{
            background-color: dodgerblue;color:white;
        }
    </style>`,
                style: ``
            }
        }

    }

    return {
        Explorer: Explorer
    }
}();
