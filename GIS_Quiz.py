#I made this to practice 2D collections. Dec 19 2024.
#Test your knowledge!

print("GIS QUIZ GAME")

questions = ("What does the acronym G.I.S. stand for? ",
             "Which of the following might be considered metadata? ",
             "What are the dimensions of a point feature?")

options = (("A. Geologic Information Structure",
            "B. Geographic Information System",
            "C. Geographic Informatic Structure",
            "D. Geologic Inherent Structure"),
           ("A. Map projection",
            "B. Coordinate System",
            "C. Data Author",
            "D. All of the above"),
           ("A. 0", "B. 1", "C. 5", "D. 10"),)

answers = ("B", "D", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
            score += 1
            print("CORRECT! :)")
    else:
            print("INCORRECT... :(")
            print(f"The correct answer is {answers[question_num]}")
    question_num += 1

print("--------------------------------")
print("------------RESULTS-----------")
print("--------------------------------")

print("Answers: ", end = "")
for answer in answers:
    print(answer, end = " ")
print()

print("Guesses: ", end = "")
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")
