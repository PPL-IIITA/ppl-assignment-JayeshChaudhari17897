from q1_girl import Girl
from q1_couple import Couple 
from q1_boy import Boy 
import csv 
class ppl_q1 :
	def run(self):
			girl_array=[]
			boy_array=[]
			couple_array=[]

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
				boy_array[i].type_of_boy = boyslist[i][3]
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
				girl_array[i].type_of_girl = girlslist[i][3]
				girl_array[i].maintenance = int(girlslist[i][4])



			#ranges galat thi
			#check boys class once there is a change in it as well
			for j in range(row_count_girls):
				for i in range(row_count_boys):#neeche wali line mai req likha tha kuch defined nahi tha wo
					if (boy_array[i].budget >= girl_array[j].maintenance and boy_array[i].attractiveness <= girl_array[j].attractiveness  and boy_array[i].commited==False and girl_array[j].committed == False) :
						boy_array[i].commited = True
						girl_array[j].commited = True

						couple_array.append(Couple(boy_array[i],girl_array[j]))

						break
			k= len(couple_array) # k define kr de yahan pr


			with open("ans_file.txt","w") as ansfile :
				ansfilewriter = csv.writer(ansfile)
				for i in range(k):
					ansfilewriter.writerow([couple_array[i].id])






