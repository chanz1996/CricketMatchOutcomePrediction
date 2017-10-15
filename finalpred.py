import pandas as pd
import random
import glob

files = pd.read_csv('probability.csv')
DBat = {}
DBall = {}
for i in range(len(files)):
	batname = files.loc[i].BatName.strip()
	DBat[batname] = files.loc[i].BatclustNo
	bowlname = files.loc[i].BowlName.strip()
	DBall[bowlname] = files.loc[i].BowlclustNo
#BatmanNames = list(DBat.keys())
#BowlerNames = list(DBall.keys())

ip = pd.read_csv('lineup.csv')
team1 = [];team2 = []
for i in ip .Team1:                      
	team1.append(i)    #team1 and team2 are lists that contain players from teams 1 and 2 respectively
for i in ip . Team2:
	team2.append(i)

runs1=0        #runs scored by team1
runs2=0        #runs scored by team2
wickets1=0     #number of wickets of team1
wickets2=0     #number of wickets of team2

#batfiles = sorted(glob.glob("BattingCluster/*.csv"))
#bowlfiles = sorted(glob.glob("BowlingCluster/*.csv"))


cp = pd.read_csv('cp1.csv')
cm = pd.DataFrame(columns=['BatclustNo','BowlclustNo','0s', '1s', '2s', '3s', '4s',  '6s','Out'])
for i in range(len(cp)):
	cm.loc[i] = [None for n in range(9)]
	cm.loc[i].BatclustNo = cp.loc[i].BatclustNo
	cm.loc[i].BowlclustNo = cp.loc[i].BowlclustNo
	cm.loc[i]['0s'] = float(cp.loc[i]['0s'])
	cm.loc[i]['1s'] = float(cp.loc[i]['1s']) + float(cm.loc[i]['0s'])   #Computing cumulative probability 
	cm.loc[i]['2s'] = float(cp.loc[i]['2s']) + float(cm.loc[i]['1s'])
	cm.loc[i]['3s'] = float(cp.loc[i]['3s']) + float(cm.loc[i]['2s'])
	cm.loc[i]['4s'] = float(cp.loc[i]['4s']) + float(cm.loc[i]['3s'])
	cm.loc[i]['6s'] = float(cp.loc[i]['6s']) + float(cm.loc[i]['4s'])
	cm.loc[i].Out = 1


def getScore(batsman,bowler):
	ptr = random.random()           #generate a random number
	prob = cm.loc[cm['BatclustNo'] == batsman].loc[cm['BowlclustNo'] == bowler]  #get the rows matching bowler and batsman cluster no.
	if ptr <= float(prob['0s']):
		return 0
	elif  ptr <= float(prob['1s']):  #this column has prob of 0s + prob 1s
		return 1
	elif ptr <= float(prob['2s']):   
		return 2
	elif ptr <= float(prob['3s']):
		return 3
	elif  ptr <= float(prob['4s']):
		return 4
	elif ptr <= float(prob['6s']):
		return 6
	else:
		return -1	

def clusterBat(batsman):
	return DBat.get(batsman,2)    #second argument indicates number to be returned if batsman is not present in DBat
def clusterBowl(bowler):
	return DBall.get(bowler,0)

def teamplay(tea1, tea2):
	striker=tea1[0]
	runner=tea1[1]
	bowler=tea2[len(tea2)-1]
	count=2
	nextBatsman=2
	wickets=0
	over=0
	runs = 0
	while(wickets<10 or over<20):
		ball=1                  #first ball
	#	over+=1
		while(ball<6 or wickets<10):            #till 1 over is completed and number of wickets is still less than 10
			score=getScore(clusterBat(striker),clusterBowl(bowler))
			if(score==99):                 #increment the number of runs only when the score reaches 99
				runs += 1
			else:
				ball += 1             
				if(score == -1):       # if score is -1 it means the team have lost a wicket
					wickets += 1     # move on to the next player in the team 
					#print "----",wickets
					striker=tea1[nextBatsman]           #get the next batsman  
					nextBatsman = (nextBatsman + 1)%11  #get the next bowler
				else:
					runs+=score        #increase number of runs
					if(score==1 or score==3):
						(striker,runner) = (runner,striker)
		over+=1
		(striker,runner) = (runner,striker)
		bowler = tea2[len(tea2)-count]
		count = (count+1)%5 + 1
	return runs,wickets

def teamplay2(tea1, tea2,runs1):     #for team2
	striker=tea1[0]
	runner=tea1[1]
        bowler=tea2[len(tea2)-1]
	count=2
	nextBatsman=2
	wickets=0
	over=0
	runs = 0
	while(wickets<10 or over<20):
		ball=1
		over+=1
		while(ball<6 and runs<=runs1 or wickets<10):   #repeat as long as runs of team2 less than runs of team1
			score=getScore(clusterBat(striker),clusterBowl(bowler))
			if(score==99):
				runs += 1
			else:
				ball += 1
				if(score == -1):
					wickets += 1
					striker=tea1[nextBatsman]
					nextBatsman = (nextBatsman + 1)%11
				else:
					runs+=score
					if(score==1 or score==3):
						(striker,runner) = (runner,striker)
		(striker,runner) = (runner,striker)
		bowler = tea2[len(tea2)-count]
		count = (count+1)%5 + 1
	return runs,wickets

def getWinner(runs1,runs2,wickets2):
	if(runs1==runs2):
		print('Match was a tie!')
	elif(runs1>runs2):
		print('team1 won by '+str(runs1-runs2)+' runs')
	else:
		#print('team2 won by '+str(10-wickets2)+' wickets')
		print('team2 won by '+str(((wickets2*10)/40)-((wickets1*10)/40)+' wickets'))


runs1,wickets1 = teamplay(team1, team2)
runs2,wickets2 = teamplay2(team2, team1,runs1)
print('Team1 : '+str(runs1)+'/'+str((wickets1*10)/40))
print('Team2 : '+str(runs2)+'/'+str((wickets2*10)/40))
getWinner(runs1,runs2,wickets2)