zoo = ("Opossum", "Chicken", "Duck", "Wolf", "Dog", "Fox", "Raccon", "Cow", "Zebra", "Hamster")
print(zoo.index("Duck"))

animal_to_find = "Chicken"
if animal_to_find in zoo:
    print(f"{animal_to_find} is on zoo")

(a, b, c, d, e, f, g, h, i, j) = zoo

print(f"{i}")
zoo = list(zoo)

zoo.extend(["Cat", "Crabby", "Fish"])
zoo  = tuple(zoo)
print(zoo)