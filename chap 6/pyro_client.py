# pyro_client.py > ...

import Pyro4

#uri = input("insert the PYRO4 server URL (help : PYRONAME:server) ").strip()
name = input("What is your name? ").strip()
# use name server object lookup url shortcut
server = Pyro4.Proxy("PYRONAME:server")
print(server.welcomeMessage(name))