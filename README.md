## Service introduction
In this repo you can see demo project. This project uses python library ```consul``` for interacting with consul server

In ```fyber-lab-consul-service.py``` file is described class for registering service on consul server. 

Also, you can see there setter and getter methods for adding and getting key/values to/from consul server.
It creates key/value and gets it once docker image starts. No any interaction can be done after executing docker etrypoint.

## Service packaging
The project packages into docker image which uses ```fyber-lab-consul-service.py``` file as entrypoint.
