#This code assigns the cluster no of the batsman and bowler in pvp file
#final output file is probabilty3.csv
import csv

#extracting columns in pvp file
playerlist1 = []
with open('probability1.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		playerlist1.append(row[0])
batsmanpvp = sorted(set(playerlist1))  # set of batsmen in col1
csvfile.close()

playerlist2 = []
with open('probability1.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		playerlist2.append(row[1])
bowlerpvp = sorted(set(playerlist2))  # set of bowlers in col2
csvfile.close()


#extracting columns in bowlerclusters
playerlist3 = []
with open('ClusterBowl0.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		playerlist3.append(row[0])
bowl0 = sorted(set(playerlist3))  # set of bowlers in cluster0
bowl0 = [w.replace(w, w.split()[0][0] +w.split()[-1]) for w in bowl0]

csvfile.close()

playerlist4 = []
with open('ClusterBowl1.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		playerlist4.append(row[0])
bowl1 = sorted(set(playerlist4))  # set of bowlers in cluster1
bowl1 = [w.replace(w, w.split()[0][0] +w.split()[-1]) for w in bowl1]
csvfile.close()

playerlist5  = []
with open('ClusterBowl2.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		playerlist5.append(row[0])
bowl2 = sorted(set(playerlist5))  # set of bowlers in cluster2
bowl2 = [w.replace(w, w.split()[0][0] +w.split()[-1]) for w in bowl2]
csvfile.close()

playerlist6 = []
with open('ClusterBowl3.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		playerlist6.append(row[0])
bowl3 = sorted(set(playerlist6))  # set of bowlers in cluster3
bowl3 = [w.replace(w, w.split()[0][0] +w.split()[-1]) for w in bowl3]
csvfile.close()

playerlist7 = []
with open('ClusterBowl4.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		playerlist7.append(row[0])
bowl4 = sorted(set(playerlist7))  # set of bowlers in cluster4
bowl4 = [w.replace(w, w.split()[0][0] +w.split()[-1]) for w in bowl4]
csvfile.close()



#extracting columns in batsmanclusters

playerlist8 = []
with open('ClusterBat0.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		playerlist8.append(row[0])
bat0 = sorted(set(playerlist8))
bat0 = [w.replace(w, w.split()[0][0] + w.split()[-1]) for w in bat0] #get initAlphabet + surname
#print bat0
csvfile.close()


playerlist9 = []
with open('ClusterBat1.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		playerlist9.append(row[0])
bat1 = sorted(set(playerlist9))  # set of batsman in cluster1
bat1 = [w.replace(w, w.split()[0][0] +w.split()[-1]) for w in bat1]
csvfile.close()

playerlist10 = []
with open('ClusterBat2.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		playerlist10.append(row[0])
bat2 = sorted(set(playerlist10))  # set of batsman in cluster2
bat2 = [w.replace(w, w.split()[0][0] +w.split()[-1]) for w in bat2]
csvfile.close()


playerlist11 = []
with open('ClusterBat3.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		playerlist11.append(row[0])
bat3 = sorted(set(playerlist11))  # set of batsman in cluster3
bat3 = [w.replace(w, w.split()[0][0] +w.split()[-1]) for w in bat3]
csvfile.close() 

playerlist12 = []
with open('ClusterBat4.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		playerlist12.append(row[0])
bat4 = sorted(set(playerlist12))  # set of batsman in cluster4
bat4 = [w.replace(w, w.split()[0][0] +w.split()[-1]) for w in bat4]
csvfile.close()

#Assign Batsman Grp

with open ('probability1.csv' , 'rb') as csvfile:
	reader = csv.reader(csvfile)
	data = []
	out_file = open("probability2.csv", "wb")
	writer = csv.writer(out_file)
	count=0
	for row in reader:
		if (row[0].split()[0][0] + row[0].split()[-1]) in bat0:
			row.append(0)
			#writer.writerow(row)
		elif (row[0].split()[0][0] + row[0].split()[-1]) in bat1:
			row.append(1)
			#writer.writerow(row)
		elif (row[0].split()[0][0] + row[0].split()[-1]) in bat2:
			row.append(2)
			#writer.writerow(row)
		elif (row[0].split()[0][0] + row[0].split()[-1]) in bat3:
			row.append(3)
			#writer.writerow(row)
		elif (row[0].split()[0][0] + row[0].split()[-1]) in bat4:
			row.append(4)
			#writer.writerow(row)
		writer.writerow(row)
csvfile.close()
out_file.close()

#string.split()[-1]

#Assign Bowler Grp

with open ('probability2.csv' , 'rb') as csvfile:
	reader = csv.reader(csvfile)
	data = []
	out_file = open("probability3.csv", "wb")
	writer = csv.writer(out_file)
	count=0
	for row in reader:
		if (row[1].split()[0][0] + row[1].split()[-1]) in bowl0:
			row.append(0)
			#writer.writerow(row)
		elif (row[1].split()[0][0] + row[1].split()[-1]) in bowl1:
			row.append(1)
			#writer.writerow(row)
		elif (row[1].split()[0][0] + row[1].split()[-1]) in bowl2:
			row.append(2)
			#writer.writerow(row)
		elif (row[1].split()[0][0] + row[1].split()[-1]) in bowl3:
			row.append(3)
			#writer.writerow(row)
		elif (row[1].split()[0][0] + row[1].split()[-1]) in bowl4:
			row.append(4)
			#writer.writerow(row)
		writer.writerow(row)
csvfile.close()
out_file.close()
	








