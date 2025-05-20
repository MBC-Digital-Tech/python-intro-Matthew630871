# starter program week 2 - perhaps this could be a task
import webbrowser
def conversation():
    print("Welcome to my conversation program")
    print()

    sports = input("What is your favourite sport? ")
    print("Your favourite sport is " + sports + "!")
    if sports == "football":
        print("Im proud of you for liking football")

    elif sports == "rowing":
        print ("Im proud of you for liking rowing")
        webbrowser.open("https://www.bing.com/images/search?view=detailV2&ccid=zZGxTYC7&id=363E320985B4E4E8EDFE6B59B31693282D8B6FFA&thid=OIP.zZGxTYC7BFjYpdsWWCSvqgHaGO&mediaurl=https%3a%2f%2fmedia.tenor.com%2faZlLaSHkmr4AAAAC%2fcat-cat-thumbs-up.gif&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.cd91b14d80bb0458d8a5db165824afaa%3frik%3d%252bm%252bLLSiTFrNZaw%26pid%3dImgRaw%26r%3d0&exph=419&expw=498&q=thumbs+up+cat&simid=608044920712476949&FORM=IRPRST&ck=2C5AF323A7B804E64EC3F6CF5BB0FA99&selectedIndex=15&itb=0")
    elif sports == "shooting":
        print ("Im proud of you for liking shooting")
        webbrowser.open("https://tse4.mm.bing.net/th/id/OIP.r9Xw70lVfiCVoQjp1a5VRAHaJ3?w=141&h=188&c=7&r=0&o=5&cb=iwc2&dpr=1.1&pid=1.7")
    # combine the next two lines into one command.

    print("Goodbye")
conversation()
# Add command here to run the function



def ENGLAND():
    print("How many cities are there in England?")
    cit = int(input("Enter a number: "))
    if cit == 51:
        print ("correct")
    elif cit < 51:
        print ("too low")
    elif cit > 51:
        print ("too high")
ENGLAND()

def Notequal_to():
    print("try not to guess the number 1 - 100")
    num = int(input("Enter a number: "))
    if num != 99:
        print("Good work you won")
    elif num == 99:
        print("try again")
Notequal_to()