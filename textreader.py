
#def read_file():
#    
#    with open("words.txt") as file:
#        count_the = 0
#        for line in file:
#            for word in line.strip().split():
#                count_the += 1
#        print(count_the)

def at_least():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if len(word) >= 20:
                    print(word)

def has_no_e(word):
    if 'e' not in word:
        return True
    else:
        return False

def no_e():
    with open("words.txt") as file:
        noe = 0
        num_words = 0
        for line in file:
            for word in line.strip().split():
                num_words += 1
                if not has_no_e(word):
                  noe += 1
        print((noe/num_words)*100)
                          

if __name__ == "__main__":
    #read_file()
    #at_least()
    no_e()