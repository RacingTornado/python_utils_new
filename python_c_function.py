def function_formatter():
	f = open('/home/itsy/python_parse_new/function_holder1.txt','r');
	f1 = open('/home/itsy/python_parse_new/enum.txt','r');
	target = open('/home/itsy/python_parse_new/enum.c', 'w');
	target.truncate();
	target1 = open('/home/itsy/python_parse_new/enum1.c', 'w');
	target1.truncate();
	target2 = open('/home/itsy/python_parse_new/enum2.c', 'w');
	target2.truncate();
	text = f.readline();
	text1 = f1.readline();
	while text:	
		text1 = text1.split('=');
		target.write("/* "+text.replace("	print ","",1)+"*/\r\n");
		target1.write("/**\r\n*\\brief "+text.replace("	print ","",1)+"**/\r\n");
		target.write("void func_"+text1[0].replace(" ", "")+"()\r\n{\r\n");
		target1.write("void func_"+text1[0].replace(" ", "")+"();\r\n");
		target2.write("case "+text1[0].replace(" ", "")+":\r\n");
		target2.write("	func_"+text1[0].replace(" ", "")+"();\r\n");
		target2.write("	break;\r\n");
		text=text.replace("	print ","",1);
		text=text.replace("'","");
		text=text.replace("\n","");
		target.write('printf("'+text+'\\r\\n");\r\n');
		target.write("}\r\n");
		text = f.readline();
		text1=f1.readline();
	f1.close();
	f.close();
	target.close();
	target1.close();
	target2.close();
	



function_formatter();
