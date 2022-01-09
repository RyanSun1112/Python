letters_list = ["aaaaa","bbbbbbb","cccccc"]

print(letters_list[1])
print(letters_list[0:3])
print(letters_list[-1])

print(len(letters_list))

letters_list.append("ddddddd")
print(letters_list)

letters_list.insert(3,"eeeee")
print(letters_list)

letters_list[4] = "rrrrrr"

print(letters_list)

letters_list.remove("rrrrrr")

print(letters_list)

letters_list.pop()
print(letters_list)
letters_list.pop(2)
print(letters_list)

letters_list.clear()

for i in range(len(letters_list)):
    print(letters_list[i])

for letter in letters_list:
    print(letter)

new_letters_list = letters_list

# new_letters_list[0] = "AAAAAAA"


New_letters_list = letters_list.copy()


list_1 = [43,324,123123,3223,43,65]

list_1.sort()
print(list_1)
list_1.sort(reverse = True)

list_2 = sorted(list_1)
print(list_1)
print(list_2)


list_3 = list_1 + list_2
print(list_3)

list_1.extend(list_2)
print(list_1)

list_1.append(list_2)
print(list_1)


if "aaaaa" in letters_list :
    print("a is in the list")