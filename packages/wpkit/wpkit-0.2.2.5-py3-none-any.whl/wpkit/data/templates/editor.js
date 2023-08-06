edjs=function () {
    var QWindow=winjs.QWindow;
    var QMenubar=winjs.QMenubar;
    var genUid=wpjs.genUid;
    var isdefined=wpjs.isdefined;
    if(isdefined(sysjs)){var registerOpener = sysjs.registerOpener;}
    class Editor {
        constructor(el, content,pan,location,filename) {
            if ((el != null) && ($.isPlainObject(el))) {
                this.el = el.el;
                this.init_content = el.content ;
                this.pan=el.pan;
                this.location=el.location;
                this.filename=el.filename;
            } else {
                this.el = el;
                this.init_content = content ;
                this.pan=pan;
                this.location=location;
                this.filename=filename;
            }
            if(!this.el){
                var uid='editor-'+genUid();
                console.log('uid:',uid)
                $('body').prepend($(`<div id="${uid}"></div>`));
                this.el=$('#'+uid);
            }
            this.uid=genUid();
            this.menubar=new QMenubar({});
            if(isdefined(this.menubar)){
                var self=this;
                this.menubar.addItem('save',()=>{
                    console.log({
                        location:self.location,
                        filename:self.filename,
                        content:self.getContent()
                    });
                    var res=self.pan.saveFile(self.location,self.filename,self.getContent());
                    if(res)self.info("Succeeded to save file!");
                })
            }
            this.init_content=this.init_content || this.el.html() || 'Write some thing here...';
            this.window=new QWindow({title:'Editor'});
            this.window.setContent(this.html());
            this.window.appendTo(this.el);
            this.content_box=this.el.find('.edit-area');
            this.hide();
        }
        info(msg){
            this.window.info(msg);
        }
        hide(){
            this.window.hide();
        }
        show(){
            this.window.show();
        }
        openFile(pan,location,filename){
            console.log('open',filename);
            this.pan=pan;
            this.location=location;
            this.filename=filename;
            var content=pan.getFile(location,filename);
            this.add_content(content);
            this.show();
        }
        add_content(cont){
            // console.log("add content:",this.content_box);
            return this.content_box.html(cont);
        }
        getContent(){
            return this.content_box.html();
        }
        html(){
            return `<div class="${this.uid}">
                ${this.menubar.toString()}
        <div class="body edit-area"  contenteditable="true">
            ${this.init_content}
        </div>
                </div>`
        }
    }
    if(typeof sysjs!="undefined"){
        registerOpener('.txt',Editor);
        registerOpener('.py',Editor);
    }
    return{
        Editor:Editor
    }
}();