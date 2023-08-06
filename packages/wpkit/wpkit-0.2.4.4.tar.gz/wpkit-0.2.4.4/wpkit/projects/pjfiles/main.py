# from wpkit.services.CloudOS import start_server
from wpkit.linux import clean_port,get_local_ip
# port1=80
# port2=8002
# clean_port(port1)
# clean_port(port2)
# start_server(__name__,host=get_local_ip() or "127.0.0.1",port1=port1,port2=port2)
from wpkit.web.applications.demo import demo,DemoApp,LocalFSServer

def main():
    app=DemoApp(__name__)
    app.sitemap['Download']='http://%s:%s'%(get_local_ip(),8001)
    app.register_blueprint(LocalFSServer(nickname="ManageDownloads",url_prefix="/manage_download",path="/var/www/html"))
    app.run(host=get_local_ip(),port=80)
if __name__ == '__main__':
    main()
    # demo(host=get_local_ip(),port=80,import_name=__name__)