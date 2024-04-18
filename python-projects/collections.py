# lists
lst = [10,20,30,40,50]
lst.append(5)
lst.append(6)
lst.append(7)
print(lst)

lst.remove(40)
print(lst)
lst.pop(2)
print(lst)

lst.reverse()
print(lst)
lst.sort()
print(lst)

lst[0] = 500
print(lst)

lst = lst[1:]
print(lst)

index10 = lst.index(10)
print(index10)
lst.append(20)
lst.append(20)
lst.append(20)
print(lst)
count20 = lst.count(20)
print(count20)

copy_lst = lst
print(copy_lst)
copy_lst[0] = 99
print(copy_lst)
print(lst)

new_copy = lst.copy()
print(new_copy)
new_copy[0] = 99
print(new_copy)
print(lst)

new_copy = list[:]

empty_lst = []
for val in lst:
    empty_lst.append(val)
print(empty_lst)

empty_list = [0] * 10
print(empty_list)
empty_list[0] = 10

squares = []
for i in range(1,10):
    squares.append(i*i)
print(squares)

squares = [x * x for x in range(1,10)]
print(squares)

plus_5 = [val + 5 for val in lst]
print(plus_5)

values = [34,27,95,18,36,21,64,50,77]
even_values = [x for x in values if x % 2 == 0]
print(even_values)

small_values = [val for val in lst if val < 20]
print(small_values)

# dictionaries
fav_foods = {"Kathleen": "pizza", "Hannah": "pasta", "Kush": "fries", "Yamill": "fries"}
print(fav_foods)

hff = fav_foods["Hannah"]
print(hff)

for key in fav_foods:
    print(f"{key}'s favorite food is {fav_foods[key]}")

for person, food in fav_foods.items():
    print(f"{person}'s favorite food is {food}")

if "Bob" in fav_foods:
    print(fav_foods["Bob"])
else:
    fav_foods["Bob"] = "wings"
print(fav_foods)