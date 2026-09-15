#survey results (each list represents a participant's choices)
survey_results = [
    ["Python","JavaScript","C++"], #Participant 1
    ["Python","JavaScript","C#"], #Participant 2
    ["Python","Java"], #Participant 3
    ["Python","C++","JavaScript"], #Participant 4
    ["Python","JavaScript","C++","Java"], #Participant 5
]
#1.Identify the languages that were chosen by all participants.
#2.Find the the languages that were only chosen by a participant.
#3. Determine the number of unique languages mentioned in the survey.
#4.List the languages that were chosen by exactly two participants.
#5.Find participants who have the exact same set of favorite languaes.

choices_sets= [set(p) for p in survey_results]
print(choices_sets)

#1.Identify the languages that were chosen by all participants.
choices_sets= [set(p) for p in survey_results]
common_languages = set.intersection(*choices_sets)
print("1. languages chosen by all participants: ",common_languages)

#2.Find the the languages that were only chosen by a participant.
choices_sets= [set(p) for p in survey_results]



#3. Determine the number of unique languages mentioned in the survey.
unique_partic_count=len(survey_results)
print("3. Number of unique languages :",unique_partic_count)
#output: 5


#4.List the languages that were chosen by exactly two participants.




#5.Find participants who have the exact same set of favorite languaes.
