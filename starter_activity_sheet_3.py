# starter program week 3 - perhaps this could be a task

def cooking():
    print("Meal planner")
    print()

    # change these to your favourite meals
    print("1. Mac and cheese")
    print("2. cheese toastie")
    print("3. Chicken Burger")
    print("4. Takeaways")
    # add one more meal here
    print()
    # adapt the next line to add in the 4.
    print("Which of these meals is your favourite? (1, 2, 3, 4) ")
    # combine the line above and below into one command that accepts an integer instead of a string.
    answer = int(input())
    # adapt the if else block to include the fourth meal and compares integers instead of strings.
    if answer == 1:
        print("Mac and cheese coming up")
    elif answer == 2:
        print("cheese toastie coming up")
    elif answer == 3:
        print("Chicken Burger coming up!")
    elif answer == 4:
        print("Takeaways coming up!")
    print("enjoy")

# add a command to run the function above.
cooking()
