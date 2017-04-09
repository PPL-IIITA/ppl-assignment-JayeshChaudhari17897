from q3_gift import gift 


class luxury(gift):
	
	def __init__(self , luxury_gift_rating = None ,cost = None , value = None, gift_name = None ): 
		super(luxury, self ).__init__()
		self.luxury_gift_rating = luxury_gift_rating 
