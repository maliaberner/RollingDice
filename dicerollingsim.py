def my_function():
    while True:
        reply = input('Would you like to roll?')
        if reply == 'yes':
            #https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
            from random import randint
            print(randint(1, 6))
        if reply == 'no':
            break


my_function()
