import re
from py_helper import *



index = 0;
def func0x10():
	print '3.3.1 Clock Data Bytes Out on +ve clock edge MSB first (no read)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x11():
	print '3.3.2 Clock Data Bytes Out on -ve clock edge MSB first (no read)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x12():
	print '3.3.3 Clock Data Bits Out on +ve clock edge MSB first (no read)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x13():
	print '3.3.4 Clock Data Bits Out on -ve clock edge MSB first (no read)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x20():
	print '3.3.5 Clock Data Bytes In on +ve clock edge MSB first (no write)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x24():
	print '3.3.6 Clock Data Bytes In on -ve clock edge MSB first (no write)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x22():
	print '3.3.7 Clock Data Bits In on +ve clock edge MSB first (no write)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x26():
	print '3.3.8 Clock Data Bits In on -ve clock edge MSB first (no write)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x31():
	print '3.3.9 Clock Data Bytes In and Out MSB first';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x33():
	print '3.3.10 Clock Data bits In and Out MSB first';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x18():
	print '3.4.1 Clock Data Bytes Out on +ve clock edge LSB first (no read)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x19():
	print '3.4.2 Clock Data Bytes Out on -ve clock edge LSB first (no read)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x1a():
	print '3.4.3 Clock Data Bits Out on +ve clock edge LSB first (no read)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x1b():
	print '3.4.4 Clock Data Bits Out on -ve clock edge LSB first (no read)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x28():
	print '3.4.5 Clock Data Bytes In on +ve clock edge LSB first (no write)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x2c():
	print '3.4.6 Clock Data Bytes In on -ve clock edge LSB first (no write)';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+length+inc_num
def func0x2a():
	print '3.4.7 Clock Data Bits In on +ve clock edge LSB first (no write)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x2e():
	print '3.4.8 Clock Data Bits In on -ve clock edge LSB first (no write)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x39():
	print '3.4.9 Clock Data Bytes In and Out LSB first';
	global index;
	length=dat[index]+dat[index+1]*256
	print 'Current index is '+str(index)+" length is "+str(length)
	index=index+length+inc_num
def func0x3b():
	print '3.4.10 Clock Data Bits In and Out LSB first';
	global index;
	length=dat[index]+dat[index+1]*256
	print 'Current index is '+str(index)+" length is "+str(length)
	index=index+2
def func0x4a():
	print '3.5.1 Clock Data to TMS pin (no read)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x4b():
	print '3.5.1 Clock Data to TMS pin (no read)';
	global index;
	length=dat[index]#+dat[index+1]*8
	index=index+2
def func0x6a():
	print '3.5.2 Clock Data to TMS pin with read';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+2
def func0x6b():
	print '3.5.2 Clock Data to TMS pin with read';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+2
def func0x6e():
	print '3.5.2 Clock Data to TMS pin with read';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+2
def func0x6f():
	print '3.5.2 Clock Data to TMS pin with read';
	global index;
	length=dat[index]+dat[index+1]*256
	index=index+2
def func0x80():
	global index;
	index=index+ 2;
	print '3.6.1 Set Data bits LowByte';
def func0x82():
	global index;
	index=index+ 2;
	print '3.6.2 Set Data bits High Byte';
def func0x81():
	global index;
	index=index+ 0;
	print '3.6.3 Read Data bits LowByte';
def func0x83():
	global index;
	index=index+ 0;
	print '3.6.4 Read Data bits HighByte';
def func0x84():
	global index;
	index=index+ 0;
	print '3.7.1 Connect TDI to TDO for Loopback';
def func0x85():
	global index;
	index=index+ 0;
	print '3.7.2 Disconnect TDI to TDO for Loopback';
def func0x86():
	global index;
	index=index+ 2;
	print '3.8.1 Set TCK/SK Divisor (FT2232D)';
def func0x87():
	global index;
	index=index+ 0;
	print 'Flush buffer';
def func0x88():
	global index;
	index=index+ 0;
	print 'Custom';
def func0x89():
	global index;
	index=index+ 0;
	print 'Custom';
def func0x8a():
	global index;
	index=index+ 0 ;
	print 'Disables the clk divide by 5 to allow for a 60MHz master clock. ';
def func0x8b():
	global index;
	index=index+ 0;
	print 'Enables the clk divide by 5 to allow for backward compatibility with FT2232D';
def func0x8c():
	global index;
	index=index+0 ;
	print 'Enables 3 phase data clocking. Used by I2C interfaces to allow data on both clock edges.';
def func0x8d():
	global index;
	index=index+0 ;
	print 'Disables 3 phase data clocking.';
def func0x8e():
	global index;
	index=index+1 ;
	print 'Allows for a clock to be output without transferring data. Commonly used in the JTAG state machine. Clocks counted in terms of numbers of bits';
def func0x8f():
	global index;
	length=dat[index]+dat[index+1]*256;
	index=index+length+inc_num;
	print 'Allows for a clock to be output without transferring data. Commonly used in the JTAG state machine. Clocks counted in terms of numbers of bytes';
def func0x94():
	global index;
	index=index+ 0;
	print 'Allows for a clock to be output without transferring datauntil a logic 1 input on GPIOL1stops the clock.';
def func0x95():
	global index;
	index=index+0 ;
	print 'Allows for a clock to be output without transferring datauntil a logic 0 input on GPIOL1stops the clock.';
def func0x96():
	global index;
	index=index+ 0;
	print 'Enable adaptive clocking';
def func0x97():
	global index;
	index=index+ 0;
	print 'Disable adaptive clocking';
def func0x9c():
	global index;
	length=dat[index]+dat[index+1]*256;
	index=index+length+inc_num;
	print 'Allows for a clock to be output without transferring data until a logic1 input on GPIOL1stops the clock or a set number of clock pulses are sent. Clocks counted in terms of numbers of bytes';
def func0x9d():
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
0x33 :func0x33,
0x18 :func0x18,
0x19 :func0x19,
0x1a :func0x1a,
0x1b :func0x1b,
0x28 :func0x28,
0x2c :func0x2c,
0x2a :func0x2a,
0x2e :func0x2e,
0x39 :func0x39,
0x3b :func0x3b,
0x4b :func0x4b,
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


