panjs = function () {
    var postJson = wpjs.postJson;
    var uploadFile = wpjs.uploadFile;

    class RemoteDB {
        constructor(url) {
            this.url = url;
            this.cmd_url = url + '/cmd';
        }

        execute(cmd) {
            console.log(cmd);
            var res = postJson(this.cmd_url, cmd).responseJSON;
            console.log(res);
            if (res.success) return res.data;
            else {
                console.log("Error!", res);
                return res.data;
            }
        }

        add(key, value) {
            var cmd = {cmd: {op: "add", params: {key: key, value: value}}};
            return this.execute(cmd);
        }

        get(key) {
            var cmd = {cmd: {op: "get", params: {key: key}}};
            return this.execute(cmd);
        }

        delete(key) {
            var cmd = {cmd: {op: "delete", params: {key: key}}};
            return this.execute(cmd);
        }

        recover(ket, step) {
            var cmd = {cmd: {op: "recover", params: {key: key, step: step}}};
            return this.execute(cmd);
        }
    }

    class RemoteFS {
        constructor(url) {
            this.url = url;
            this.cmd_url = this.url + '/cmd';
            this.upload_url = this.url + '/upload';
        }

        execute(cmd) {
            // console.log(cmd);
            var res = postJson(this.cmd_url, cmd).responseJSON;
            // console.log(res);
            if (res.success) return res.data;
            else {
                console.log("Cmd Error!", res);
                return res.data;
            }
        }
        getUrl(location,name){
            var cmd = {cmd: {op: "getUrl", params: {location: location, name: name}}};
            return this.execute(cmd);
        }
        getDir(location, dirname) {
            var cmd = {cmd: {op: "getDir", params: {location: location, dirname: dirname}}};
            return this.execute(cmd);
        }

        getFile(location, filename) {
            var cmd = {cmd: {op: "getFile", params: {location: location, filename: filename}}};
            return this.execute(cmd);
        }

        newDir(location, dirname) {
            var cmd = {cmd: {op: "newDir", params: {location: location, dirname: dirname}}};
            return this.execute(cmd);
        }

        newFile(location, filename) {
            var cmd = {cmd: {op: "newFile", params: {location: location, filename: filename}}};
            return this.execute(cmd);
        }

        saveFile(location, filename, content) {
            var cmd = {cmd: {op: "saveFile", params: {location: location, filename: filename, content: content}}};
            return this.execute(cmd);
        }

        deleteFile(location, name) {
            var cmd = {cmd: {op: "delete", params: {location: location, name: name}}};
            return this.execute(cmd);
        }

        deleteDir(location, name) {
            var cmd = {cmd: {op: "delete", params: {location: location, name: name}}};
            return this.execute(cmd);
        }

        uploadFile(location, filename, file, callback) {
            var info = {
                info: {
                    location: location,
                    filename: filename,
                    file: file
                }
            };
            uploadFile(this.upload_url, file, info, (res) => {
                console.log(res);
                if(typeof callback!="undefined")callback(res);
                if (res.success) return res.data;
                else {
                    console.log("Error!", res);
                    return res.data;
                }
            });

        }
    }

    class Pan extends RemoteFS {
        constructor(url) {
            super(url);
        }

        pull() {
            var cmd = {cmd: {op: "pull", params: {}}};
            return this.execute(cmd);
        }

        push() {
            var cmd = {cmd: {op: "pull", params: {}}};
            return this.execute(cmd);
        }
    }

    return {
        RemoteDB: RemoteDB,
        RemoteFS: RemoteFS,
        Pan: Pan
    }
}();