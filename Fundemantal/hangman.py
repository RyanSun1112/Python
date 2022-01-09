


import requests, random

def underscore(random_word):
    for i in range(len(random_word)):
        print("▔" , end = " ")
    print(" ")

url = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(url)
words = response.text.splitlines()

print("Welcome to hangman, please input minimum length of word. You have two hints. Input hint for a hint")
minimum = input()
hangman = [
    " O",
    " |",
   "/|\ ",
   " |",
   " |",
   "/ \ ",

]
hints_counter = 0
hangman_output = []
int_minimum = int(minimum)
random_word = random.choice(words) 
while len(random_word) < int_minimum:
    random_word = random.choice(words) 
counter = 0
output_list = []
for i in range(len(random_word)):
    output_list.append(" ")
input_list = [""]
while counter < 6:
    print("input letter:", end = " ") 
    input_list = input()
    if input_list in random_word:
        v = 0
        for v in range(len(random_word)):
            if random_word[v] == input_list:
                output_list[v] = input_list
    elif input_list == "hint" and hints_counter != 2:
        hints_counter+=1
        for i in range(len(random_word)):
            if " " in output_list[i]:
                output_list[i]=random_word[i]
                break 
    else:  
        hangman_output.append(hangman[counter])
        counter+=1
    print(' '.join(output_list)) 
    underscore(random_word)
    if " " not in output_list:
        print("You won")
        exit()
    for i in range(len(hangman_output)):
        print(hangman_output[i])
    if hints_counter == 2:
        print("You ran out of hints")

print("You lost")
print("The word was " + random_word)

# with open("words.txt", "w") as write_file:
#     write_file.write(response.text)

# with open("words.txt", "r") as read_file:
#     for line in read_file:
#         print(line)