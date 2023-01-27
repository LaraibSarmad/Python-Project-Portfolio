name = input("Enter your full name:")

description = input ("Describe yourself:")

file = open('Personal.html', 'w')

file.readline()

my_file = open("Personal.txt","w")

html="<html>\n"+\

"<head>\n"+\

"</head>\n"+\

"<body>\n"+\

"<center>\n"+\

"<h1>"+name+"</h1>\n"+\

"</center>\n"+\

"<hr/>\n"+\

description+"\n"\

"<hr/>\n"+\

"</body>\n"+\

"</html>\n"



myfile = my_file.readline()



print(myfile)



file.write(html)



my_file.close

