gnome-terminal --tab -e "python central.py -p 10000"
gnome-terminal --tab -e "python central.py -p 10001"
gnome-terminal --tab -e "python central.py -p 10002"
sleep 3
for i in {11000..11010}
do
	gnome-terminal --tab -e "python server.py -p $i"
done

#After establishing the servers, call clients with script client.py
