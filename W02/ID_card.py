print ('Please enter the following information:')
print ()
name = input ('First name: ')
surname = input ('Last name: ')
email = input ('Email address: ')
phone = input ('Phone number: ')
job = input ('Job title: ')
number = input ('ID Number: ')
hair = input ('Hair color: ')
eyes = input ('Eye color: ')
month = input ('Starting month: ')
training = input ('Have you completed advanced training (yes/no)? ')
print ()
print ('The ID Card is:')
print ('---------------------------------------')
print (f'{surname.upper()}, {name.capitalize()}')
print (job.capitalize())
print (f'ID: {number}')
print ()
print (email.lower())
print (phone)
print ()
print (f'Hair: {hair.capitalize():15} Eyes: {eyes.capitalize()}')
print (f'Month: {month.capitalize():14} Training: {training.upper()}')
print ('---------------------------------------')