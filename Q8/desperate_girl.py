from q3_girl import girl 
from q3_gift import gift 

class desperate(girl):
	
	def __init__ (self , name=None  , attractiveness = None ,  intelligence = None, budget= None ):  
		super(Choosy , self ).__init__()
		self.typee = desperate

	''' this function will calculate happiness for desperate girl object '''	
	def cal_happiness(self , gifts_array):
		x = 0 
		y = 0 
		for j in range (len(gifts_array)):
			x = x + gifts_array[i].get_cost()
			y = y + gifts_array[i].get_value()

		happiness_girl = 0 
		r = x - get_budget()

		happiness_girl = happiness_girl + abs(2.73 ** r )
		set_happiness(happiness_girl)

		return happiness_girl 
