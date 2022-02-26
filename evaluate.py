import random, os, sys
os.system('clear') #start fresh

#-------------  Global variable declarations --------------
turn = 0  #starts the game with turn counter at 0
is_correct = False #true means the answer has been guessed
wordlength = 5 #default
qwerty_one = "   q w e r t y u i o p"
qwerty_two = "    a s d f g h j k l"
qwerty_three = "      z x c v b n m"
the_guess_list = []
answer_index = 1000000
library = []
dictionary_file = ""
#----------------------------------------------------------

#argument parser
# - stage 1: python wordle.py <wordlength>
# - stage 2: python wordle.py <wordlength> <gamelength>
def arg_parser():
    global wordlength
    global dictionary_file
    if len(sys.argv) > 1:
        print "Found argument"
        if sys.argv[1] == "6":
            wordlength = 6
            print "Wordlength for game is: " + str(wordlength)
    dictionary_file = "dictionary" + str(wordlength) + ".txt"

#build a list variable within game based on dictionary file
def build_library():
    global library
    with open(dictionary_file) as libfile:
        for line in libfile:
            word_item = line.rstrip("\r\n").lower().split(",")
            library.append(word_item)
    libfile.close()

#find a valid answer within the library
def get_answer(library):
    global answer_index
    i = 0 #try to find a valid answer 10 times
    while i < 10:
        #print "Try #" + str(i+1) + " to find a valid answer"
        answer_index = random.randint(0, len(library)-1)
        #format for library: [['1','AFTER'], ... , ['0','ZORRO']] where 1 is valid answer, 0 is not
        #print "Found: " + library[answer_index][1]
        if library[answer_index][0] == "1":
            answer = library[answer_index][1]
            return answer
        i += 1
    print "Did not find a valid answer in " + str(i) + " attempts - quitting."
    quit()

def print_logo():
    with open("gnomefarts_logo.txt") as logo:
        for line in logo:
            print line,
    print "\n\n"
    logo.close()

#function to update visual qwerty keyboard as letters are guessed
def update_the_unguessed(word):
    global qwerty_one
    global qwerty_two
    global qwerty_three
    for letter in word:
        if letter in qwerty_one:
            qwerty_one = qwerty_one.replace(letter, "_")
        elif letter in qwerty_two:
            qwerty_two = qwerty_two.replace(letter, "_")
        elif letter in qwerty_three:
            qwerty_three = qwerty_three.replace(letter, "_")

#function to print the visual qwerty keyboard of unguessed letters
def print_the_unguessed():
    print "\nUnguessed:\n"
    print qwerty_one
    print qwerty_two
    print qwerty_three

def print_word(word):
    format_word = "  | "
    i = 0
    while i < len(word):
        format_word = format_word + word[i] + " | "
        i += 1
    print format_word, #removed line break from this print

def print_empty_word():
    empty_word = ""
    i = 0
    while i < wordlength:
        empty_word = empty_word + "_"
        i += 1
    print_word(empty_word)
    print ""

def print_guess_history(guess_list):
    for guess in guess_list:
        print_word(compare_word(answer, guess))
        print guess

#function gets player feedback on validity/reasonableness of word and update dictionary file if not
def approve_word(answer_index):
    global library
    answer = library[answer_index]
    approved = ""
    while (approved != "y" and approved != "n"):
        approved = raw_input("Was this a reasonable word? (y/n): ").lower()
    if approved == 'n':
        print "Thank you for the feedback, removing [" + answer[1] + "] from potential answers list."
        answer[0] = "0" #remove word from library list object
        #remove word from dictionary file
        with open(dictionary_file) as libfile:
            data = libfile.readlines()
        data[answer_index] = "0," + answer[1].upper() + "\r\n"
        with open(dictionary_file, 'w') as libfile:
            libfile.writelines(data)
        libfile.close()
    else:
        print "Acknowledged, keeping [" + answer[1] + "] in list."

#function that determines correctness of guess word letters and formats output
def compare_word(answer, guess):
    output_string = ""
    i = 0
    while i < wordlength:
        if guess[i] in answer:
            if guess[i] == answer[i]:
                #print "hit!"
                output_string += guess[i]
            else:
                #print "partial hit!"
                output_string += guess[i].upper()
        else:
            #print "miss!"
            output_string += "_"
        i += 1
    return output_string

#function that takes player guess input, forces correctness/validity of guess
def guess_word():
    guess = "0"
    while (not guess.isalpha() or len(guess) != wordlength):
        guess = raw_input("Guess a word: ").lower()
        if not any(guess in sublib for sublib in library) and guess.isalpha() and len(guess) == wordlength:
            print "Your guess, [" + guess + "] was not found in the dictionary."
            guess = "0"
    the_guess_list.append(guess)
    update_the_unguessed(guess)

#function for game turn loop
def take_turn():
    global turn
    global is_correct

    # Toggle this turn to clear screen each turn #
    if turn != 0:
        os.system('clear')

    print_guess_history(the_guess_list)
    print_empty_word()
    print_the_unguessed()
    print "\n - Turn", turn + 1, " -"
    guess_word()

    if the_guess_list[-1] == answer:
        is_correct = True
        print "\nHooray you are a winnar!!!\n"

    turn += 1

    if turn == (wordlength + 1):
        os.system('clear')
        print_guess_history(the_guess_list)
    return 

#---------  Game logic ----------------
arg_parser()
build_library()
answer = get_answer(library)
#print_logo()

#while ( turn < ( wordlength + 1 ) and is_correct == False ):	
#    take_turn()

#print_word(answer)
print answer

print "\n"
approve_word(answer_index)