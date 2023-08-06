edjs=function () {
    var QWindow=winjs.QWindow;
    var QMenubar=winjs.QMenubar;
    var genUid=wpjs.genUid;
    var isdefined=wpjs.isdefined;
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
                    })
                    self.pan.saveFile(self.location,self.filename,self.getContent());
                })
            }
            this.init_content=this.init_content || this.el.html() || 'Write some thing here...';
            this.el.html(this.html());
            this.window=new QWindow({el:this.el,title:'Editor'});
            this.content_box=this.el.find('.edit-area');
            this.hide();
        }
        hide(){
            this.window.hide();
        }
        show(){
            this.window.show();
        }
        add_content(cont){
            console.log("add content:",this.content_box);
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
    return{
        Editor:Editor
    }
}();