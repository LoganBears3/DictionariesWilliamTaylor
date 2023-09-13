import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}


'''
print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(len(phonebook))

mydict = {}
mydict = dict(m=8, n=8)

print(mydict)

phone = phonebook['Chris']
print(phone)

print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()


name = 'Chris'

if name in phonebook:
    print(phonebook([name]))
else:
    print(f'{name} is not in the phonebook')





print()
print('****  end section 2 ********')
print()


print(phonebook)

phonebook['Joe'] = '555-4564'
phonebook['Chris'] = '555-4565'

print(phonebook)




print()
print('*****  start section 3 - edit/append dictionary ********')
print()





print()
print('*****  end section 3 ********')
print()





'''
print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)
del phonebook['Chris']
print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:
    print(f'The key is {key} and the value is {phonebook[key]}')

for v in phonebook.values():
    print(v)

for item in phonebook.items():
    print(item)

for k,v in phonebook.items():
    print(f'the key is {k} and the item is {v}')


print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()


phone = phonebook.get('chris', ' NOT FOUND')
print(phone)
phonebook.clear()
print(phonebook)



print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

print(phonebook)
phone = phonebook.pop('chris', 'NOT FOUND')

print(phone)
print(phonebook)

print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

keyvalue = phonebook.popitem()

#only pops out the last item, how do we get a random key value pair out of a dictionary
print(phonebook)





print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

listofkeys = list(phonebook)
randomkey = random.choice(listofkeys)

print(randomkey)
print(phonebook[randomkey])

print()
print('*****  end section 9 ********')
print()

print(randomkey, phonebook[randomkey])






