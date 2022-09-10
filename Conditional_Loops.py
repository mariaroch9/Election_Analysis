
#How mny votes did you get?
my_votes=int(input("How mny votes did you get?"))

#  Total votes in the election
total_votes=int(input("#  What is the total votes in the election?"))

# Calculate the percentage of votes you received.
percentage_votes=(my_votes/total_votes) *100

print("I received"+ " "+ str(percentage_votes)+ "% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1]=="Denver":
    print(counties[1])


temperature=(int(input("What is the outside temperature?")))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows")


#what is your test score

score=int(input("What is your test score?"))

if score>=90:
    print("Your grade is A!")
else:
    if score>=80:
        print("Your grade is B")
    else:
        if score>=70:
            print("Your grade is C")
        else:
            if score>=60:
                print("Your grade is D")
            else:
                print("Your grade is F")

# what is your test score? using elif

score=int(input("What is your score?"))

if score>=90:
    print("Your grade is A")
elif score>=80:
    print("Your grade is B")
elif score>=70:
    print("Your grade is C")
elif score>=60:
    print("Your grade is D")
else:
    print("Your grade is F")        















