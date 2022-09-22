my_dict = dict({1:"Apple"})

my_dict1 = dict([(1, "apple"), (2, "ball")])

print(list(my_dict1.items()))
print(list(my_dict1.keys()))
print(list(my_dict1.values()))

print(my_dict.get("name"))
my_dict["name"] = "person1"

my_dict.pop("name")
print(my_dict)

del my_dict[1]
print(my_dict)

my_dict1.clear()
print(my_dict1)

nums_dict = {1: "one", 3: "three", 2: "two"}
print(sorted(nums_dict)) #keys are returned by default
sorted_dict = dict(sorted(nums_dict.items()))
print(sorted_dict)


# set

my_set = {'quiz'}
print(my_set)
my_set1 = set('quiz')
print(my_set1)

set1 = {1, 2, 3, 4}
set1.add(5)
set1.update([7, 8, 9])
print(set1)

# can iterate cann't slice

for i in set1:
    print(i, end=" ")

print()
print(sorted(set1))
