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
from q7_algo import algorithm
from q7_hash_table import hash_table
from q7_sorted_array import sorted



''' this class creates a template , to select best k objects among given n '''
class template(object):

	def __init__(self):
		self.kj = 0
	

	''' this function compares boy according to their values of attractiveness '''	
	def cmp_boy(boy_1  , boy_2 ):
		if (boy_1.attractiveness < boy_2.attractiveness):
			return 1
		elif (boy_1.attractiveness > boy_2.attractiveness):
			return -1 
		else :
			return 0

	'''this function compares girls according to their values of attractiveness '''		
	def cmp_girl(girl_1 , girl_2): 
		if (girl_1.attractiveness < girl_2.attractiveness):
			return 1
		elif (girl_1.attractiveness > girl_2.attractiveness):
			return -1 
		else :
			return 0
	''' this function comapres gifts according to their cost '''
	def cmp_gift(gift_object1 , gift_object2): 
		gift1 = gift_object1
		gift2 = gift_object2

		if (gift1.gift_cost > gift2.gift_cost):
			return 1
		elif ( gift1.gift_cost < gift2.gift_cost):
			return -1
		elif (gift1.gift_value < gift2.gift_value):
			return 1
		elif ( gift1.gift_value > gift2.gift_value):
			return -1
		else :
			return 0


	''' this function returnns best k objects among n objects '''
	def best_k(self , k , b_g_gi , array): 
		if ( b_g_gi == 'boy' ):
			array.sort(cmp_boy , reverse = True)
		elif (b_g_gi == 'girl'):
			array.sort(cmp_girl , reverse = True)
		elif (b_g_gi == 'gift'):
			array.sort(cmp_gift , reverse = True)


