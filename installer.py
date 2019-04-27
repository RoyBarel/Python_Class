#!/usr/bin/env python3.6

#########################################################
#created by RoyBarel
#Purpose : finelWork - installer
#Date    : 15/4/2019
#Version : 1
#########################################################

#import libs =========================================================

import os
import sys
import time
import re


#installing mysql
os.system('sudo yum install mysql-server')
try :
	import pymysql 
except ModuleNotFoundError:
	os.system('sudo pip3.6 ins#!/usr/bin/env python3.6

#########################################################
#created by RoyBarel
#Purpose : finelWork - installer
#Date    : 27/4/2019
#Version : 1
#########################################################

#import libs =========================================================

import os
import sys
import time
import re


#installing mysql
os.system('sudo yum install mysql-server')
try :
	import pymysql 
except ModuleNotFoundError:
	os.system('sudo pip3.6 install pymysql')
except Exception as e:
	print(e)
	sys.exit(1)	

#installing Perl
os.system('sudo yum -y install perl perl-CGI')    

#installing PHP
os.system('sudo yum -y install php php-mbstring php-pear ') 


#Functions /\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\

def changingFiles (input_file, in_search_term , in_new_data , start_line_search=0):
	
	try:
		search_term = in_search_term+"\n"
		new_data = in_new_data+"\n"

		try:
			index = lines.index(search_term , start_line_search)
			lines[index] = new_data
			f = open(input_file,'w')
			f.writelines(lines)
			f.close()
						
		except ValueError:
			print("Not find the term")
	except FileNotFoundError:
		print("Not find the file, check the Path of the file")
	except PermissionError:
		print("You don't have permission to get this file")
	except Exception as e:
		print(e)
		sys.exit(1)


def addingToTheLast (input_file , in_new_data ):
	
	try:
		with open(input_file) as f1: # open the file 
				lines = f1.readlines() # Copy the file to lists
		new_data = in_new_data+"\n"
		f = open(input_file,'w')
		f.writelines(lines)
		f.write(new_data)
		f.close()
		
	except FileNotFoundError:
		print("Not find the file, check the Path of the file")
	except PermissionError:
		print("You don't have permission to get this file")
	except Exception as e:
		print(e)
		sys.exit(1)
	

###
#Main - _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _
###

if __name__ == '__main__':
	
	#creating directory for each language
	os.system('sudo mkdir /var/www/html/')# for html
	#os.system('sudo mkdir /var/www/python/index.py/')# for python
	os.system('sudo mkdir /var/www/cgi-bin')# for perl
	
	try :
		#Install httpd
		os.system('sudo yum -y install httpd')
		os.system('sudo rm -f /etc/httpd/conf.d/welcome.conf') 
		
			
		#Configure httpd
		## Copy the file httpd.conf to tmp file
		
		with open('/etc/httpd/conf/httpd.conf') as f1: # open the file 
				lines = f1.readlines() # Copy the file to lists
		tmpFileHttpd = '/tmp/tmpHttpd1.conf'
		f = open(tmpFileHttpd,'w')
		f.writelines(lines)
		f.close()
		
		
		changingFiles(tmpFileHttpd, "ServerAdmin root@localhost" , 'ServerAdmin roy@localhost')
		
		print("The admin's email address is: roy@localhost")
		
		changingFiles(tmpFileHttpd, "#ServerName www.example.com:80" , "ServerName 127.0.0.1:80" )
		
		print("The ServerName is: 127.0.0.1:80")
		
		changingFiles(tmpFileHttpd, "    AllowOverride None" , "    AllowOverride All" , 150)
		
		changingFiles( tmpFileHttpd, "    DirectoryIndex index.html" , "    DirectoryIndex index.html index.php index.perl index.py" , 160)
				
		addingToTheLast(tmpFileHttpd , "ServerTokens Prod" )
				
		addingToTheLast(tmpFileHttpd , "KeepAlive On" )
	
		#return the file to his place
		os.system(f'sudo mv {tmpFileHttpd} /etc/httpd/conf/httpd.conf')
				
		os.system('sudo systemctl start httpd')
		os.system('sudo systemctl enable httpd')
		
		#If Firewalld is running, allow HTTP service. HTTP uses 80/TCP. 
		os.system('sudo firewall-cmd --add-service=http --permanent')           
		os.system('sudo firewall-cmd --reload')
		
		
		#Create HTML page
		tmpFileHtml='/tmp/tmphtmpl.index'
		in_new_data = '<html>\n<body>\n<div style="width: 100%; font-size: 40px; font-weight: bold; text-align: center;">\nHello from html\n</div>\n</body>\n</html>\n'
		f = open(tmpFileHtml,'w')
		f.write(in_new_data)
		f.close()
		os.system(f'sudo mv {tmpFileHtml} /var/www/html/index.html')
		
		#Create php page
		tmpFilephp='/tmp/tmpphp.index'
		in_new_data = '<html>\n<body>\n<div style="width: 100%; font-size: 40px; font-weight: bold; text-align: center;">\n<?php\n echo "Hello from php<br>";\n?>\n</div>\n</body>\n</html>\n'
		f = open(tmpFilephp,'w')
		f.write(in_new_data)
		f.close()
		os.system(f'sudo mv {tmpFilephp} /var/www/html/index.php')
		
		#Create Perl page
		tmpFileperl='/tmp/tmpperl.index'
		in_new_data = '#!/usr/bin/perl\nprint "Hello from perl;"'
		f = open(tmpFileperl,'w')
		f.write(in_new_data)
		f.close()		
		os.system(f'sudo mv {tmpFileperl} /var/www/cgi-bin/index.perl')
		os.system(f'sudo chmod 705 /var/www/cgi-bin/index.perl')
		
		#Create Python page
		tmpFilepython='/tmp/tmppython.index'
		in_new_data = '#!/usr/bin/python\nprint(Hello from python)\n'
		f = open(tmpFilepython,'w')
		f.write(in_new_data)
		f.close()		
		os.system(f'sudo mv {tmpFilepython} /var/www/cgi-bin/index.python')
		os.system(f'sudo chmod 705 /var/www/cgi-bin/index.python')
		
		
		
	except Exception as e:
		print(e)
		sys.exit(1)
	
		#https://www.server-world.info/en/note?os=CentOS_7&p=httpd&f=1
tall pymysql')
except Exception as e:
	print(e)
	sys.exit(1)	

#installing Perl
os.system('sudo yum -y install perl perl-CGI')    

#installing PHP
os.system('sudo yum -y install php php-mbstring php-pear ') 


#Functions /\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\

def changingFiles (input_file, in_search_term , in_new_data , start_line_search=0):
	
	try:
		search_term = in_search_term+"\n"
		new_data = in_new_data+"\n"

		try:
			index = lines.index(search_term , start_line_search)
			lines[index] = new_data
			f = open(input_file,'w')
			f.writelines(lines)
			f.close()
						
		except ValueError:
			print("Not find the term")
	except FileNotFoundError:
		print("Not find the file, check the Path of the file")
	except PermissionError:
		print("You don't have permission to get this file")
	except Exception as e:
		print(e)
		sys.exit(1)


def addingToTheLast (input_file , in_new_data ):
	
	try:
		with open(input_file) as f1: # open the file 
				lines = f1.readlines() # Copy the file to lists
		new_data = in_new_data+"\n"
		f = open(input_file,'w')
		f.writelines(lines)
		f.write(new_data)
		f.close()
		
	except FileNotFoundError:
		print("Not find the file, check the Path of the file")
	except PermissionError:
		print("You don't have permission to get this file")
	except Exception as e:
		print(e)
		sys.exit(1)
	

###
#Main - _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _
###

if __name__ == '__main__':
	
	#creating directory for each language
	os.system('sudo mkdir /var/www/html/cgi-enabled/')
	os.system('sudo mkdir /var/www/html/php/')
	
	try :
		#Install httpd
		os.system('sudo yum -y install httpd')
		os.system('sudo rm -f /etc/httpd/conf.d/welcome.conf') 
		
			
		#Configure httpd
		## Copy the file httpd.conf to tmp file
		
		with open('/etc/httpd/conf/httpd.conf') as f1: # open the file 
				lines = f1.readlines() # Copy the file to lists
		tmpFileHttpd = '/tmp/tmpHttpd1.conf'
		f = open(tmpFileHttpd,'w')
		f.writelines(lines)
		f.close()
		
		
		changingFiles(tmpFileHttpd, "ServerAdmin root@localhost" , 'ServerAdmin roy@localhost')
		
		print("The admin's email address is: roy@localhost")
		
		changingFiles(tmpFileHttpd, "#ServerName www.example.com:80" , "ServerName 127.0.0.1:80" )
		
		print("The ServerName is: 127.0.0.1:80")
		
		changingFiles(tmpFileHttpd, "    AllowOverride None" , "    AllowOverride All" , 150)
		
		changingFiles( tmpFileHttpd, "    DirectoryIndex index.html" , "    DirectoryIndex index.html index.php index.perl index.py" , 160)
				
		addingToTheLast(tmpFileHttpd , "ServerTokens Prod" )
				
		addingToTheLast(tmpFileHttpd , "KeepAlive On" )
	
		#return the file to the origain place
		os.system(f'sudo mv {tmpFileHttpd} /etc/httpd/conf/httpd.conf')
		
		
	except Exception as e:
		print(e)
		sys.exit(1)
	
		
