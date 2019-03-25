#!/usr/bin/env python3.6


DC_Heros = open('DC_Heros.txt','w')
hero=''
heros=[]


while(True):
	hero=input('Enter New Hero:    (use 0 to exit)')
	if(hero != "0"):
		DC_Heros.write(hero +"\n")
		heros.append(hero)
	else:
		break


DC_Heros.close()
