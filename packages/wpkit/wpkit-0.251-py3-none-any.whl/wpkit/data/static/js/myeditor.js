class Editor {
        constructor(el) {
            this.el=el;
            el.resizable({
                addClass:false
            });
            el.draggable().click(function () {
                $(this).draggable({disabled: false});
            }).dblclick(function () {
                $(this).draggable({disabled: true});
            });
            // console.log($('#editor-style'))
            this.init();
        }
        init(){
            var style= this.style();
            this.el.append($(style));
            this.el.addClass('editor-window');
            this.el.append($(this.html()));
        }
        html(){
           return `
        <div class="window-header"></div>
        <div class="window-inner">
            <div contenteditable="true" class="editable-area">
                this is possible
            </div>
        </div>
            `

        }
        style(){
            var style=`
            <style id="editor-style">
    .editor-window {
        background-color: #ff4a37;
        width: 400px;
        height: 400px;
        /*max-width: 400px;*/
        /*max-height: 400px;*/
        display: flex;
        flex-flow: column;
    }
    .window-header {
        flex: 0 0 30px;
        background-color: deepskyblue;
        width: 100%;
    }

    .window-inner {
        flex: auto;
        overflow: auto;
        padding: 5px;
        width: 100%;
        background-color: #f1f1f1;

    }

    .editable-area {
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