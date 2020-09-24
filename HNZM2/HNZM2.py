######Assessment1_Parts 1 & 2#########
##################################################
##################################################

# opening all of the files at once
# used listdir to get a list of the file names only
from os import listdir
files = listdir('.')

# ordering all the files to make sure that they stay in the original order
files_sorted = sorted(files)
files_1 = []

# creating a loop to read all the files and then appending them to a list
# Also filtering out the python files so that it only reads the csv.
for b in files_sorted:
    if 'results' in b:
        read = open(b, 'r')
        files_read = read.readlines()
        files_1.append(files_read)



participant_IDs = [] # creating a new list to hold all the information for each participant
participant = [] # need to create a list for participant IDs to filter out repeated identifiers

# Gathering info per participant file using a large loop to make sure that it gathers from every participant
# Also included in this is part 2 which is making sure that the participant files are not repeated twice

for info in files_1:
    participants = []
    participant_ID = info[2]
    if participant_ID not in participant_IDs: # This will put in the unique IDs without repeating
        participant_IDs.append(participant_ID)
        if participant_ID in participant_IDs: # Once that happens only after the unique ID is added and now matches does the code continue

# This should eliminate any repeating participants

# Getting each participant condition
            condition = 0
            if 'skill' in info[0].lower():
                condition = 'skill'
                participants.append(condition)
            elif 'luck' in info[0].lower():
                condition = 'luck'
                participants.append(condition)
            elif 'mixed' in info[0].lower():
                condition = 'mixed'
                participants.append(condition)

# Separating name, age, and gender and then appending
            name_age_gender = info[3].split(',')
            name = name_age_gender[0]
            age = name_age_gender[1].lower()
            gender = name_age_gender[2].lower()
            participants.append(name)
            participants.append(age)
            if 'female' in gender:
                participants.append(2)
            elif 'male' in gender:
                participants.append(1)
            else:
                participants.append(0)

            trial_data = []
# creating a new list for remaining lines of data which is just the trial information
# makes it easier in my head to edit within the loop
            for i in range(5, len(info)):
                hit = 0
                nearMiss = 0
                fullMiss = 0
                happiness_hit = 0
                happiness_nearMiss = 0
                happiness_fullMiss = 0
                willingness_hit = 0
                willingness_nearMiss = 0
                willingness_fullMiss = 0
                trial_data.append(info[i])
                happiness_list = []
                for lines in trial_data:
                    # this is because we want to look at each line within i --> creating another loop lets me do that
                    split_lines = lines.split(',') # then I can split the lines and take out the score I want using the index
                    if 'hit' in lines.lower(): # I sometimes used lower to standardize my data and avoid mistakes
                        hit = hit + 1
                        happiness_hit = happiness_hit + int(split_lines[7])
                        happiness_list.append(int(split_lines[7]))
                        willingness_hit = willingness_hit + int(split_lines[8])
                    elif 'nearmiss' in lines.lower():
                        nearMiss = nearMiss + 1
                        happiness_nearMiss = happiness_nearMiss + int(split_lines[7])
                        happiness_list.append(int(split_lines[7]))
                        willingness_nearMiss = willingness_nearMiss + int(split_lines[8])
                    elif 'fullmiss' in lines.lower():
                        fullMiss = fullMiss + 1
                        happiness_fullMiss = happiness_fullMiss + int(split_lines[7])
                        happiness_list.append(int(split_lines[7]))
                        willingness_fullMiss = willingness_fullMiss + int(split_lines[8])
                max_happiness = max(happiness_list)
                min_happiness = min(happiness_list)
                max_trial_number = happiness_list.index(max_happiness) + 1
                min_trial_number = happiness_list.index(min_happiness) + 1

# appending all of the filtered trial information into correct part of list and for each participant
            participants.append(hit/(len(info[5:])))  # we divide by this length because that is the total number of trials for each particiapnt
            participants.append(nearMiss/(len(info[5:])))
            participants.append(fullMiss/(len(info[5:])))
            participants.append(happiness_hit / hit)
            participants.append(happiness_nearMiss / nearMiss) # divide by each number i.e of nearMiss/hit/fullMiss to find the average
            participants.append(happiness_fullMiss / fullMiss)
            participants.append(willingness_hit / hit)
            participants.append(willingness_nearMiss / nearMiss)
            participants.append(willingness_fullMiss / fullMiss)
            participants.append(max_happiness)
            participants.append(max_trial_number)
            participants.append(min_happiness)
            participants.append(min_trial_number)

        participant.append(participants)

################################################################
################################################################
# writing the actual CSV file

    final_file = open("Assessment1.csv",'w')

# creating the headers just to make it look a little nicer

    final_file.write('Condition, Name, Age, Gender, '
                     'Proportion of Hits, Proportion of Near Misses, Proportion of Full Misses, '
                     'Mean_happinesss_hits, Mean_happiness_nearMiss, Mean_happiness_fullMiss, '
                     'Mean_willingness_hits,''Mean_willingness_nearMiss, Mean_willingness_fullMiss,'
                     'Max_happiness, Max_trial_number,Min_happiness,Min_trial_number''\n')
    final_file.close()
# appending the new lists of lists created for each participant with relevant information
# using strip function since I turned the items in my listoflists into a string

final_file2 = open("Assessment1.csv",'a')
for new_line in participant:
    final_file2.write(str(new_line).replace("'",'').strip('[]') + '\n')
final_file2.close()


################################################################
################################################################
#Part 3 - Creating a new CSV File For Dates
################################################################


date_dictionary = {}
# changing each date to fit the correct format by stripping certain parts and then adding in dashes
for d in files_1:
    date = d[1]
    date = date.split('Date:')[1]
    date = date.strip('Date').strip('')
    date = date[:3] + '-' + date[3:5] + '-' + date[5:9]
    if date not in date_dictionary:
# making sure that the dates are not added into the dictionary more than once.
# creating a list and putting place holders for the information per date later
        date_dictionary[date] = [0,0,0,0,0]

# using the same loop over again to maintain d
# then looping and adding in the information for each date

for d in files_1:
    date = d[1]
    date = date.split('Date:')[1]
    date = date.strip('Date:').strip('')
    date = date[:3] + '-' + date[3:5] + '-' + date[5:9]

    date_dictionary[date][0] += 1  # this is to count the total number of participants
    participants_per_date = 0
    if 'skill' in d[0]:
        date_dictionary[date][1] += 1 # counting how many participants per date were in the 'skill' condition
    if 'luck' in d[0]:
        date_dictionary[date][2] += 1  # counting how many participants per date were in the 'luck' condition
    if 'mixed' in d[0]:
        date_dictionary[date][3] += 1  # counting how many participants per date were in the 'mixed' condition

    trials = 0
    for t in d[5:]:
        if 'trial' in t:
            trials += 1
    date_dictionary[date][4] += trials  # counting how many total trials there were per date


for date in date_dictionary:
    date_dictionary[date][4] /= date_dictionary[date][0]
    date_dictionary[date][4] = f"{date_dictionary[date][4]:.2f}" # making sure that it only goes to two decimal points


# we divide through a loop (so that it does it for every date) by the number of participants
# for that specific date because each participant basically represents a numeral of that day
# this gives us the average of trials per day



######################################################
######################################################
# Actually writing the csv file for dates
# creating headers for the file, again I think it looks nice :)
date_file = open("date_file.csv","w")
date_file.write("Dates, Number of Participants, Participants_per_Skill, "
                "Participants_per_Luck, Participants_per_Mixed, Average_Number_Trials_PerDate"'\n')

# create a loop to write each item in the date_dictionary

for write in date_dictionary:
    date_file = open("date_file.csv","a")
    date_file.write(str(write) + ',' + str(date_dictionary[write]).strip('[]').replace("'"," ") + '\n')

    # I used strip and replace a lot to get rid of some of the extrenuous looking items in the file
    # i.e. it looks a little bit prettier after :)
