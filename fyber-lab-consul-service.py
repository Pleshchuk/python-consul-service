import consul

class Consul(object):
    def __init__(self, host, port):
        '''Initialization, connect the consul server'''
        self._consul = consul.Consul(host, port)

    def SetValue(self, key, value):
        self._consul.kv.put(key, value)

    def GetValue(self, key):
        return self._consul.kv.get(key)

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
    check = consul.Check().tcp(host, port, "5s", "30s", "30s")
    print(check)
    consul_client.RegisterService(name,host,port)

    res=consul_client.GetService("fyber-lab")
    print(res)

    key = "service-name"
    value = name
    print("Set key %s with value %s" % (key, value))
    consul_client.SetValue(key, value)

    print("Get key %s" % key)
    res=consul_client.GetValue(key)
    print(res)
