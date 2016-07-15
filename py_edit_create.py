import re
regexp = re.compile(r'3.[3|4|5|6|7|8].[\d]')

def find_command():
	global f;
	while True:
		temp = f.readline();
		if('0x' in temp) :
			target.write(temp[:-2]+",");
			for i in range(2):
				temp = f.readline();
				if( 'LengthL' in temp ):
					target.write(str(2));
					break;
				else:
					target.write(str(1));
					break;
			break;
		else:
			continue;
	return

f = open('/home/itsy/Downloads/an1081.txt','r');
target = open('/home/itsy/Downloads/an1082_formatted.txt', 'w');
target.truncate();
text=f.readline();
count = 0;
target.write("data"+str(count)+"=[");
while text:
	prev_line = text;
	text = f.readline();
	if regexp.search(text) is not None:
		print text	
		target.write("[" +"'"+text[:-1]+"',");
		find_command();
		target.write("],\r\n");
		count+=1;
f.close();
target.close();
