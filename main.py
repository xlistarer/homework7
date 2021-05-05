# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


'''Task 1

A simple function.

Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. The function should then print “My favorite movie is named {name}”.'''
def favorite_movie(answer):
    print('My favorite movie is named', answer)
favorite_movie(input("What is your favorite movie?"))
'''Task 2

Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital as parameters. Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. Make the function print out the values of the dictionary to make sure that it works as intended.'''
finish={ }
def make_country(name):

     dictt={name[0] :name[1]}
     return dictt
while True:
    answer=list(map(str, input('Put country and capital or no if you want stop:').split( )))
    if len(answer)==2:
        finish.update(make_country(answer))
    else:
        print("oh, goodbye! I finish at this", finish)

        break

'''

Task 3

A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  '''


def make_operation(answer):
    general = "something wrong"
    if answer[0]=='+':
        general=0
        for i in range(len(answer)-1):
            general+=answer(i+1)

    else if  answer[0] == '-':
        general = 0
        for i in range(len(answer) - 1):
            general -= answer(i + 1)
    else if answer[0] == '*':
        general = 1
        for i in range(len(answer) - 1):
            general *= answer(i + 1)
    return general
print(make_operation(list(map(str, input('Put what i need to count').split( ))))