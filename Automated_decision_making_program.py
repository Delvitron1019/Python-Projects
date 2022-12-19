from random import choice

options=[]

no=int(input('Please enter number of choices: '))
for i in range(no):
    opt=input('Enter a choice: ')
    options.append(opt)

print('you should: ' + choice(options))