import socket                
import getopt	 
import sys
import random
import time
import operator
from math import sin, cos, sqrt, atan2, radians


def distance(a,b):
    '''Calculate the distance between two coordinates in earth'''
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(a[0])
    lon1 = radians(a[1])
    lat2 = radians(b[0])
    lon2 = radians(b[1])
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    p = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(p), sqrt(1 - p))
    
    return R * c

def get_server(por):
    '''Connect to the central server to get the list of the available servers and their locations'''
    try:
        # Create a socket object 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
          
        # connect to the server on local computer 
        s.connect((socket.gethostname(), por)) 
          
        # receive data from the server 
        print (s.recv(1024))
        
        #send client to tell the central server that it is a client and not a server
        s.send(b'client')        
        servers=eval(s.recv(1024))
        # close the connection 
        s.close()      
        return servers
    except socket.error:
        print("Unable to connect to port {}".format(por))
        por+=1
        if por<num_central_server:
            print("Trying to connect to port {}".format(por))
            client(por)
        else:
            print("The location of this server cannot be delivered to central servers")
            sys.exit()
def client(p):
    '''Establish the connection with the server and send data to be appended to cache
    and query the data in the cache'''
    try:        
        # connect to the server on the closest port to the client
        c.connect((socket.gethostname(), sorted_dict[p][0])) 
        #prints the port connected
        print(c.recv(1024))
        print("You are located at {} and the server is located at {}".format(coor,list_server[sorted_dict[p][0]]))
        print("It is {} km far away".format(sorted_dict[p][1]))
        #testing the cache with some random variable
        append_data('some_variable','some_value')
        print("The value of 'some_variable' is: {}".format(get_data('some_variable')))
        
        #This while loop is an interactive CLI to append and get data from the server cache
        #The query should be formulated this way: either "get:variable_name"
        #or "append:variable_name:variable_value"
        while True:
            message=input("$")
            print("This is your query",message)            
            if message not in ['q','quit','exit']:
                c.sendall(b'{}'.format(message))
                if message.split(':')[0]=="get":
                    print(c.recv(recvsize))
            else:
                break
        c.close()
    except socket.error:
        print("Unable to connect to port {}".format(sorted_dict[p][0]))
        p+=1
        if p<server_num:
            print("Trying to connect to port {}".format(sorted_dict[p][0]))
            client(p)
        else:
            print("Unable to establish connection with any server")
            sys.exit()
def get_data(data):
    '''Send a query to the server to get the value associated with the data 
       and return it'''
    c.sendall(b'get:{}'.format(data))
    recieved=c.recv(recvsize)
    return recieved
def append_data(a,b):
    '''Send a string to be decoded by the server to append the pair a:b in the cache '''
    c.sendall(b'append:{}:{}'.format(a,b))

if __name__=='__main__':
    #get random coordinates of the client to simulate geo distribution
    coor=[random.uniform(-90,90),random.uniform(-180,180)]
    port=10000
    recvsize=9999999
    num_central_server=3
    #get a dictionnary of the ports of the servers and their locations
    list_server=get_server(port)
    if list_server=={}:
        print("No server is available, try later")
    server_num=len(list_server)
    #create a dictionary of the servers and their distance from the client location
    dict_distance={}
    for j,k in list_server.items():
        dict_distance[j]=distance(coor,k)
    sorted_dict=sorted(dict_distance.items(),key=operator.itemgetter(1))
    #start the connection with the closest server
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    client(0)
    
    
        
        
        