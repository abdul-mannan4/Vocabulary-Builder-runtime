import random
import os
import time
def newword(vocab):
    word=input("Enter the word you want to add: ")
    meaning1=input("Enter the meaning of word: ")
    senetence1=input("Enter the sentence made by word: ")
    difficulty1=input("Enter the Difficulty level: ")
    vocab.update({
        word : {"meaning": meaning1, "sentence": senetence1,"difficulty": difficulty1}})
    time.sleep(3)
    os.system('cls')
    print(">>>Do you want to Add more words\n1. Yes\n2. No")
    choice2=int(input("Enter your choice: "))
    if(choice2==1):
        newword(vocab)
    elif(choice2==2):
        os.system('cls')
        return "back"
    else:
        print("Invalid Input.Enter Corret Number")
    

def viewwords(vocab):
    print("==============================================")
    print(">>>>>>>>>>>View th whole vocabulary<<<<<<<<<<<")
    for word,detail in vocab.items():
        print("==========================================")
        print(f"Word: {word}")
        print(f"Meaning: {detail['meaning']}")
        print(f"Sentence: {detail['sentence']}")
        print(f"Difficulty: {detail['difficulty']}")
        print("==========================================")
    
    press =int(input("Press 1 to go Back: "))
    if press==1:
        os.system('cls')
        return 
    else:
        print("Enter Correct Key")

def quizyou(vocab):
    print(">>>>>>>>>>>>>>>Quiz Yourself<<<<<<<<<<<<<<<<<")
    print(">>>>>>>>>>>>>>>Suggest word on the basis of meaning<<<<<<<<<<<<<<<<\n\n")
    randomwod=random.choice(list(vocab.keys()))
    meaning1=vocab[randomwod]['meaning']
    print("Meaning is: ",meaning1)
    choice1=input("Enter the Correct Word: ")
    if choice1.lower()==randomwod.lower():
        print("Your answer is correct")
    else:
        print(f"Your answer is incorrect\nCorrect Answer is: {randomwod}")
    time.sleep(4)
    os.system('cls')
    print(">>>Do you want to play again\n1. Play Again\n2. Return back")
    choice2=int(input("Enter your choice: "))
    if(choice2==1):
        quizyou(vocab)
    elif(choice2==2):
        os.system('cls')
        return "back"
    else:
        print("Invalid Input.Enter Corret Number")
    


vocab = {
    "eager": {
        "meaning": "Very excited or enthusiastic",
        "sentence": "She was eager to learn Python.",
        "difficulty": "Easy"
    },
    "Resilient":{
        "meaning": "Recover Quickly",
        "sentence": "A resilient student never give up",
        "difficulty": "Medium"
    }

}


def main():
    while True:
        print("=====================================================")
        print(">>>>>>>>>>>>Small Vocabulary Builder<<<<<<<<<<<<<<<<<")
        print("=====================================================")
        print("                 1. Add New Word")
        print("                 2. View all Words")
        print("                 3. Quiz Yourself")
        print("                 4. Exit")

        choice=int(input("Enter Your Choice: "))
        if choice==1:
            os.system('cls')
            newword(vocab)
            result = newword(vocab)
            if result == "back":
                continue
        elif choice==2:
            os.system('cls')
            viewwords(vocab)
        elif choice ==3:
            os.system('cls')
            result = quizyou(vocab)
            if result == "back":
                continue 
        elif choice==4:
            os.system('cls')
            print("Good to see you Later!")
            break
main()