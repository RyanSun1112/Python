# file = open("file.txt", "w")
# file.write("more content")
# file.close()




with open("file.txt", "w") as write_file:

    write_file.write("hello\n")
    write_file.write("hello    hello \n")

with open("file.txt", "a") as write_file:

    write_file.write("hello\n")
    write_file.write("hello    hello \n")

with open("file.txt" "r") as read_file:
    for line in read_file:
        print(line)

    print(read_file.readline())
    print(read_file.readlines())
