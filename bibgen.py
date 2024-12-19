print("Hello! How are you feeling? \n Happy - Sad - Angry")
mood = input("Type here: ")

if mood == "happy" or mood == "Happy":
    print("Go, eat your bread with joy, and drink your wine with a merry heart, for God has already approved what you do.\n - Ecclesiastes 9:7")
    
elif mood == "sad" or mood == "Sad":
    print("The LORD is near to the brokenhearted And saves those who are crushed in spirit.\n - Psalm 34:18")
    
elif mood == "angry" or mood == "Angry":
    print("Be angry and do not sin. Don’t let the sun go down on your anger, and don’t give the devil an opportunity.\n - Ephesians 4:26")
    
else:
    print("Invalid entry - please type happy, sad, or angry")
    