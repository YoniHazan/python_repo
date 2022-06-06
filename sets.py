# main difference between sets and lists are:
# sets are not ordered and have unique values
my_set = {"January", "February", "March"}

for elemet in my_set:
    print(elemet)

my_set.add("April")
print(my_set)

my_set.remove("January")
print(my_set)

my_list = ["January", "February", "March"]
my_list.append("February")
my_list.remove("February")
print(my_list)