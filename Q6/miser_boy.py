from q3_boy import boy 
from q3_gift import gift 

class miser(boy):
	
	def __init__ (self , name=None  , attractiveness = None ,  intelligence = None, budget= None ): 
		super(miser, self).__init__()
		self.typee = miser

	'''this function will calculate happiness for miser boy object '''
	def cal_happiness( gifts_array , happiness_girl , intelligence_girl):
		x = 0 
		k = len(gifts_array)
		for j in range(k):
			x  =  x + gifts_array[i].get_cost()

		happiness_boy = abs(get_budget() - x )
		set_happiness(happiness_boy)

		return happiness_boy
