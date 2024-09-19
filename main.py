import random
print("Hangman Game!")
f = open("words.txt", "r")
words = f.read().split()
f.close()
word = random.choice(words)
length = len(word)
score = 0
num_of_tries = 0
guessed_word = [*"_" * length]
guessed_letters = []
used_word=word # to keep the original word

while num_of_tries < 11:
    print("Guessed word:",guessed_word)
    guess = input("Enter a letter: ")
    if guess in guessed_letters:
        print("You have already guessed this letter!")
        continue
    guessed_letters.append(guess)
    if guess in word:
        i=word.count(guess)
        for j in range(i):# if the letter is repeated in the word
            index = used_word.index(guess)
            guessed_word[index] = guess
            used_word = used_word[:index] + "_" + used_word[index+1:]
            score += 1

    else:
        num_of_tries += 1
        print("Wrong guess! Number of tries left:",11-num_of_tries)
    if score == length:
        print("You won!")
        break
    if num_of_tries == 11:
        print("You lost!")
        break
print("The word was:",word)

