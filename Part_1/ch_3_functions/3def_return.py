# when using def() and return together, you can specify return values based on the value input 
# a return statement should consist of: 
# 1. the return keyword and
# 2. the value or expression the function should return 

# the below imports the random module (which is one one of the built in Python libraries)
# then the get_answer is defined
# random then produces a random integet within the set parameters, and depeding on the value in answer_number, produces the fortune string

import random 
def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Ask again later'

r = random.randint(1,5)
fortune = get_answer(r)
print(fortune) 

# this could also be written as | print(getAnswer(random.randint(1, 9)))