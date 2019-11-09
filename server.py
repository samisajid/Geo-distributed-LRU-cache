# first of all import the socket library 
import socket		
import getopt	 
import sys
import random
import time
import lru

recvsize=9999999
def server():
    # next create a socket object 
    s = socket.socket()		 
    print ("Socket successfully created")
    
    # reserve a port on your computer in our 
    # case it is 1234 but it can be anything 
    
    # Next bind to the port 
    # we have not typed any ip in the ip field 
    # instead we have inputted an empty string 
    # this makes the server listen to requests 
    # coming from other computers on the network 
    s.bind(('', port))		 
    print ("socket binded to {}".format(port))
    
    # put the socket into listening mode 
    s.listen(3)	 
    print ("socket is listening")			
    
    
    # a forever loop until we interrupt it or 
    # an error occurs 
    while True: 
        # Establish connection with client. 
        c, addr = s.accept()	 
        print ('Got connection from', addr)
        
        # send a thank you message to the client. 
        c.send(b'You are connected to the port {}'.format(port)) 
        while True:
            query=c.recv(1024).split(':')
            if len(query)>1:
                print("query",query)
                if query[0]=="append":
                    a,b=query[1:]
                    print(a,b)
                    server_cache.append(a,b)
                    print("serveur",server_cache.valuemap)
                elif query[0]=="get":
                    data=server_cache.get(query[1])
                    print(data)
                    c.send(b'{}'.format(data))
                else:
                    print("invalid query")   
            else:
                print("A query was expected")
                break
            
        print(server_cache.clist)
        print(server_cache.timemap)
        
        # Close the connection with the client 
        #c.close() 
def client(port):        
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
        
        # connect to the server on local computer 
        c.connect((socket.gethostname(), port)) 
          
        # receive data from the server 
        print (c.recv(1024))
        c.send(b'server')
        c.send(b'{}'.format(portinfo))
        print(c.recv(recvsize))
        c.close()
    except socket.error:
        print("Unable to connect to port {}".format(port))
        port+=1
        if port<num_central_server:
            print("Trying to connect to port {}".format(port))
            client(port)
        else:
            print("The location of this server cannot be delivered to central servers")
            sys.exit()

if __name__=='__main__':
    #The script takes an argument of the port the server is bound to
    csize=1024
    timeout=10
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, 'hp:t:c:')
    except getopt.GetoptError:
        #Print a message or do something useful
        print('Something went wrong!')
        sys.exit(2)
    print(opts)
    print(args)
    for op,ar in opts:
        print(op,ar)
        if op=="-t":
            try:
                timeout=float(ar)
            except:
                print("The timeout value is not a number")
                sys.exit()
        elif op=="-c":
            try:
                csize=int(ar)
            except:
                print("The cache size value is not an integer")
                sys.exit()
        elif op=="-p":
            try:
                port = int(ar)
            except:
                print("The port value is not an integer")
                sys.exit()
        elif op=="-h":
            print("Create a server with a LRU cache")
            print("-p        Indicate the port value of the server, it is a mandatory argument")
            print("-c        Indicate the size of the cache, the default value is 1024")
            print("-t        Indicate the timeout after whiche the cache expires, default value is 10s")
            sys.exit()
    print(timeout,csize,port)
    #Random location of the server to simulate geo distribution
    coor=[random.uniform(-90,90),random.uniform(-180,180)]
    portinfo={port:coor}
    num_central_server=3
    #Connect to the central server in port 10000
    client(10000)
    #Create the server cache
    
    server_cache=lru.LRUcache(csize)
    #Ready to serve clients
    server()
    
    
