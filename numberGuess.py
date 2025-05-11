import random

while True:
    compNum = random.randint(1,100)
    attempts = 1
    UserGuessList = []
    print("\n🎯 New Game Started! Guess the number between 1 and 100.")
    while attempts <= 5:
        userNum = int(input("Enter a number between 1 and 100: "))
        if userNum < 1 or userNum > 100:
            print("Please enter a number between 1 and 100.")
            continue
        UserGuessList.append(userNum)
        if userNum == compNum: 
                print("🎉 Congratulation! You guessed right.")
                print("You guessed the number in ", attempts, "attempts.")
                print("Your guesses were: ", UserGuessList)
                break
        elif userNum < compNum:
                print("Your guess is lower than the number.")
        else:
                print("Your guess is higher than the number.")
        attempts += 1
        if attempts > 5:
            print("❌ You have used all your attempts.")
            print("The number was: ", compNum)
            print("Your guesses were: ", UserGuessList)
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break