#this function returns the square of a number
def square(n):
    print(n*n)

square(9)

#this function checks whether a number is even or not
def is_even(n):
    if n%2==0:
        print(True)
    if n%2==1:
        print(False)

is_even(9)

#this function returns a greeting using a default argument
def greet(name, greeting = "Hello"):
    print(greeting + " " + name)

greet("Mabel")

#this function cleans a text, stripping preceding and trailing spaces
#and converts to uppercase
def clean_name(tt):
    cleaned = tt.strip().upper()
    print(cleaned)

clean_name(" aBA WILson ")

#this function accepts a list and returns the min,
#max and average as a dictionary
def summarise(n):
    #initialise variables for output
    max_val=float('-inf')
    min_val=float('inf')
    avg_val=float()

    #looping through the list and 
    #comparing values to determine min or max
    for i in n:
        if i>max_val:
            max_val=i

        if i<min_val:
            min_val=i

    avg_val=sum(n)/len(n)

    #create dictionary
    dicttt = {
        "min": min_val,
        "max": max_val,
        "average": avg_val
    }
    return dicttt

#create list    
num = [6,7,8,9,3,16,45,86,65,364]

result = summarise(num)
print(result)

import csv

def read_csv(path):
    with open(path, newline="") as f:
        reader=csv.DictReader(f)
        return list(reader)

rows = read_csv("score.csv")
print(rows)
print(rows[0]["name"])