from q3_boy import boy 
from q3_gift import gift 

class generous(boy):
	
	def __init__ (self , name=None  , attractiveness = None ,  intelligence = None, budget= None ): 
		super(generous, self).__init__()
		self.typee = generous
	''' this function is used to calculate happiness for generous object type'''
	def cal_happiness( self , gifts_array , happiness_girl , intellligence_girl): 
		happiness_boy = happiness_girl 
		set_happiness(happiness_boy)
		return 0
