'''
#build a guessing game
secret_word = "seven"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses. You lose!")
else:
    print("You won!")

#for loop
for x in "Hello World":
    print(x)

car = ["Volvo", "BMW", "Vinfast"]
for index in car:
    print(index)

for i in range(10):
    print(i)

for index in range(len(car)):
    print(car[index])  #the index will run from 0 to len(car)=3, which can be for index in range(3)
                       #so it'll print car[0], car[1] and car[2]

bonus = True
for index in range(5):
    if index == 1:
        print("The second iteration")
    else:
        print("Not the second one")

#exponent function using for loop

def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num  #this demand will loop for the number depends on power_num
    return result                   #e.g: power_num = 2 -> index will run from 0 to 1, which means 2 times

print(raise_to_power(4, 3))

#2d lists and nested loops (loop in loop)

list_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(list_grid[2][0])

for row in list_grid:
    print(row) #print indices of the list

for row in list_grid:
    for column in row:
        print(column)

#build a translator
#we will translate the vowel aeiou to the letter "q"

def translation(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "q"
        else:
            translation = translation + letter
    return translation

print(translation(input("Enter a phrase: ")))

#more efficient one
def translation(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "Q"
            else:
                translation = translation + "q"
        else:
            translation = translation + letter
    return translation

print(translation(input("Enter a phrase: ")))
#try with One Two Three Four Five Six Seven Eight Nine Ten

#try/except

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input.")

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("Divided by zero")
except ValueError:
    print("Invalid input.")
'''










