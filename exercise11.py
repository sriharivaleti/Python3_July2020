#print("How old are you?", end=' ')
age = input("How old are you?")
#print("How tall are you?", end=' ')
height = input('How tall are you?')
#print("How much do you weigh?", end=' ')
weight = input('How much do you weigh?')

#print(f'So, you\'re {age} old, {height} tall and {weight} heavy.')
print('So, you\'re {0} old, {2} tall and {1} heavy.'.format(age,weight,height))