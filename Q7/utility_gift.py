from q3_gift import gift 
''' this is utility gift's class ''' 
class utility(gift):
	
	def __init__ (self , utility_value =None , utility_class =None, cost = None, value = None , gift_name  = None):
		super(utility, self ).__init__()
		self.utility_class = utility_class 
		self.utility_value = utility_value
