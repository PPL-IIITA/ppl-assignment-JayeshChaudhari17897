from q1_boy import Boy 
from q1_girl import Girl 

class Couple(object) :
	def __init__ (self , boy_object , girl_object ):
		self.boy = boy_object
		self.girl = girl_object
		self.id = self.boy.name+"  is committed with    "+self.girl.name

