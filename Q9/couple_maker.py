from q3_boy import boy
from q3_girl import girl
from q3_gift import gift


class couple(object):
	

	def __init__(self , boy_b ,girl_g ):
		self.id = boy_b.name+ "&&" + girl_g.name
		self.boy = boy_b
		self.girl = girl_g
		self.happiness  = 0
		self.fitting= 0
		self.array_gift = []

	
