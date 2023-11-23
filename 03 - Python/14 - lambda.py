people = [
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Cho", "house":"Ravenclaw"},
    {"name":"Draco", "house":"Slytherin"}
]

# The two statement bellow will return an exception because python doesn't now how to sort list of dict
# We need to be specific of what key it should use to sort

# people.sort()
# print(people)

# The code bellow will work, but we can siplify f() using lambda

# def f(person):
#     return person["house"]

# people.sort(key = f)

# print(people)

people.sort(key = lambda person: person["name"])
print(people)