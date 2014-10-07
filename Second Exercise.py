#Max Louis
#Boolean Exercise 2
#24/09/14

team1 = input("What is name of a team.")
team2 = input("What is name of another team.")

team1Score = int(input("What was the score of {0}?".format(team1)))
team2Score = int(input("What was the score of {0}?".format(team2)))



if team1Score < team2Score:
    team2Score = 3
    team1Score = 0

if team1Score == team2Score:
    team2Score = 1
    team1Score = 1

if team1Score < team2Score:
    team1Score = 3
    team2Score = 0

print("Here is the scoreboard:")
print(" Team            Score")
print("-----------------------")
print("")
print(team1,"       ",team1Score)
print(team2,"       ",team2Score)


