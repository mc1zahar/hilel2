input_str = input()

elements = input_str.split('*')

name = elements[0]
birthdate = elements[1]
deathdate = elements[2]

birth_year = int(birthdate[:4])
death_year = int(deathdate[:4])
age = death_year - birth_year

print(f"Name: {name}")
print(f"Age: {age} years")
