from q7_algo import algorithm 
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

''' this class applies hash table version of storing data of committed boys & girls'''
class hash_table(algorithm):
	def __init__(self  ):
		super(hash_table , self).__init__()


	  
	def algo_applier(self, array_of_couples ):
		hash_map = {}

		k = len(array_of_couples)

		for i in range(k):
			hash_map[array_of_couples[i].boy.name]= array_of_couples[i].girl.name

		return hash_map

