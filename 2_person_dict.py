person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] #list since we have singular names
person["pets"] = {"dog": "Fido", "cat": "Sox"} #dictionary since we have a key value pair

#print(person)

# print out the name of the second child
# seperate the childen list, name it child, then use index to single it out
namelist = person['children'][1]
print(namelist)


# use a loop to print out the names of each child
namelist = person['children']
for name in namelist:
    print(name)



# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for k,v in person['pets'].items():
    print(f'The type of pet is: {k} and the name of the pet is: {v}')