f = open('/home/itsy/python_parse_new/case1.txt','r');
target = open('/home/itsy/python_parse_new/caser.py', 'w');
target.truncate();
text = f.readline();
pri=[];
pri1=[];
while text:
	if '():' in text:
		target.write(text);
		temp_text=text[-8:];
		temp_text=temp_text[:-4];
		target.write("	global count"+temp_text+";\r\n");
		pri.append("print 'Count is "+temp_text+ " ' + str(count"+temp_text+");\r\n");
		pri1.append("count"+temp_text+"=0;\r\n");
		target.write("	count"+temp_text+"+=1;\r\n");
	else:
		target.write(text);
	text=f.readline();
for elem in pri:
	target.write(elem);
for elem in pri1:
	target.write(elem);
f.close();
target.close();
	
