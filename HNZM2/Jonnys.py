from os import listdir
allFiles = listdir('.')
ipAddressList = []
fileRead = []
listOfDates = []
dictPptsCondition = {}
NoSkill = 0
NoLuck = 0
NoMixed = 0
for everyFile in allFiles:
    if 'results_' in everyFile:
        fileOpen = open(everyFile, 'r')
        openedFiles = fileOpen.readlines()
        fileRead.append(openedFiles)
##########################################################
#extracting date and time
##########################################################
for items in fileRead:
    # dateAndTime = items[1]
    # day = dateAndTime[6:8]
    # month = dateAndTime[8:10]
    # year = dateAndTime[10:14]
    # date = day + '-' + month + '-' + year
    # listOfDates.append(date)
##########################################################
##########################################################
    totalNoOfTrials = 0
    totalHappiness = 0
    totalWillingness = 0
    nearMissNo = 0
    hitNo = 0
    fullMissNo = 0

    listHappinessScores = []
    ipAddress = items[2].strip('\n')
    if ipAddress not in ipAddressList:
        ipAddressList.append(ipAddress)
        splitNameAgeGender = items[3].split(',')
        name = splitNameAgeGender[0]
        age = splitNameAgeGender[1]
        gender = splitNameAgeGender[2].lower().strip('\n')
        if gender == 'male':
            gender = 1
        else:
            gender = 2
        #############################################################
        #############################################################
    for everyTrial in range(5,len(items[5:])+1):
        totalNoOfTrials += 1
        split = items[everyTrial].split(',')
        if len(split) > 2:
            outcome = split[4]
            eachHappiness = split[7]
            eachWillingness = split[8].strip('\n')
            totalHappiness += int(eachHappiness)
            totalWillingness += int(eachWillingness)
            listHappinessScores.append(eachHappiness)
        ############################################################
        #proportion of hit near miss or full miss
        ############################################################
        if outcome == 'hit':
            hitNo += 1
        elif outcome == 'nearMiss':
            nearMissNo += 1
        elif outcome == 'fullMiss':
            fullMissNo += 1
    propHit = hitNo / totalNoOfTrials
    propNearMiss = nearMissNo / totalNoOfTrials
    propFullMiss = fullMissNo / totalNoOfTrials
    #############################################################
    # averages of happiness + willingness
    #############################################################
    meanHappiness = totalHappiness / totalNoOfTrials
    meanWillingness = totalWillingness / totalNoOfTrials
    #############################################################
    # minimum and maximum happiness and the first trial in which they occurred.
    #############################################################
    maxHappiness = max(listHappinessScores)
    trialNoMaxHap = listHappinessScores.index(maxHappiness) + 1
    minHappiness = min(listHappinessScores)
    trialNoMinHap = listHappinessScores.index(minHappiness) + 1
    ################################################################
    #checking how many people on each date
    ################################################################
    # condition = items[0].strip('\n')
    # if 'skill' in condition:
    #     NoSkill += 1
    # elif 'luck' in condition:
    #     NoLuck += 1
    # else:
    #     NoMixed += 1
    #
    # for everyDate in listOfDates:
    #     dictDatePpts[everyDate] = 0
    #     noOfPpts = 0
    #     for eachDate in listOfDates:
    #         if eachDate == everyDate:
    #             noOfPpts += 1
    #             dictDatePpts[everyDate] = noOfPpts
    # for dates in dictDatePpts:
    #     dictPptsCondition[date] = [NoSkill, NoLuck, NoMixed]
    ##################################################################
    ##################################################################
# print(dictPptsCondition)
# print(dictDatePpts)
    # print(ipAddress,gender,propHit,propNearMiss,propFullMiss,maxHappiness,minHappiness,meanHappiness,meanWillingness)

dictPptsCondition = {}
dictDatePpts = {}
for items in fileRead:

    condition = items[0]
    dateAndTime = items[1][6:14]
    day = dateAndTime[6:8]
    month = dateAndTime[8:10]
    year = dateAndTime[10:14]
    date = day + '-' + month + '-' + year
    conditionList = [NoSkill,NoLuck,NoMixed]

    if date not in dictDatePpts:
        dictDatePpts[dateAndTime] = [0,0,0]

for items in fileRead:
    condition = items[0]

    dateAndTime = items[1][6:14]
    day = dateAndTime[6:8]
    month = dateAndTime[8:10]
    year = dateAndTime[10:14]
    date = day + '-' + month + '-' + year

    if 'skill' in condition:
        dictDatePpts[dateAndTime][0] + 1
    elif 'luck' in condition:
        dictDatePpts[dateAndTime][1] + 1
    else:
        dictDatePpts[dateAndTime][2] + 1




print(dictDatePpts)

