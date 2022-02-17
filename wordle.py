import random

#answer = "pants"
#library = ["pants", "siren", "dumpy", "clear", "proxy", "knoll", "moist", "junky", "burst", "octal", "rinse", "human","after", "pinto", "roach", "login", "under", "purse", "uncle", "crime", "couch", "flute", "lotus", "whale"]
qwerty_one = "   q w e r t y u i o p"
qwerty_two = "    a s d f g h j k l"
qwerty_three = "      z x c v b n m"
the_guesses = []
wordlength = 5 #new variable that will later be chosen value by player; removed hardcoded references to '5'

library = []

with open("fiveletters.txt") as libfile:
    for line in libfile:
        library.append( line.rstrip( "\n" ).lower() )
libfile.close()

def get_answer(library):
    index = random.randint(0, len(library)-1)
    answer = library[index]
    return answer

def the_unguessed(word):
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
    print qwerty_one
    print qwerty_two
    print qwerty_three

def print_word(word):
    #format_word = "[" + word[0] + "][" + word[1] + "][" + word[2] + "][" + word[3] + "][" + word[4] + "]"
    #return format_word
    format_word = ""
    i = 0;
    while i < len(word):
        format_word = format_word + "[" + word[i] + "]"
        i += 1
    print "   ",
    print format_word
	
def compare_word(answer, guess):
    output_string = ""
    i = 0;
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
            output_string += "?"
        i += 1
    return output_string


def guess_word():
    guess = "0"
    #print (not guess.isalpha())
    while (not guess.isalpha() or len(guess) != wordlength):
        guess = raw_input("Guess a word: ")
    print_word(compare_word(answer, guess.lower()))
    print "\nUnguessed:\n"
    the_unguessed(guess)
    #guess = raw_input("Guess a word: ")
    #print print_word(compare_word(answer, guess.lower()))
	
answer = get_answer(library)
#print answer

print_word("?????")
turn = 0
while ( turn < ( wordlength + 1 ) ):
    print "\nTurn", turn + 1
    guess_word()
    turn += 1

print "The answer was", answer