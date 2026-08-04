score1 = int(input("Enter the score for test 1: "))
score2 = int(input("Enter the score for test 2: "))
score3 = int(input("Enter the score for test 3: "))
average_score = (score1 + score2 + score3) / 3
print("Your average score is:", average_score)
if average_score > 95:
    print("Congratulations!")
    print("That is a great score!")