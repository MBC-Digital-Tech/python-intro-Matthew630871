def quiz():
    print("Welcome to the quiz!")
    print("Please answer the following questions:")

    print("1. What is the largest canyon in the world?")
    print("a) The Great Wall of China")
    print("b) The Grand Canyon")
    print("c) The gulf of Mexico")
    print("d) The Arizona Desert")
    answer1 = input("Your answer: ")
    if answer1.lower() == "b":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is b) The Grand Canyon.")

    print("2. Canada shares the world's longest national border with what country?")
    print("a) The United States")
    print("b) Mexico")
    print("c) Russia")
    print("d) Alaska")
    answer2 = input("Your answer: ")
    if answer2.lower() == "a":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is a) The United States.")

    print("3. What is the largest hot desert in the world?")
    print("a) The Sahara Desert")
    print("b) The Arabian Desert")
    print("c) The Gobi Desert")
    print("d) The Kalahari Desert")
    answer3 = input("Your answer: ")
    if answer3.lower() == "a":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is a) The Sahara Desert.")

    print("4. What is the smallest country in the world?")
    print("a) Vatican City")
    print("b) Monaco")
    print("c) Nauru")
    print("d) Tuvalu")
    answer4 = input("Your answer: ")
    if answer4.lower() == "a":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is a) Vatican City.")

    print("5. What continent covers all four hemispheres?")
    print("a) Africa")
    print("b) Asia")
    print("c) North America")
    print("d) South America")
    answer5 = input("Your answer: ")
    if answer5.lower() == "a":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is a) North America.")

    print("Good work on the quiz. Goodbye!")

quiz()