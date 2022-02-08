import consul

class Consul(object):
    def __init__(self, host, port):
        '''Initialization, connect the consul server'''
        self._consul = consul.Consul(host, port)

    def RegisterService(self, name, host, port, tags=None):
        tags = tags or []
        #  Registration service
        self._consul.agent.service.register(
            name,
            name,
            host,
            port,
            tags,
            #  Health check IP port, check time: 5, timeout time: 30, logout time: 30s
            check=consul.Check().tcp(host, port, "5s", "30s", "30s"))

    def GetService(self, name):
        services = self._consul.agent.services()
        service = services.get(name)
        if not service:
            return None, None
        addr = "{0}:{1}".format(service['Address'], service['Port'])
        return service, addr

if __name__ == '__main__':
    host="consul-server" #IP of the consul server
    port="8500" #Consul server external port
    consul_client=Consul(host,port)

    name="fyber-lab"
    host="consul-server"
    port=8500
    consul_client.RegisterService(name,host,port)

    check = consul.Check().tcp(host, port, "5s", "30s", "30s")
    print(check)
    res=consul_client.GetService("maple")
    print(res)