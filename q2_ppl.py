from q2_girl import Girl
from q2_couple import Couple 
from q2_boy import Boy 
from q2_gift import Gift
import csv 
import math

girl_array=[]
boy_array=[]
couple_array=[] 
gift_array = []

row_count_boys = 0
with open ("boys.csv","r") as boysfile :
	boyReader = csv.reader(boysfile,delimiter=',')
	boyslist = []
	
	#row_count_boys = sum(1 for row in boyReader)
	for row in boyReader:
			row_count_boys = row_count_boys +1
			boyslist = boyslist + [row]
boysfile.close()


for i in range(row_count_boys):
	boy_array.append(Boy())
	boy_array[i].name = boyslist[i][0]
	boy_array[i].attractiveness = int(boyslist[i][1])
	boy_array[i].intelligence = int(boyslist[i][2])
	boy_array[i].typee = boyslist[i][3]
	boy_array[i].budget = int(boyslist[i][4])

row_count_girls = 0

with open ("girls.txt","r") as girlsfile :
	girlReader = csv.reader(girlsfile)
	girlslist = []
	#row_count_girls = sum(1 for row in girlReader)
	for row in girlReader:
		if len(row)!=0 :
			row_count_girls = row_count_girls + 1
			girlslist = girlslist + 	[row]




for i in range(row_count_girls):
	girl_array.append(Girl())
	girl_array[i].name = girlslist[i][0]
	girl_array[i].attractiveness = int(girlslist[i][1])
	girl_array[i].intelligence =int(girlslist[i][2])
	girl_array[i].typee = girlslist[i][3]
	girl_array[i].maintenance = int(girlslist[i][4]) 

row_count_gifts = 0

with open ("gifts.txt","r") as giftsfile :
	giftReader = csv.reader(giftsfile)
	giftslist = []
	#row_count_girls = sum(1 for row in girlReader)
	for row in giftReader:
		if len(row)!=0 :
			row_count_gifts = row_count_gifts + 1
			giftslist = giftslist + 	[row]



for i in range (row_count_gifts):
	gift_array.append(Gift())
	gift_array[i].gift_type = giftslist[i][0]
	gift_array[i].gift_cost  = int(giftslist[i][1])
	gift_array[i].gift_value = int(giftslist[i][2])




for j in range(row_count_girls):
	for i in range(row_count_boys):
		if (boy_array[i].budget >= girl_array[j].maintenance and boy_array[i].attractiveness <= girl_array[j].attractiveness  and boy_array[i].committed==False and girl_array[j].committed == False) :
			boy_array[i].committed = True
			girl_array[j].committed = True
			couple_array.append(Couple(boy_array[i],girl_array[j]))
			
			break
k= len(couple_array) # k define kr de yahan pr 


with open("ans_file_couples.txt","w") as ansfile :
	ansfilewriter = csv.writer(ansfile)
	for i in range(k):
		ansfilewriter.writerow([couple_array[i].id])



def comapare_gifts(gift_object1 , gift_object2): # comparator function for gifts comparing
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


gift_array.sort(comapare_gifts)  # sorting gifts according to its cost followed by value .


for i in range(k):
	if (couple_array[i].boy.typee == 'Geek'):
		main_cost = couple_array[i].girl.maintenance
		i1 = 0
		y = 0
		while (i < main_cost):
			i1 = i1 + gift_array[y].gift_cost
			couple_array[i].array_gift.add(gift_array[y])
			y = y + 1

		y1 = couple_array[i].boy.budget - i1 

		for j in range(row_count_gifts):
			if ( gift_array[j].typee == 'Luxury'  and y1 >= gift_array[j].gift_cost):
				couple_array[i].array_gift.add(gift_array[y])


	elif ( couple_array[i].boy.typee == 'Miser'):
		main_cost = couple_array[i].girl.maintenance
		j = 0 
		x = 0 
		while ( j < main_cost):
			j = j + gift_array[x].gift_cost
			couple_array[i].array_gift.add(gift_array[x])
			x = x + 1
	else :          
		main_cost = couple_array[i].boy.budget
		j = 0 
		x = 0  
		while ( j < main_cost and x < row_count_gifts):
			j = j + gift_array[x].gift_cost
			couple_array[i].array_gift.append(gift_array[x])
			x = x + 1

for i in range(k):
	x = 0 
	y = 0 
	hap_boy = 0
	hap_girl = 0

	for j in range(len(couple_array[i].array_gift)):
		x = x + couple_array[i].array_gift[j].gift_cost
		y = y + couple_array[i].array_gift[j].gift_value 

	main_cost = couple_array[i].girl.maintenance

	if ( couple_array[i].girl.typee == 'Choosy'):
		hap_girl = hap_girl + math.log(x -main_cost + 2*y)

	elif (couple_array[i].girl.typee == 'Desperate'):
		hap_girl = hap_girl + (2.73 ** (x-main_cost))
	else :
		hap_girl = x -main_cost + y


	if ( couple_array[i].boy.typee == 'Geek'):
		hap_boy = hap_boy + couple_array[i].girl.intelligence

	elif (couple_array[i].boy.typee == 'Miser' ):
		hap_boy = hap_boy + couple_array[i].boy.budget - x 

	else :
		hap_boy = hap_girl

	couple_array[i].boy.happiness = hap_boy
	couple_array[i].girl.happiness = hap_girl
	couple_array[i].happiness = hap_girl + hap_boy 
	couple_array[i].fitting = couple_array[i].boy.budget - main_cost + abs(couple_array[i].girl.attractiveness - couple_array[i].boy.attractiveness) + abs(couple_array[i].girl.intelligence - couple_array[i].boy.intelligence)




def compare_fitting (couple1 , couple2):
		if (couple1.fitting > couple2.fitting):
			return 1
		elif couple1.fitting < couple2.fitting:
			return -1
		else :
			return 0


def compare_happiness(couple1 , couple2) :
			if couple1.happiness > couple2.happiness :
				return 1
			elif couple1.happiness < couple2.happiness :
					return -1
			else :
					return 0


couple_array.sort(compare_fitting, reverse = True)

file = open('ans_file_Compatibility.txt','w') 
file.write('Given Below are Couple According to The sorted value of Comapatibility \n\n \n') 
file.close()	

with open("ans_file_Compatibility.txt","a") as ansfile :
	ansfilewriter = csv.writer(ansfile)
	for i in range(k):
		ansfilewriter.writerow([couple_array[i].id]+[couple_array[i].fitting])





couple_array.sort(compare_happiness , reverse = True)





file = open('ans_file_Happiness.txt','w') 

file.write('Given Below are Couple According to The sorted value of happiness\n\n \n') 
file.close()	

	
with open("ans_file_Happiness.txt","a") as ansfile :
	ansfilewriter = csv.writer(ansfile)
	for i in range(k):
		ansfilewriter.writerow([couple_array[i].id]+[couple_array[i].happiness])
		



























