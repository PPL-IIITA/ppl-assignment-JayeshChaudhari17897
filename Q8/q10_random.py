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
from q9_template_best_k import template
import random

''' this class is random generator   '''
class random1(object):
	def __init__ (self ):
		pass

	''' this function gives unique random index  to return a unique index to the calling object ''' 
	def random_of_n (self , array  ,k ):
		array_random=[]

		my_list = list(xrange(0,k)) 
		random.shuffle(my_list)



		for i in range(k):
			
			array_random.append(array[my_list[i]])


		for i in range(k):
			array[i]=array_random[i]





