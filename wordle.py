import random

#answer = "pants"
#library = ["pants", "siren", "dumpy", "clear", "proxy", "knoll", "moist", "junky", "burst", "octal", "rinse", "human","after", "pinto", "roach", "login", "under", "purse", "uncle", "crime", "couch", "flute", "lotus", "whale"]
library = []

with open("fiveletters.txt") as libfile:
    for line in libfile:
        library.append( line.rstrip( "\n" ).lower() )
libfile.close()

def get_answer(library):
	index = random.randint(0, len(library)-1)
	answer = library[index]
	return answer

def print_word(word):
	format_word = "[" + word[0] + "][" + word[1] + "][" + word[2] + "][" + word[3] + "][" + word[4] + "]"
	return format_word

	
def compare_word(answer, guess):
    output_string = ""
    i = 0;
    while i < 5:
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
	guess = raw_input("Guess a word: ")
	print print_word(compare_word(answer, guess.lower()))
	
answer = get_answer(library)
#print answer

print print_word("?????")

turn = 0
while (turn < 6):
	print "Turn", turn + 1
	guess_word()
	turn += 1

print "The answer was", answer