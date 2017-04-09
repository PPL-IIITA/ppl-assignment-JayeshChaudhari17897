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
	if boyslist[i][3] == 'miser' :
		boy_array.append(miser())
		boy_array[i].name = boyslist[i][0]
		boy_array[i].attractiveness = int(boyslist[i][1])
		boy_array[i].intelligence = int(boyslist[i][2])
		boy_array[i].typee = boyslist[i][3]
		boy_array[i].budget = int(boyslist[i][4])
	elif boyslist[i][3] == 'geek' :
		boy_array.append(geek())
		boy_array[i].name = boyslist[i][0]
		boy_array[i].attractiveness = int(boyslist[i][1])
		boy_array[i].intelligence = int(boyslist[i][2])
		boy_array[i].typee = boyslist[i][3]
		boy_array[i].budget = int(boyslist[i][4])
	else :
		boy_array.append(generous())
		boy_array[i].name = boyslist[i][0]
		boy_array[i].attractiveness = int(boyslist[i][1])
		boy_array[i].intelligence = int(boyslist[i][2])
		boy_array[i].typee = boyslist[i][3]
		boy_array[i].budget = int(boyslist[i][4])

row_count_girls = 0
with open ("girls.txt","r") as girlsfile :
	girlReader = csv.reader(girlsfile,delimiter=',')
	girlslist = []
	
	#row_count_boys = sum(1 for row in boyReader)
	for row in girlReader:
			row_count_girls = row_count_girls +1
			girlslist = girlslist + [row]
girlsfile.close()

'''with open ("girls.txt","r") as girlsfile :
	girlReader = csv.reader(girlsfile)
	girlslist = []
	row_count_girls = sum(1 for row in girlReader)
	for row in girlReader:
		if len(row)!=0 :
			row_count_girls = row_count_girls + 1
			girlslist = girlslist + 	[row] ///
'''


for i in range(row_count_girls):
	
	if girlslist[i][3] == 'normal' :
		girl_array.append(normal())
		girl_array[i].name = girlslist[i][0]
		girl_array[i].attractiveness = int(girlslist[i][1])
		girl_array[i].intelligence =int(girlslist[i][2])
		girl_array[i].typee = girlslist[i][3]
		girl_array[i].maintenance = int(girlslist[i][4]) 

	elif girlslist[i][3] == 'desperate':
		girl_array.append(desperate())
		girl_array[i].name = girlslist[i][0]
		girl_array[i].attractiveness = int(girlslist[i][1])
		girl_array[i].intelligence =int(girlslist[i][2])
		girl_array[i].typee = girlslist[i][3]
		girl_array[i].maintenance = int(girlslist[i][4]) 
	else :
		girl_array.append(choosy())
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
	if giftslist[i][0] == 'essential':
		gift_array.append(essential())
		gift_array[i].gift_type = giftslist[i][0]
		gift_array[i].gift_cost  = int(giftslist[i][1])
		gift_array[i].gift_value = int(giftslist[i][2])

	elif giftslist[i][0] == 'utility':
		gift_array.append(utility())
		gift_array[i].gift_type = giftslist[i][0]
		gift_array[i].gift_cost  = int(giftslist[i][1])
		gift_array[i].gift_value = int(giftslist[i][2])
	else :
		gift_array.append(luxury())
		gift_array[i].gift_type = giftslist[i][0]
		gift_array[i].gift_cost  = int(giftslist[i][1])
		gift_array[i].gift_value = int(giftslist[i][2])






for j in range(row_count_girls):
	for i in range(row_count_boys):
		if (boy_array[i].budget >= girl_array[j].maintenance and boy_array[i].attractiveness <= girl_array[j].attractiveness  and boy_array[i].committed==False and girl_array[j].committed == False) :
			boy_array[i].committed = True
			girl_array[j].committed = True
			couple_array.append(couple(boy_array[i],girl_array[j]))
			
			break
k= len(couple_array) # k define kr de yahan pr 


with open("ans_file_couples.txt","w") as ansfile :
	ansfilewriter = csv.writer(ansfile)
	for i in range(k):
		ansfilewriter.writerow([couple_array[i].id])

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



d={}

t = 300
i = 0

for z in range(t):
	
	k1 = len(couple_array)
	for i in range(k1):
		if ( i < len(couple_array) and  couple_array[i].boy.happiness + couple_array[i].girl.happiness < t):
			couple_array[i].boy.committed = False
			couple_array[i].girl.committed = False 
			couple_array[i].boy.happiness = 0.0
			couple_array[i].girl.happiness = 0.0
			d[couple_array[i].boy.name] = couple_array[i].girl.name
			
			with open("log.txt","a") as ansfile :
				ansfilewriter = csv.writer(ansfile)
				ansfilewriter.writerow([couple_array[i].id]+[couple_array[i].happiness])
			#print couple_array[i].boy.name + couple_array[i].girl.name
			couple_array.remove(couple_array[i]);
			



	for j in range(row_count_girls):
		for i in range(row_count_boys):
			if (  boy_array[i].budget >= girl_array[j].maintenance  and boy_array[i].attractiveness <= girl_array[j].attractiveness  and boy_array[i].committed==False and girl_array[j].committed == False  and d[boy_array[i].name]!= girl_array[j].name ) :
				boy_array[i].committed = True
				girl_array[j].committed = True
				couple_array.append(couple(boy_array[i],girl_array[j]))
				break

couple_array.sort(compare_fitting, reverse = True)
k = len(couple_array)
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
		
file = open('ans_file_Happiness_after_breakup.txt','w') 

file.write('Given Below are Couple According to The sorted value of happiness sfege ytreu 5t6u6tu t\n\n \n') 
file.close()	

	
with open("ans_file_Happiness_breakup.txt","a") as ansfile :
	ansfilewriter = csv.writer(ansfile)
	for i in range(k):
		ansfilewriter.writerow([couple_array[i].id]+[couple_array[i].happiness])






























