import socket
import time
import sys
import getopt

servers={}
def server(por):
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
    print ("socket binded to {}".format(por))
    
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
        c.send(b'You are connected to the port {}'.format(por)) 
        #This message is recieved to telle wether the sender is a server or a client
        typ=c.recv(1024)
        if typ==b'server':
           servers.update(eval(c.recv(1024)))
           print(servers)
        elif typ==b'client':
            c.sendall(b'{}'.format(servers))
        
        # Close the connection with the client 
        c.close() 
        
if __name__=='__main__':
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, 'p')
    except getopt.GetoptError:
        #Print a message or do something useful
        print('Something went wrong!')
        sys.exit(2)
    try:
        port = int(args[0])
    except:
        print("The port value is not an integer")
        sys.exit()
    #start the server
    server(port)