from random import randint
x = randint(1, 20)
count = 0

name = input("Hello! What is your name?: ")
print ("Well,",name , ",Im thinking of a number between 1 and 20")
print("You have five guesses.")

while True:
    n = int(input("Take a Guess: "))
    count += 1
    if n > x:
        print("Your guess was too high")
    if n < x:
        print("your guess was too low")
    if n == x:
        print("Good Job!,", name, "you guessed my number in", count, "guesses")
        break
    if count == 5:
        print("Nope. The number I was thinking of was", x)
        quit()
