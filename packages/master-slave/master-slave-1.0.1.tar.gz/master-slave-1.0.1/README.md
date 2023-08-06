# Python Henallux Project 2019
Usage informations about master.py and slave.py classes
## Class Master

Usage:
```python
from master-slave import Master

master = Master(address="", port=50000)
   # address = address to listen to (empty mean listenning on all addresses)
   # port = listening port 
master.start()
```

## Class Slave

Usage:
```python
from master-slave import Slave

slave = Slave(address="192.168.0.10", port=50000)  
   # address = address of master
   # port = listening port of master
slave.start()
```
