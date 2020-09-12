# print("Starting Analysis...")
# # How many votes did you get
# my_votes = int(input("How many votes did you get in the election? "))
# #Total votes in the election
# total_votes = int(input("how many total votes in the election? "))
# # percentage votes
# percentage_votes = (my_votes/total_votes)*100
# print("I received " + str(percentage_votes)+"% votes in the election")
# counties = ['Arapahoe', 'Denver', 'Jefferson']
# if counties[0] == 'Denver':
#     print(counties[0])
# else:
#     print('No Bueno')
# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
# #     print("Open the windows.")
# counties = ["Arapahoe","Denver","Jefferson"]
# if 'Arapahoe' or 'El Paso' in counties:
#     print("They are in there")
# else:
#     print("They are in not there")
# x = 0
# while x <=5:    
#     print(x)
#     x +=1
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for key,value in counties_dict.items():
#     print(key,"county has", value, "registered voters.") 
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#     print(county_dict['county'])
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100 :.2f}% of the total votes.")

print(message_to_candidate)