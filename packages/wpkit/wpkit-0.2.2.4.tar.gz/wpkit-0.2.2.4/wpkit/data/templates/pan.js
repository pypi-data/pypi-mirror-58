panjs = function () {
    var postJson = wpjs.postJson;
    class RemoteDB{
        constructor(url) {
            this.url=url;
        }
        execute(cmd){
            console.log(cmd);
            var res = postJson(this.url, cmd).responseJSON;
            console.log(res);
            if(res.success)return res.data;
            else {
                console.log("Error!",res);
                return res.data;
            }
        }
        add(key,value){
            var cmd={cmd:{op:"add",params:{key:key,value:value}}};
            return this.execute(cmd);
        }
        get(key){
            var cmd={cmd:{op:"get",params:{key:key}}};
            return this.execute(cmd);
        }
        delete(key){
            var cmd={cmd:{op:"delete",params:{key:key}}};
            return this.execute(cmd);
        }
        recover(ket,step){
            var cmd={cmd:{op:"recover",params:{key:key,step:step}}};
            return this.execute(cmd);
        }
    }
    class RemoteFS {
        constructor(url) {
            this.url = url;
        }
        execute(cmd){
            console.log(cmd);
            var res = postJson(this.url, cmd).responseJSON;
            console.log(res);
            if(res.success)return res.data;
            else {
                console.log("Error!",res);
                return res.data;
            }
        };

        getDir (location, dirname) {
            var cmd = {cmd: {op: "getDir", params: {location: location, dirname: dirname}}};
            return this.execute(cmd);
        };
        getFile = function (location, filename) {
            var cmd = {cmd: {op: "getFile", params: {location: location, filename: filename}}};
            return this.execute(cmd);
        };
        newDir = function (location, dirname) {
            var cmd = {cmd: {op: "newDir", params: {location: location, dirname: dirname}}};
            return this.execute(cmd);
        };
        newFile = function (location, filename) {
            var cmd = {cmd: {op: "newFile", params: {location: location, filename: filename}}};
            return this.execute(cmd);
        };
        saveFile = function (location, filename, content) {
            var cmd = {cmd: {op: "saveFile", params: {location: location, filename: filename, content: content}}};
            return this.execute(cmd);
        };
        deleteFile = function (location, name) {
            var cmd = {cmd: {op: "delete", params: {location: location, name: name}}};
            return this.execute(cmd);
        };
        deleteDir = function (location, name) {
            var cmd = {cmd: {op: "delete", params: {location: location, name: name}}};
            return this.execute(cmd);
        };
    }
    class Pan {
        constructor(url) {
            this.url = url;
        }
        execute(cmd){
            console.log(cmd);
            var res = postJson(this.url, cmd).responseJSON;
            console.log(res);
            if(res.success)return res.data;
            else {
                console.log("Error!",res);
                return null;
            }
        };
        pull(){
            var cmd={cmd:{op:"pull",params:{}}};
            return this.execute(cmd);
        };
        push(){
            var cmd={cmd:{op:"pull",params:{}}};
            return this.execute(cmd);
        };
        getDir (location, dirname) {
            var cmd = {cmd: {op: "getDir", params: {location: location, dirname: dirname}}};
            return this.execute(cmd);
        };
        getFile = function (location, filename) {
            var cmd = {cmd: {op: "getFile", params: {location: location, filename: filename}}};
            return this.execute(cmd);
        };
        newDir = function (location, dirname) {
            var cmd = {cmd: {op: "newDir", params: {location: location, dirname: dirname}}};
            return this.execute(cmd);
        };
        newFile = function (location, filename) {
            var cmd = {cmd: {op: "newFile", params: {location: location, filename: filename}}};
            return this.execute(cmd);
        };
        saveFile = function (location, filename, content) {
            var cmd = {cmd: {op: "saveFile", params: {location: location, filename: filename, content: content}}};
            return this.execute(cmd);
        };
        deleteFile = function (location, name) {
            var cmd = {cmd: {op: "delete", params: {location: location, name: name}}};
            return this.execute(cmd);
        };
        deleteDir = function (location, name) {
            var cmd = {cmd: {op: "delete", params: {location: location, name: name}}};
            return this.execute(cmd);
        };

    }

    return {
        RemoteDB:RemoteDB,
        RemoteFS:RemoteFS,
        Pan: Pan
    }
}();