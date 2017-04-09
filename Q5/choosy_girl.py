from q3_girl import girl 
from q3_gift import gift 

class choosy(girl):
	
	def __init__ (self , name=None  , attractiveness = None ,  intelligence = None, budget= None ): 
		super(choosy , self).__init__()
		self.typee = choosy

	''' this fucnction will calculate happpiness for choosy girl object '''
		

	def cal_happiness (self , gifts_array): 
		x = 0.0
		y = 0.0
		for j in range (len(gifts_array)) :
			x = x + gifts_array[j].get_cost()
			y = y + gifts_array[j].get_value()

		happiness_girl = 0.0
		happiness_girl = happiness_girl + abs( log ( x - get_budget() + 2*y ) )
		set_happiness(happiness_girl)
		return happiness_girl

