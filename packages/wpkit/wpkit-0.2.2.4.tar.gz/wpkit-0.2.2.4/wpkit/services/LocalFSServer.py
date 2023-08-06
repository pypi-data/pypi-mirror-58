from wpkit.pan import LocalFSHandle,Pan
from flask import Blueprint,Flask,jsonify
from wpkit.web.utils import parse_json
from wpkit.basic import Status,StatusError,StatusSuccess
from flask_cors import CORS
class LocalFSServer(LocalFSHandle,Flask):
    def __init__(self,import_name,path="./",url="/fs/cmd",*args,**kwargs):
        LocalFSHandle.__init__(self,path)
        Flask.__init__(self,import_name=import_name,*args,**kwargs)
        self.url = url
        self.add_handlers()

        CORS(self,resources=r'/*')
    def add_handlers(self):
        @self.route(self.url,methods=['POST'])
        @parse_json
        def do_cmd(cmd):
            print("cmd:", cmd)
            try:
                res = self.execute(cmd)
                res = StatusSuccess(data=res)
            except:
                res = StatusError()
            # print(res)
            return jsonify(res)






