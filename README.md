Deliverable 3 Instructions
Use your repository README to write your analysis of Deliverables 1 and 2. The analysis should contain the following:


# Overview of Election Audit: Explain the purpose of this election audit 

To assist a Colorado board of elections employee, Tom, in an election audit of the tabulated results for a U.S. congressional precinct in Colorado. There are three primary voting methods that will be considered, mail-in ballots, punch cards, and direct recording electronic, or DRE, counting machines. Mail-in ballots are typically hand counted at the central office. Punch cards are collected and then fed into a machine that tabulates vote totals and sends the results to the central office. Finally, memory cards from DRE counting machines are sent to the central office and read by a computer.
Altogether, the votes cast by these three methods will determine the final election results. 
The election commission has requested the following data to complete the audit. 
	The voter turnout for each county
	The percentage of votes from each county out of the total count
	The county with the highest turnout
Traditionally, this analysis was prepared in Excel, this is the first time we’ll be using Python to automate the process. If this audit is done successfully with Python, the code will be replicated to audit not only other congressional districts, but also senatorial districts, and local elections.


## 1. Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.
### To find how many votes were cast in this congressional election the first thing I did was to initialize the total vote counter to zero. This will add each vote to get the final tally. The variables county list, county votes, candidate options and candidate votes were defined to help with the analysis. 
### Total Votes: 369,711
```

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}


```
### The next steps were to be able to identify the candidate winning in terms of highest votes count as well as percentage. They also wanted a similar break-up of the county winning with respect to vote count and percentage of votes. 
```
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_county = ""
winning_count = 0
winning_percentage = 0


```
### To determine the number of votes and the percentage of the total votes each candidate received, I used conditional loops. Since this was the part where each row of the spreadsheet was to be scanned to find the total number of votes and the total percentage of votes. 

 ### Names of candidates along with the total votes they received and the percentage of the votes received:

Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)

-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
```

# For each row in the CSV file.
for row in reader:

        # Add to the total vote count
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage #removed .get before (candidate name)
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    #print(winning_candidate_summary)
    print(winning_candidate_summary)


```
### Similarly, to determine the county with the highest number of votes I used conditional loops here. This conditional statement checked each row to determine the winning County. 
### County Names, Votes percentage and total number of votes
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
Largest County Turnout: Denver
```

# 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.

        if county_name not in county_list:
            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


# 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count. #removed .get
        votes = county_votes[county_name]
    
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes)/ float(total_votes) *100
        county_results= (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

         # 6d: Print the county results to the terminal.
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_county = county_name
            winning_percentage = vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_turnout = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(largest_county_turnout)
    
    # Track the winning candidate, vote count and percentage
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0


        






























```

## The details of the winning candidate are below.

-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%

![image](https://user-images.githubusercontent.com/111670866/190222686-27769140-3e4f-48c0-90fa-e3e29c9e488f.png)

 

 
```
## 2. Election-Audit Summary: 
Using Python over Excel has increased our efficiency tremendously. The process of counting votes is now a breeze. Additionally, we can tailor the search to extract the exact data that we need. Here, we analysed the data of all the candidates and the counties. We established the total votes and votes percentage received by each candidate and by each county. 

This Python code is versatile enough and can be replicated across other elections with minor modifications.  If we were to consider using this code for other elections we could do so by changing the variables used. The counties could be changed to states for the state-level elections. Furthermore, we could gather additional information on many other variables to include demographic details such as age, gender, income levels, etc. These details could vary on the purpose for which the analysis is conducted. 

Instead of an election audit, if we were to generate the analysis to devise our promotional campaign then we could collect and analyse data with respect to other variables such as demographics, opposition parties etc. 

The basic syntax of using conditional statements would remain the same. We could vary the number of iterations based on the number of variables used. 

Using Python is highly recommended not only as a measure to improve efficiency and productivity but to get a distinct picture and generate a compelling story taking into account several perspectives. 


