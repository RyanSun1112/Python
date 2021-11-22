


import requests, random


url = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(url)

words = response.text.splitlines()

minimum = input()

int_minimum = int(minimum)
random_word = random.choice(words) 
while len(random_word) < int_minimum:
    random_word = random.choice(words) 

print(random_word)
# with open("words.txt", "w") as write_file:
#     write_file.write(response.text)

# with open("words.txt", "r") as read_file:
#     for line in read_file:
#         print(line)