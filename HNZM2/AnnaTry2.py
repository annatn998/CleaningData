from os import listdir
file = listdir('.')
openedFiles = []


for x in file:
    if 'results_' in x:
        readFiles = open(x,'r')
        read = readFiles.readlines()
        openedFiles.append(read)

#############################################################
#############################################################
#isolating all of the different variables that I will need later

for _ in range(len(openedFiles)):
    items = openedFiles[_] # so that it is easier to reference
    nearMiss = 0
    fullMiss = 0
    hit = 0
    row4split = items[3].split(',')
    condition = items[0]
    date = items[1]
    IP = items[2].split()[2]
    name = row4split[0]
    age = row4split[1]
    gender = row4split[2]

    if len(items) > 4:
        hitOrMiss = items[4]
        happiness = items[7]
        wantsMore = items[8]

    if hitOrMiss == 'nearMiss':
        nearMiss += 1
    elif hitOrMiss == 'fullMiss':
        fullMiss += 1
    else:
        hit += 1

    if gender.lower() == 'male':
        pass # will append the gender into the csv file here (1)
    else:
        pass #write in the csv file (2)

















