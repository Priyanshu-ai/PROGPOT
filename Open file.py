import random
print("Here, I am your Professional Friendly Bot... You can call me PROGPOT")
list0 = ["Heya!!","Hello","Hi"]
dict1 = {"how are you?","what's up","whatsup","how are you doing","how are you","how are you???","how are you??"}
list1 = ["I am fine and you","Fine","Okay","I am fine"]
text = input(":-->>")
if "hi" in text.lower() or "hello" in text.lower():
    print(random.choice(list0))
else:
    print("Sorry, Go and learn some Manners")
text0 = input(":-->>")
if text0.lower() in dict1:
    print(random.choice(list1))
else:
    print("Leave it, First tell me How are you ")
    input(":-->>")
print("\n\n-->>>Here,I am PROGPOT and I am glad that you came here... so What you want to do ?<<<----")


