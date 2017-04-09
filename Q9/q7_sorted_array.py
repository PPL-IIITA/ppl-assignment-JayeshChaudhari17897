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
''' this class is used to store the data of commiitted boys and girls in sorted array ''' 
class sorted(algorithm):
	def __init__(self ):
		super(sorted , self).__init__()

	''' this function compares two couplkes according to the names of boys in couple '''
	def cmp(couple_1 , couple_2): 
		if ( couple_1.boy.name > couple_1.boy.name ):
			return 1

		elif (couple_1.boy.name < couple_2.boy.name ):
			return -1
		else :
			return 0 
	''' this function stores  the information  in  sorted array ''' 
	def algo_applier(self , array_of_couples):
		k = len(array_of_couples)
		print k 
		sorted_array=[]
		for i in range(k):
			print i
			a = array_of_couples[i].boy
			b = array_of_couples[i].girl
			sorted_array.append(couple(a,b))
			#sorted_array[i]=array_of_couples[i]

		sorted_array.sort(cmp , reverse = False)
		return sorted_array


