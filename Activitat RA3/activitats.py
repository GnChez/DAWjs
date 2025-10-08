# 7.9.3
def uses_only(word, available):
    for letter in word:
        if(letter not in available):
            return False
    return True

    """Checks whether a word uses only the available letters.
    
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    >>> uses_only('watermelon', 'wtrmaelon')
    True
    >>> uses_only('orange', 'ranger')
    False
    """
    return None
print("7.9.3")
print(uses_only("banana", "ban"))
print(uses_only('apple', 'apl'))
print(uses_only('watermelon', 'wtrmaelon'))
print(uses_only('orange', 'ranger'))

# 7.9.4
def uses_all(word, required):
    for letter in required:
        if(letter not in word):
            return False
    return True
    """Checks whether a word uses all required letters.
    
    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    """
    return None
print("7.9.4")
print(uses_all("banana", "ban"))
print(uses_all('apple', 'api'))
print(uses_all('watermelon', 'wtrmaelon'))
print(uses_all('orange', 'rng'))

#9.15.2
def is_anagram(first_word, second_word):
    first_ordered = sorted(list(first_word))
    second_ordered = sorted(list(second_word))
    return True if(first_ordered== second_ordered) else False

print("9.15.2")
print(is_anagram("hola","alho"))


#9.15.3
def is_palindrome(first_word, second_word):
    reversed_word = "".join(reversed(second_word))
    return True if (first_word == reversed_word) else False

print("9.15.3")
print(is_palindrome("hola","aloh"))


#9.15.4
def reverse_sentence(sentence):
    separeted_sentence = sentence.split(" ")
    return " ".join(list(reversed(separeted_sentence)))

print("9.15.4")
print(reverse_sentence("Hola mundo estoy vivo"))


#9.15.5
def total_length(sentences):
    total_letters = 0
    for word in sentences:
        total_letters += len(word)
    return total_letters

print("9.15.5")
print(total_length(["hola","mundo muerto"]))

#11.11.2
def append_number(tupla:tuple, value):
    list_modify = list(tupla)
    list_modify[1].append(value)
    dic = {str(num):0 for num in list_modify}
    return dic

list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)
print(append_number(t, 6))

#11.11.3
def shift_word(word, shift):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = range(len(letters))
    letter_map = dict(zip(letters, numbers))
    limit = len(letter_map)
    for i in letter_map.keys():
        letter_map[f'{i}'] = letter_map[f'{i}']+shift if (letter_map[f'{i}']+shift<limit) else (shift-1)
    print(letter_map)

shift_word("1",2)