# Geo-distributed-LRU-cache

This repo simulate a geo distirbuted LRU (Last Recently Used) cache.

# How it works:

The script central.py create central server (in my implementation I create three but it can goes up or down) that will communicate 
with distributed servers to get their port and geolocation using socket library. And then with clients to send them the list of 
available servers and their geolocation.

The script server.py first connect to the central server to send its location and port, the location is randomly chosen to simulate 
different geolocation, and the port is given as a mandatory command line argument using the option -p. In case of failure server.py 
connects to the next central server.

Then the script server.py listen to its port waiting for a client to connect.

This connection is established after launching the script client.py. The script chose the closest server in the server list acquired
from the central server. In case of failure it connects to the next closest server and so on. The client can append data to the 
server cache and fetch the data from its variable name. 

The LRU cache is a class containing a deque of variables sorted by the last time they were used. Then there is a dictionary 
having as a key the variables names and the value of the variables in 'valuemap', the other dictionary contain the time of most 
recent usage of a variable. Once the cache is full and a new value needs to be appended, the last recently used variables are 
discarded until there will be enough space for the new variable and its value to be appended.

The variables of the cache expire when they exceed the time out after their most recent usage. The default value of the time out
is 10s but it can be changed. The clean up is done once new values
are appended to the cache. (I taught that keeping a thread to lookup for timeouted variables would add some complexity and I just
do not see the need to clean up the cache if nothing is happening. Also deleting variables just for being timeouted increases the 
cache misses ratio. Nevertheless, the clean up is performed whenever a new value is appended).

# The limits:

The test were succesful under my machine but it doesn't tell nothing about how would the system behave in a real geo distributed 
environement.

The servers share the same ip, (as I have only one machine to test my code) and they differ just by their port number. This limits 
the communication to one client per server.

If a client connects to two different servers one after another. He cannot benifit from the cache stored from the first one.

In a real life scenario connecting to the closest server does not guaranty the best performance depending on the trafic and the 
quality of instalations. This program does not handle this issue.

The program does not handle cache misses. Whether a variable has expired due to time out or if it is discarded for being the last 
recently used. It cannot be fetched anymore and its lost. 

For the reasons above. The program in its current state simulate quite well a geo distributed LRU cache but it is not ready yet
to be used as a library or deployed in production.

# How to use it:

Launch the script.sh in your terminal. In case you use windows try to replicates the cammands in script.sh to create the servers.

Once the server launched launche client.py. You will be prompted to enter a query, only two possible queries are possible: get or append.

To get the value of a variable from server cache, type: "get:variable_name". USE THE QUOTES.

To append new variables and their value to the server cache, type: "append:variable_name:variable_value". Do not forget the quotes.

You can also use the fuctions get_data(data) and append_data(variable,value) in the python script if you want to use the script 
with no interaction.

Both Python 2 or 3 are fine and works well with either one.



