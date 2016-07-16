def function_formatter():
	f = open('/home/itsy/python_parse_new/function_holder1.txt','r');
	f1 = open('/home/itsy/python_parse_new/enum.txt','r');
	target = open('/home/itsy/python_parse_new/enum.c', 'w');
	target.truncate();
	text = f.readline();
	text1 = f1.readline();
	while text:	
		text1 = text1.split('=');
		target.write("/* "+text.replace("	print ","",1)+"*/\r\n");
		target.write("void func_"+text1[0].replace(" ", "")+"()\r\n{\r\n}\r\n");
		text = f.readline();
		text1=f1.readline();
	f1.close();
	f.close();
	target.close();
	



function_formatter();
