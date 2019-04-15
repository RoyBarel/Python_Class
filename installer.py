#!/usr/bin/env ptrhon3.6

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
	os.system('sudo pip3.6 install pymysql')
except Exception as e:
	print(e)
	sys.exit(1)	

#installing Perl
os.system('sudo yum -y install perl perl-CGI')    

#installing PHP
os.system('sudo yum -y install php php-mbstring php-pear ') 


#Functions /\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\



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
		#os.system('cp /etc/httpd/conf/httpd.conf ~/')
		with open('/etc/httpd/conf/httpd.conf','r') as web:
			httpd_file_data = web.readlines()
			#print(httpd_file_data)
	
		search_term = "^ServerAdmin root@localhost"
		new_data = 'ServerAdmin roy@localhost'
		time.sleep(1)
		for line in httpd_file_data:
			#print(line)
			if re.findall(search_term, line):
				print(line)
				time.sleep(1)
				line = new_data
				#print(line)
		with open('/etc/httpd/conf/httpd.conf','r') as f:
			
			print(str(httpd_file_data))
			f.write(str(httpd_file_data))
			#	if line == None:
			#		print('no matches found')
		
	
	
	except Exception as e:
		print(e)
		sys.exit(1)

	
