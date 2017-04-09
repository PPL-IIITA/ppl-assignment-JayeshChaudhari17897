from abc import ABCMeta , abstractmethod 

class gift(object):
	__metaclass__= ABCMeta
	
	def __init__ ( self , cost = None , value = None , gift_name = None):
		self.gift_cost = cost 
		self.gift_value = value 
		self.gift_type= gift_name 



