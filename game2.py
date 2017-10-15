import pandas as pd
import random


ip = pd.read_csv('input4.csv') #The input file
team1 = []
team2 = []
for i in ip .Team1:   
	team1.append(i)   #team1 and team2 are lists that contain players from teams 1 and 2 respectively
for i in ip . Team2:
	team2.append(i)


files = pd.read_csv('pvp.csv')
DBat = {} #Dbat is a dictionary keys->batsman name values->cluster_nos
DBall = {} #DBall: Key is bowler name, value is the bowler cluster number
for i in range(len(files)):
	batname = files.loc[i].BatName.strip()
	DBat[batname] = files.loc[i].BatclustNo
	bowlname = files.loc[i].BowlName.strip()
	DBall[bowlname] = files.loc[i].BowlclustNo
#BatmanNames = list(DBat.keys())
#BowlerNames = list(DBall.keys())


runs1=0  #runs scored by team1
runs2=0
wickets1=0
wickets2=0

#batfiles = sorted(glob.glob("BattingCluster/*.csv"))
#bowlfiles = sorted(glob.glob("BowlingCluster/*.csv"))


cp = pd.read_csv('clustprob.csv')
cm = pd.DataFrame(columns=['BatclustNo','BowlclustNo','0s', '1s', '2s', '3s', '4s',  '6s','Out'])
for i in range(len(cp)):
	cm.loc[i] = [None for n in range(9)]
	cm.loc[i].BatclustNo = cp.loc[i].BatclustNo
	cm.loc[i].BowlclustNo = cp.loc[i].BowlclustNo
	cm.loc[i]['0s'] = float(cp.loc[i]['0s'])
	cm.loc[i]['1s'] = float(cp.loc[i]['1s']) + float(cp.loc[i]['0s'])     #Computing cumulative probability 
	cm.loc[i]['2s'] = float(cp.loc[i]['2s']) + float(cm.loc[i]['1s'])
	cm.loc[i]['3s'] = float(cp.loc[i]['3s']) + float(cm.loc[i]['2s'])
	cm.loc[i]['4s'] = float(cp.loc[i]['4s']) + float(cm.loc[i]['3s'])
	cm.loc[i]['6s'] = float(cp.loc[i]['6s']) + float(cm.loc[i]['4s'])
	cm.loc[i].Out = 1


def getScore(batsman,bowler):
	ptr = random.random()
	prob = cm.loc[cm['BatclustNo'] == batsman].loc[cm['BowlclustNo'] == bowler]
	if ptr <= float(prob['0s']):
		return 0
	elif  ptr <= float(prob['1s']):
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
	return DBat.get(batsman,2)
def clusterBowl(bowler):
	return DBall.get(bowler,0)

def teamplay(t1, t2):
	striker=t1[0]
	runner=t1[1]
	bowler=t2[len(t2)-1]
	count=2
	nextBatsman=2
	wickets=0
	over=0
	runs = 0
	while(wickets<10 or over<20):
		ball=1
		over+=1
		while(ball<6 or wickets<10):
			score=getScore(clusterBat(striker),clusterBowl(bowler))
			if(score==99):
				runs += 1
			else:
				ball += 1
				if(score == -1):
					wickets += 1
					#print "----",wickets
					striker=t1[nextBatsman]
					nextBatsman = (nextBatsman + 1)%11
				else:
					runs+=score
					if(score==1 or score==3):
						(striker,runner) = (runner,striker)
		(striker,runner) = (runner,striker)
		bowler = t2[len(t2)-count]
		count = (count+1)%5 + 1
	return runs,wickets

def teamplay2(t1, t2,runs1):
	striker=t1[0]
	runner=t1[1]
        bowler=t2[len(t2)-1]
	count=2
	nextBatsman=2
	wickets=0
	over=0
	runs = 0
	while(wickets<10 or over<20):
		ball=1
		over+=1
		while(ball<6 and runs<=runs1 or wickets<10):
			score=getScore(clusterBat(striker),clusterBowl(bowler))
			if(score==99):
				runs += 1
			else:
				ball += 1
				if(score == -1):
					wickets += 1
					striker=t1[nextBatsman]
					nextBatsman = (nextBatsman + 1)%11
				else:
					runs+=score
					if(score==1 or score==3):
						(striker,runner) = (runner,striker)
		(striker,runner) = (runner,striker)
		bowler = t2[len(t2)-count]
		count = (count+1)%5 + 1
	return runs,wickets

def GameOutcome(runs1,runs2,wickets2):
	if(runs1==runs2):
		print('Match was a tie!')
	elif(runs1>runs2):
		print('team2 won by '+str(runs1-runs2)+' runs')
	else:
		wkt1 = (wickets1*10)/40
		wkt2 = (wickets2*10)/40
		print('team1 won by' + str(10-wkt2)+' wickets')
		#print('team2 won by '+str(((wickets2*10)/40)-((wickets1*10)/40)+' wickets'))


runs1,wickets1 = teamplay(team1, team2)
runs2,wickets2 = teamplay2(team2, team1,runs1)
print('Team2 : '+str(runs1)+'/'+str((wickets1*10)/40))
print('Team1 : '+str(runs2)+'/'+str((wickets2*10)/40))
GameOutcome(runs1,runs2,wickets2)