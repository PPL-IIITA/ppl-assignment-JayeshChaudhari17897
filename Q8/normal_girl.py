from q3_girl import girl 
from q3_gift import gift 

class normal(girl):

	
	def __init__ (self , name=None  , attractiveness = None ,  intelligence = None, budget= None ): 
		super(Choosy , self).__init__()
		self.typee = normal 

		

	def cal_happiness(self , gifts_array):
		x = 0 
		y = 0 
		for j in range (gifts_array.size()) :
			x = x + gifts_array[i].get_cost()
			y = y + gifts_array[i].get_value()
		happiness_girl = 0 
		happiness_girl = happiness_girl + x + y - get_budget()
		set_happiness(happiness_girl)
		return happiness_girl
