from q3_boy import boy 
from q3_gift import gift 

class geek(boy):
	
	def __init__ (self , name=None  , attractiveness = None ,  intelligence = None, budget= None ):
		super(Choosy , self).__init__()
		self.typee = geek
	''' this function is used to calculate happiness of geek boy type object ''' 
	def cal_happiness(self , gifts_array , happiness_girl , intelligence_girl  ): 
		happiness_boy = intelligence_girl 
		set_happiness(happiness_boy)
		return happiness_boy 
