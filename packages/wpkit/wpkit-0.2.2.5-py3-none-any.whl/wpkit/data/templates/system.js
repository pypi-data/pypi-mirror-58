sysjsData={};
sysjs=function () {
    var QWindow=winjs.QWindow;
    var QMenubar=winjs.QMenubar;

    var Application=class{
        constructor() {
            this.window=new QWindow();

        }
    };
    var openerMap={

    };
    sysjsData.openerMap=openerMap;
    var registerOpener=function(ext,opener){
        openerMap[ext]=opener;
    };
    var openFile=function(pan,location,filename){
        // console.log('opening file...',filename);
        // console.log(openerMap);
        var parts=filename.split('.');
        if(parts.length>1){
            // console.log(filename)
            var ext='.'+parts.slice(-1)[0];
            console.log(ext)
            console.log(Object.keys(openerMap))
            console.log(Object.keys(openerMap).indexOf(ext))
            if(Object.keys(openerMap).indexOf(ext)>-1){
                var opener=new openerMap[ext]();
                // console.log(opener)
                opener.openFile(pan,location,filename);
                // console.log(opener)
            }
        }
    };
    return {
        openFile:openFile,
        registerOpener:registerOpener
    }
}();