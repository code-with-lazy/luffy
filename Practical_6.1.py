import random
def question():
    for i in range(1, 26):
        number = random.randint(0, 100)
        dic[i] = number
        if number == 1:
            dic[i] = "Lion"
            print(f"Lion is placed at {i} Number Cage")       
    if 'Lion' not in dic.values():
        dic[25] = 'Lion'
        print("Lion is at 25th Number cage") 


dic = {} # empty dictionary
question() # main logic
print(dic) # printing the resulting dictionary 






