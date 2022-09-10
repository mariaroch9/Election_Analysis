counties = ["Arapahoe","Denver","Jefferson"]
if counties[1]=="Denver":
    print(counties[1])

counties= ["Arapahoe", "Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list")
else:
    print("El Paso is not in the list")    

for county in counties:
    print(county)

numbers=[0,1,2,3,4,5]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties [i])

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("..", "Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

   # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print each row in the CSV file.
for row in file_reader:
    print(row)
