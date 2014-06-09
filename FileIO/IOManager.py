"""This scrip controls both th input and output to text files and GDBM stores"""
__author__ = 'Nicholas Branfield'

import dbm

keys = list()
names = list()


def read_text(file_name, split):
    """reads in txt file (file_name) and uses split to datetime how to divide each line"""
    global keys, names
    with open(file_name, 'r') as f:
        for line in f:
            raw = line.split(split)
            keys.append(raw[0])
            names.append(raw[1])
    f.close()


def first_15():
    """print out first 15 values'"""
    print("##Frist 15 records:##")
    for i in range(15):
        print(keys[i] + '\t' + names[i])


def last_15():
    """print out last 15 values'"""
    print("##last 15 records:##")
    for i in range(15):
        print(keys[len(keys) - 1 - i] + '\t' + names[len(names) -1 - i])

print("##Reading in text file##")

read_text("lab3Input.txt", ', ')

while True:
    order = input("Please enter in a sort operator (asc or desc):")
    if order in ["asc", "desc"]:
        break
    else:
        print("Invaild entry detected - ONLY asc or desc allowed")

print("#Sorting text file data##")

if(order == "asc"):
    keys, names = (list(t) for t in zip(*sorted(zip(keys, names))))
else:
    keys, names = (list(t) for t in zip(*sorted(zip(keys, names), reverse=True)))

print("##Stroing sorted data into GDBM##")

db = dbm.open('StoreDB', 'c')

for i in range(len(keys)):
    db[keys[i]] = names[i]

keys = list()
names = list()

for key in db:
    keys.append(key.decode())
    names.append(db[key].decode())

db.close()

first_15()

last_15()

print("##Output GDBM to text file##")

f = open("lab3Output.txt", "w")
for i in range(len(keys)):
    f.write(keys[i] + '\t' + names[i])
f.close()

keys = list()
names = list()

print("##Reading in text out file##")

read_text("lab3Output.txt", " ")

first_15()

last_15()








