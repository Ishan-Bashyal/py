#Accept the age of 4 people and display the youngest one

first = int(input("Enter age of First Person: "))
second = int(input("Enter age of Second Person: "))
third = int(input("Enter age of Third Person: "))
fourth = int(input("Enter age of Fourth Person: "))

if first <= second and first <= third and first <= fourth:
    print("First person is the Youngest")
elif second <= third and second <= fourth and second <= first:
    print("Second person is the Youngest")
elif third <= second and third <= first and third <= fourth:
    print("Third person is the Youngest")
else:
    print("Fourth is the Youngest")