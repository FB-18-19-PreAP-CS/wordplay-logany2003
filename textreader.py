
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
    ''' finds words that do not have the letter e
    >>> has_no_e('potato')
    True
    >>> has_no_e('bruther')
    False
    >>> has_no_e('jacob')
    True
    
    '''
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
        c = (noe/num_words)*100
        print(f"{c} % of the words do not have e.")

def avoids(word, forbid_lett):
    for letter in forbid_lett:
        if letter.lower() in word.lower():
            return False
    return True
    
def count_avoids():
    forbid_letters = input("Enter a list of forbidden letters ")
    avoid = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if avoids(word, forbid_letters):
                    avoid += 1
    print(avoid)

def uses_only(word, letters):
    for letter in word:
        if letter.lower() not in letters.lower():
            return False
    return True

def words_with_only(letters):
    uses = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_only(word, letters):
                    uses += 1
    print(uses)
            
def uses_all(word, letters):
    for letter in letters:
        if letter.lower() not in word.lower():
            return False
    return True

def how_many_uses_all(letters):
    uses_lett = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_all(word, letters):
                    uses_lett += 1
    print(uses_lett)

def is_abecedarian(word):
    for i in range(len(word)):
        for j in word[i:]:
            if word[i].lower() > j.lower():
                return False
    return True

def count_abecedarian():
    count = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if is_abecedarian(word):
                    count += 1
    print(count)

if __name__ == "__main__":
    #read_file()
    #at_least()
    #no_e()
    #count_avoids()
    #words_with_only('abcdefg')
    #how_many_uses_all('aeiou')
    count_abecedarian()