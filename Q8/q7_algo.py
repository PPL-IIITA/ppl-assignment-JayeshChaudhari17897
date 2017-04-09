from abc import ABCMeta , abstractmethod 
from q3_girl import girl
from couple_maker import couple 
from q3_boy import boy 
from q3_gift import gift
import csv 
import math
from generous_boy import generous
from miser_boy import miser
from geek_boy import geek
from normal_girl import normal
from choosy_girl import choosy
from desperate_girl import desperate 
from utility_gift import utility 
from essential_gift import essential
from luxury_gift import luxury 

''' this is abstract class used to implement algorithm for storing data for commiitted couples '''
class algorithm(object):
	__metaclass__ = ABCMeta 
	def __init__(self ):
		self.array_of_couple = None  

	''' this is abstract method , ehich will be made conmcrete in child method that applies it '''
	@abstractmethod 
	def algo_applier (self ): 
		pass 
	
