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



#set value of k to change the way in which committed couples are stored



k = 1  # 1 for default(array implementation) 
		# 2 for hash_table 
		# 3 for sorted_array 




if ( k == 1):
	couple_array_store = couple_array
elif ( k == 2 ):

	store  = hash_table()
	couple_array_store = store.algo_applier(couple_array)


else :
	store = sorted()
	couple_array_store = store.algo_applier(couple_array)


























