import requests,random
minimum = input()

int_minimum = int(minimum)

with open("words.txt", "r") as read_file:
     words = read_file.readlines()


random_word = random.choice(words) 
while len(random_word) < int_minimum:
    random_word = random.choice(words) 


print(random_word)