import csv

with open('pvp3.csv') as csvfile:
        reader = csv.reader(csvfile)
        vlist = list()
        ipl = dict()

        for row in reader:
                if row[0] not in vlist:
                        vlist.append(row[0])

                if row[0] not in ipl:                 
                        ipl[row[0]] = [0 for x in range(5)]

                if '0' in row[15]:
                    ipl[row[0]][0] = ipl[row[0]][0] + int(row[3])
                if '1' in row[15]:
                    ipl[row[0]][1] = ipl[row[0]][1] + int(row[3])
                if '2' in row[15]:
                    ipl[row[0]][2] = ipl[row[0]][2] + int(row[3])
                if '3' in row[15]:
                    ipl[row[0]][3] = ipl[row[0]][3] + int(row[3])
                if '4' in row[15]:
                    ipl[row[0]][4] = ipl[row[0]][4] + int(row[3])

        v = list(ipl.values())

        for i in range(5):
                for j in range(112):
                        if float(v[j][0] + v[j][1] + v[j][2] + v[j][3] + v[j][4]) == 0.0:
                                 continue
                        v[j][i] = float(v[j][i])/float(v[j][0] + v[j][1] + v[j][2] + v[j][3] + v[j][4])

        for keys,values in ipl.items(): 
                print(keys,values)
