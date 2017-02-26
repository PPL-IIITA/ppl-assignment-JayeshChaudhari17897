from q2_boy import Boy
from q2_girl import Girl
from q2_gift import Gift


class Couple(object):
	def __init__(self , boy_object , girl_object ):
		self.boy = boy_object
		self.girl = girl_object 
		self.id = self.boy.name+" is committed with "+self.girl.name
		self.array_gift=[]
		self.happiness = 0
		self.fitting = 0