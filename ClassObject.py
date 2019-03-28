class Person:
	"""
	Doc String that descrives the car class
	"""
	
	def __init__(self,name='NAME',last_name='LAST NAME',age='AGE',height=0.0,weight=0.0,id_num='0'):
		"""
		Doc String that explains init functoin of car class
		"""
		self.name=name
		self.last_name=last_name
		self.age=age
		self.height=height
		self.weight=weight
		self.id_num=id_num
#		pass placeHolder
		
	def sleep(time=-1):
		if (time!=-1):
			print (time)
		else:
			print ("You didnt Enter Time!")
	
	def eat():
		how_much=input("How much do you want to eat")
	def work():
		print("I'll back to you soon")
	def walk(time):
		print(f"you walk for{time} min")
	def wake():
		print ("still want to sleep")


Alex = Person

Alex.sleep(2)
Alex.work()
Alex.walk(1)
Alex.wake()
