from pcapfile import savefile
testcap = open('my_file.pcap', 'rb')
capfile = savefile.load_savefile(testcap, verbose=True)
data=[];
temp=""; 
row = 0;
column = 0;
for count, elem in enumerate(capfile.packets):
	#print "Packet number "+ str(count)+" capture_len is "+str(elem.capture_len)+"\r\n";
	temp_str = bytearray.fromhex(elem.packet)
	temp_str = temp_str[64:];
	for elem1 in temp_str:
		temp=temp+str(elem1)+":";
	data.append(temp);
	temp_length = elem.capture_len;
	#print "Data is " + temp_str[64:]
data[12]=data[12][:-1];
print(data[12])
dat=data[12].split(':');
#print [map(hex, l) for l in a]
dat = [int(x, 10) for x in dat];
print [map(hex, dat)]
