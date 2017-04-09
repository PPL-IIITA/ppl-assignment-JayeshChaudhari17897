
from abc import ABCMeta , abstractmethod 
from q3_gift import gift 


'''this class is the parent boy class from here other three classes have been inherited'''
class boy(object):
	__metaclass__ = ABCMeta 
	
	def __init__(self , name = None , attractiveness = None , intelligence = None , budget = None): 
		# this  is a  constructor for Boy class.
		self.name = name 
		self.attractiveness = attractiveness 
		self.budget = budget 
		self.intelligence = intelligence 
		self.committed = False 
		self.happiness = 0.0 
	''' this abstract method s used to calculate happiness , which will be made concrete in the calling class '''
	@abstractmethod
	def cal_happiness(self , gifts_Array  , happiness_of_girl , intelligence_girl ): 
		pass


