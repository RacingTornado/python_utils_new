import re
from py_helper import *



index = 0;
count0x10=0;
count0x11=0;
count0x12=0;
count0x13=0;
count0x20=0;
count0x24=0;
count0x22=0;
count0x26=0;
count0x31=0;
count0x34=0;
count0x33=0;
count0x36=0;
count0x18=0;
count0x19=0;
count0x1a=0;
count0x1b=0;
count0x28=0;
count0x2c=0;
count0x2a=0;
count0x2e=0;
count0x39=0;
count0x3c=0;
count0x3b=0;
count0x3e=0;
count0x4a=0;
count0x4b=0;
count0x6a=0;
count0x6b=0;
count0x6e=0;
count0x6f=0;
count0x80=0;
count0x82=0;
count0x81=0;
count0x83=0;
count0x84=0;
count0x85=0;
count0x86=0;
count0x87=0;
count0x88=0;
count0x89=0;
count0x8a=0;
count0x8b=0;
count0x8c=0;
count0x8d=0;
count0x8e=0;
count0x8f=0;
count0x94=0;
count0x95=0;
count0x96=0;
count0x97=0;
count0x9c=0;
count0x9d=0;
def func0x10():
	global count0x10;
	count0x10+=1;
	print '3.3.1 Clock Data Bytes Out on +ve clock edge MSB first (no read)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x11():
	global count0x11;
	count0x11+=1;
	print '3.3.2 Clock Data Bytes Out on -ve clock edge MSB first (no read)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x12():
	global count0x12;
	count0x12+=1;
	print '3.3.3 Clock Data Bits Out on +ve clock edge MSB first (no read)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x13():
	global count0x13;
	count0x13+=1;
	print '3.3.4 Clock Data Bits Out on -ve clock edge MSB first (no read)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x20():
	global count0x20;
	count0x20+=1;
	print '3.3.5 Clock Data Bytes In on +ve clock edge MSB first (no write)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x24():
	global count0x24;
	count0x24+=1;
	print '3.3.6 Clock Data Bytes In on -ve clock edge MSB first (no write)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x22():
	global count0x22;
	count0x22+=1;
	print '3.3.7 Clock Data Bits In on +ve clock edge MSB first (no write)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x26():
	global count0x26;
	count0x26+=1;
	print '3.3.8 Clock Data Bits In on -ve clock edge MSB first (no write)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x31():
	global count0x31;
	count0x31+=1;
	print '3.3.9 Clock Data Bytes In and Out MSB first,edged';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x34():
	global count0x34;
	count0x34+=1;
	print '3.3.9 Clock Data Bytes In and Out MSB first,edged';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x33():
	global count0x33;
	count0x33+=1;
	print '3.3.10 Clock Data bits In and Out MSB first';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x36():
	global count0x36;
	count0x36+=1;
	print '3.3.10 Clock Data bits In and Out MSB first,edged';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x18():
	global count0x18;
	count0x18+=1;
	print '3.4.1 Clock Data Bytes Out on +ve clock edge LSB first (no read)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x19():
	global count0x19;
	count0x19+=1;
	print '3.4.2 Clock Data Bytes Out on -ve clock edge LSB first (no read)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x1a():
	global count0x1a;
	count0x1a+=1;
	print '3.4.3 Clock Data Bits Out on +ve clock edge LSB first (no read)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x1b():
	global count0x1b;
	count0x1b+=1;
	print '3.4.4 Clock Data Bits Out on -ve clock edge LSB first (no read)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x28():
	global count0x28;
	count0x28+=1;
	print '3.4.5 Clock Data Bytes In on +ve clock edge LSB first (no write)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x2c():
	global count0x2c;
	count0x2c+=1;
	print '3.4.6 Clock Data Bytes In on -ve clock edge LSB first (no write)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x2a():
	global count0x2a;
	count0x2a+=1;
	print '3.4.7 Clock Data Bits In on +ve clock edge LSB first (no write)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x2e():
	global count0x2e;
	count0x2e+=1;
	print '3.4.8 Clock Data Bits In on -ve clock edge LSB first (no write)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x39():
	global count0x39;
	count0x39+=1;
	print '3.4.9 Clock Data Bytes In and Out LSB first,edged';
	global index;
	length=dat[index]+dat[index+1]*256
	print 'Current index is '+str(index)+" length is "+str(length)
	index=index+length+inc_num
def func0x3c():
	global count0x3c;
	count0x3c+=1;
	print '3.4.9 Clock Data Bytes In and Out LSB first,edged';
	global index;
	length=dat[index]+dat[index+1]*256
	print 'Current index is '+str(index)+" length is "+str(length)
	index=index+length+inc_num
def func0x3b():
	global count0x3b;
	count0x3b+=1;
	print '3.4.10 Clock Data Bits In and Out LSB first,edged';
	global index;
	length=dat[index]+dat[index+1]*256
	print 'Current index is '+str(index)+" length is "+str(length)
	index=index+2
def func0x3e():
	global count0x3e;
	count0x3e+=1;
	print '3.4.10 Clock Data Bits In and Out LSB first,edged';
	global index;
	length=dat[index]+dat[index+1]*256
	print 'Current index is '+str(index)+" length is "+str(length)
	index=index+2
def func0x4a():
	global count0x4a;
	count0x4a+=1;
	print '3.5.1 Clock Data to TMS pin (no read)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x4b():
	global count0x4b;
	count0x4b+=1;
	print '3.5.1 Clock Data to TMS pin (no read)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x6a():
	global count0x6a;
	count0x6a+=1;
	print '3.5.2 Clock Data to TMS pin with read';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+2
def func0x6b():
	global count0x6b;
	count0x6b+=1;
	print '3.5.2 Clock Data to TMS pin with read';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+2
def func0x6e():
	global count0x6e;
	count0x6e+=1;
	print '3.5.2 Clock Data to TMS pin with read';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+2
def func0x6f():
	global count0x6f;
	count0x6f+=1;
	print '3.5.2 Clock Data to TMS pin with read';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+2
def func0x80():
	global count0x80;
	count0x80+=1;
	global index;
	index=index+ 2;
	print '3.6.1 Set Data bits LowByte';
def func0x82():
	global count0x82;
	count0x82+=1;
	global index;
	index=index+ 2;
	print '3.6.2 Set Data bits High Byte';
def func0x81():
	global count0x81;
	count0x81+=1;
	global index;
	index=index+ 0;
	print '3.6.3 Read Data bits LowByte';
def func0x83():
	global count0x83;
	count0x83+=1;
	global index;
	index=index+ 0;
	print '3.6.4 Read Data bits HighByte';
def func0x84():
	global count0x84;
	count0x84+=1;
	global index;
	index=index+ 0;
	print '3.7.1 Connect TDI to TDO for Loopback';
def func0x85():
	global count0x85;
	count0x85+=1;
	global index;
	index=index+ 0;
	print '3.7.2 Disconnect TDI to TDO for Loopback';
def func0x86():
	global count0x86;
	count0x86+=1;
	global index;
	index=index+ 2;
	print '3.8.1 Set TCK/SK Divisor (FT2232D)';
def func0x87():
	global count0x87;
	count0x87+=1;
	global index;
	index=index+ 0;
	print 'Flush buffer';
def func0x88():
	global count0x88;
	count0x88+=1;
	global index;
	index=index+ 0;
	print 'Custom';
def func0x89():
	global count0x89;
	count0x89+=1;
	global index;
	index=index+ 0;
	print 'Custom';
def func0x8a():
	global count0x8a;
	count0x8a+=1;
	global index;
	index=index+ 0 ;
	print 'Disables the clk divide by 5 to allow for a 60MHz master clock. ';
def func0x8b():
	global count0x8b;
	count0x8b+=1;
	global index;
	index=index+ 0;
	print 'Enables the clk divide by 5 to allow for backward compatibility with FT2232D';
def func0x8c():
	global count0x8c;
	count0x8c+=1;
	global index;
	index=index+0 ;
	print 'Enables 3 phase data clocking. Used by I2C interfaces to allow data on both clock edges.';
def func0x8d():
	global count0x8d;
	count0x8d+=1;
	global index;
	index=index+0 ;
	print 'Disables 3 phase data clocking.';
def func0x8e():
	global count0x8e;
	count0x8e+=1;
	global index;
	index=index+1 ;
	print 'Allows for a clock to be output without transferring data. Commonly used in the JTAG state machine. Clocks counted in terms of numbers of bits';
def func0x8f():
	global count0x8f;
	count0x8f+=1;
	global index;
	length=dat[index]+dat[index+1]*256;
	index=index+length+inc_num;
	print 'Allows for a clock to be output without transferring data. Commonly used in the JTAG state machine. Clocks counted in terms of numbers of bytes';
def func0x94():
	global count0x94;
	count0x94+=1;
	global index;
	index=index+ 0;
	print 'Allows for a clock to be output without transferring datauntil a logic 1 input on GPIOL1stops the clock.';
def func0x95():
	global count0x95;
	count0x95+=1;
	global index;
	index=index+0 ;
	print 'Allows for a clock to be output without transferring datauntil a logic 0 input on GPIOL1stops the clock.';
def func0x96():
	global count0x96;
	count0x96+=1;
	global index;
	index=index+ 0;
	print 'Enable adaptive clocking';
def func0x97():
	global count0x97;
	count0x97+=1;
	global index;
	index=index+ 0;
	print 'Disable adaptive clocking';
def func0x9c():
	global count0x9c;
	count0x9c+=1;
	global index;
	length=dat[index]+dat[index+1]*256;
	index=index+length+inc_num;
	print 'Allows for a clock to be output without transferring data until a logic1 input on GPIOL1stops the clock or a set number of clock pulses are sent. Clocks counted in terms of numbers of bytes';
def func0x9d():
	global count0x9d;
	count0x9d+=1;
	global index;
	length=dat[index]+dat[index+1]*256;
	index=index+length+inc_num;
	print 'Allows for a clock to be output without transferring datauntil a logic 0 input on GPIOL1stops the clock or a set number of clock pulses are sent. Clocks counted in terms of numbers of bytes';

inc_num = 3;


options={0x10 :func0x10,
0x11 :func0x11,
0x12 :func0x12,
0x13 :func0x13,
0x20 :func0x20,
0x24 :func0x24,
0x22 :func0x22,
0x26 :func0x26,
0x31 :func0x31,
0x34 :func0x34,
0x33 :func0x33,
0x36 :func0x36,
0x18 :func0x18,
0x19 :func0x19,
0x1a :func0x1a,
0x1b :func0x1b,
0x28 :func0x28,
0x2c :func0x2c,
0x2a :func0x2a,
0x2e :func0x2e,
0x39 :func0x39,
0x3c :func0x3c,
0x3b :func0x3b,
0x3e :func0x3e,
0x4a :func0x4b,
0x4b :func0x4b,
0x6a :func0x6a,
0x6b :func0x6b,
0x6e :func0x6e,
0x6f :func0x6f,
0x80 :func0x80,
0x82 :func0x82,
0x81 :func0x81,
0x83 :func0x83,
0x84 :func0x84,
0x85 :func0x85,
0x86 :func0x86,
0x87 :func0x87,
0x88 :func0x88,
0x89 :func0x89,
0x8a :func0x8a,
0x8b :func0x8b,
0x8c :func0x8c,
0x8d :func0x8d,
0x8e :func0x8e,
0x8f :func0x8f,
0x94 :func0x94,
0x95 :func0x95,
0x96 :func0x96,
0x97 :func0x97,
0x9c :func0x9c,
0x9d :func0x9d
};
#options[0x10]();

while index < len(dat):
	curr_command = dat[index];
	print("Index is "+ str(index)+" command is ", hex(curr_command))
	index += 1
	options[(curr_command)]();
	print '\r\n'

print 'Count is 0x10 ' + str(count0x10);
print 'Count is 0x11 ' + str(count0x11);
print 'Count is 0x12 ' + str(count0x12);
print 'Count is 0x13 ' + str(count0x13);
print 'Count is 0x20 ' + str(count0x20);
print 'Count is 0x24 ' + str(count0x24);
print 'Count is 0x22 ' + str(count0x22);
print 'Count is 0x26 ' + str(count0x26);
print 'Count is 0x31 ' + str(count0x31);
print 'Count is 0x34 ' + str(count0x34);
print 'Count is 0x33 ' + str(count0x33);
print 'Count is 0x36 ' + str(count0x36);
print 'Count is 0x18 ' + str(count0x18);
print 'Count is 0x19 ' + str(count0x19);
print 'Count is 0x1a ' + str(count0x1a);
print 'Count is 0x1b ' + str(count0x1b);
print 'Count is 0x28 ' + str(count0x28);
print 'Count is 0x2c ' + str(count0x2c);
print 'Count is 0x2a ' + str(count0x2a);
print 'Count is 0x2e ' + str(count0x2e);
print 'Count is 0x39 ' + str(count0x39);
print 'Count is 0x3c ' + str(count0x3c);
print 'Count is 0x3b ' + str(count0x3b);
print 'Count is 0x3e ' + str(count0x3e);
print 'Count is 0x4a ' + str(count0x4a);
print 'Count is 0x4b ' + str(count0x4b);
print 'Count is 0x6a ' + str(count0x6a);
print 'Count is 0x6b ' + str(count0x6b);
print 'Count is 0x6e ' + str(count0x6e);
print 'Count is 0x6f ' + str(count0x6f);
print 'Count is 0x80 ' + str(count0x80);
print 'Count is 0x82 ' + str(count0x82);
print 'Count is 0x81 ' + str(count0x81);
print 'Count is 0x83 ' + str(count0x83);
print 'Count is 0x84 ' + str(count0x84);
print 'Count is 0x85 ' + str(count0x85);
print 'Count is 0x86 ' + str(count0x86);
print 'Count is 0x87 ' + str(count0x87);
print 'Count is 0x88 ' + str(count0x88);
print 'Count is 0x89 ' + str(count0x89);
print 'Count is 0x8a ' + str(count0x8a);
print 'Count is 0x8b ' + str(count0x8b);
print 'Count is 0x8c ' + str(count0x8c);
print 'Count is 0x8d ' + str(count0x8d);
print 'Count is 0x8e ' + str(count0x8e);
print 'Count is 0x8f ' + str(count0x8f);
print 'Count is 0x94 ' + str(count0x94);
print 'Count is 0x95 ' + str(count0x95);
print 'Count is 0x96 ' + str(count0x96);
print 'Count is 0x97 ' + str(count0x97);
print 'Count is 0x9c ' + str(count0x9c);
print 'Count is 0x9d ' + str(count0x9d);
