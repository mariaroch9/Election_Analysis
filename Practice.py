print("Hello World")

counties=["Arapahoe", "Denver", "Jefferson"]

counties
print(counties)

print(counties[0])

print(counties[-1])

print(len(counties))
print(counties[0:2])

counties.append("El Paso")

counties.insert(2, "El Paso")
print(counties)
counties.remove("El Paso")
print(len(counties))
print(counties)

counties.pop(3)
print(counties)

counties[2]= "El Paso"

print(counties)

counties_tuple=("Arapahoe", "Denver", "Jefferson")

print(counties_tuple)
print(len(counties_tuple))

print(counties_tuple[1])

counties_dict={}

counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())

print(counties_dict.get("Denver"))

print(counties_dict["Arapahoe"])

voting_data=[]

voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Jefferson", "registered_voters":432438})

print(voting_data)
voting_data.insert(0,{"county":"El Paso", "registered_voters":461129})

voting_data.remove({"county":"Arapahoe", "registered_voters":422829})

voting_data.insert(3,{"county":"Denver", "registered_voters":463353})

voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.pop(1)
print(voting_data)

for county, voters in counties_dict.items():
    print(f"{county } county has {voters} registered voters.")

candidate_votes=int(input("How many votes did the candidate get?"))
total_votes=int(input("What were the total number of votes in the election?"))
message_to_candidate=(
    f"You receied {candidate_votes} total number of votes."
    f"The total number of votes in the election was {total_votes}."
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
