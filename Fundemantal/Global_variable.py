cool = 300

def cool2():
    global cool
    cool = 400
    print ("cool =", cool)

print(cool)
cool2()
print(cool)