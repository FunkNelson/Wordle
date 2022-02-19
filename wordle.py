import random
import os
os.system('clear')

#answer = "pants"
#library = ["pants", "siren", "dumpy", "clear", "proxy", "knoll", "moist", "junky", "burst", "octal", "rinse", "human","after", "pinto", "roach", "login", "under", "purse", "uncle", "crime", "couch", "flute", "lotus", "whale"]
qwerty_one = "   q w e r t y u i o p"
qwerty_two = "    a s d f g h j k l"
qwerty_three = "      z x c v b n m"
the_guess_list = []
wordlength = 5 #new variable that will later be chosen value by player; removed hardcoded references to '5'
turn = 0  #starts the game with turn counter at 0
is_correct = False #true means the answer has been guessed

library = []

with open("fiveletters.txt") as libfile:
    for line in libfile:
        library.append( line.rstrip( "\n" ).lower() )
libfile.close()

def get_answer(library):
    index = random.randint(0, len(library)-1)
    answer = library[index]
    return answer

def print_logo():
    with open("gnomefarts_logo.txt") as logo:
        for line in logo:
            print line,
    print "\n\n"
    logo.close()

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

def print_the_unguessed():
    print "\nUnguessed:\n"
    print qwerty_one
    print qwerty_two
    print qwerty_three

def print_word(word):
    #format_word = "[" + word[0] + "][" + word[1] + "][" + word[2] + "][" + word[3] + "][" + word[4] + "]"
    #return format_word
    #format_word = ""
    format_word = "  | "
    i = 0
    while i < len(word):
        #format_word = format_word + "[" + word[i] + "]"
        format_word = format_word + word[i] + " | "
        i += 1
    print format_word,   #removed line break from this print

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

def guess_word():
    guess = "0"
    while (not guess.isalpha() or len(guess) != wordlength):
        guess = raw_input("Guess a word: ").lower()	
    the_guess_list.append(guess)
    update_the_unguessed(guess)

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

    if the_guess_list[-1].strip() == answer.strip():
        is_correct = True
        print "\nHooray you are a winnar!!!\n"

    turn += 1

    if turn == 6:
        os.system('clear')
        print_guess_history(the_guess_list)
    return 

#---------  Game logic ----------------

answer = get_answer(library)
print_logo()

while ( turn < ( wordlength + 1 ) and is_correct == False ):	
    take_turn()

print_word(answer.strip())	
print "\n"
