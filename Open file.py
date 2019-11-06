import random
print("Here, I am your Professional Friendly Bot... You can call me PROGPOT")
list0 = ["Heya!!","Hello","Hi"]
dict1 = {"how are you?","what's up","whatsup","how are you doing","how are you","how are you???","how are you??"}
text = input(":-->>")
list1 = ["i am fine.","Fine","Doing Good"]
if "hi" in text.lower() or "hello" in text.lower():
    print(random.choice(list0))
    text0 = input(":-->>")
    if text0.lower() in dict1:
        print(random.choice(list1))
        print("\n\n-->>>Here,I am PROGPOT and I am glad that you came here... so What you want to do ?<<<----")
    else:
        print("Leave it, First tell me How are you ")
        input(":-->>")
        print("\n\n-->>>Here,I am PROGPOT and I am glad that you came here... so What you want to do ?<<<----")
else:
    print("\n\n-->>>Here,I am PROGPOT and I am glad that you came here... so What you want to do ?<<<----")
    ask0 = input("What You want to know?")
    print(ask0)




