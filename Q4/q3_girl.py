from q3_gift import gift 
from abc import ABCMeta , abstractmethod 

class girl(object):
	_metaclass_ = ABCMeta 
	
	def __init__(self , name = None , attractiveness = None , intelligence = None , budget = None):

		self.name = name 
		self.attractiveness = attractiveness 
		self.maintenance = budget 
		self.intelligence = intelligence 
		self.committed = False 
		self.happiness = 0.0 
	'''this abstract  function is used to calculate happiness , will be made concrete in the calling class ''' 
	@abstractmethod
	def cal_happiness(self , gifts_Array   ):
		pass



