

class template(object):
	def __init__ ( self , k , b_g_gi):
		self.k = k
		self.b_g_gi = b_g_gi

		
	def cmp_boy(boy_1  , boy_2 ):
		if (boy_1.attractiveness < boy_2.attractiveness):
			return 1
		elif (boy_1.attractiveness > boy_2.attractiveness):
			return -1 
		else :
			return 0


	def cmp_girl(girl_1 , girl_2):
		if (girl_1.attractiveness < girl_2.attractiveness):
			return 1
		elif (girl_1.attractiveness > girl_2.attractiveness):
			return -1 
		else :
			return 0

	def 



	def best_k(self , k , b_g_gi , array):
		if ( b_g_gi == 'boy' ):
			array.sort(cmp_boy , reverse = True)
		elif (b_g_gi == 'girl'):
			array.sort(cmp_girl , reverse = True)
		else (b_g_gi == 'gift'):
			array.sort(cmp_gift , reverse = True)


