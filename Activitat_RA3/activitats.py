# 7.9.3
#Esta funcion itera sobre cada letra de la palabra dada y revisa si esta presenta en el "string" de letras disponibles. 
#Devuelve True si la palabra usa solo letras desponibles, caso contrario devuelve False.
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
print("_____________________________________")
print("---------------7.9.3---------------")
print(uses_only("banana", "ban"))
print(uses_only('apple', 'apl'))
print(uses_only('watermelon', 'wtrmaelon'))
print(uses_only('orange', 'ranger'))

# 7.9.4
#Esta funcion itera sobre cada letra del "string" de letras requeridas y revisa si esta presenta en la palabra dada. 
#Devuelve True si la palabra usa todas letras requeridas, caso contrario devuelve False.
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
print("_____________________________________")
print("---------------7.9.4---------------")
print(uses_all("banana", "ban"))
print(uses_all('apple', 'api'))
print(uses_all('watermelon', 'wtrmaelon'))
print(uses_all('orange', 'rng'))

#9.15.2
#Esta funcion revisa si dos palabras son anagramas. 
#Devuelve True si lo son, caso contrario devuelve False.
def is_anagram(first_word, second_word):
    first_ordered = sorted(list(first_word))
    second_ordered = sorted(list(second_word))
    return True if(first_ordered== second_ordered) else False

print("_____________________________________")
print("---------------9.15.2---------------")
print(is_anagram("hola","alho"))


#9.15.3
#Esta funcion revisa si dos palabras son palindromos. 
#Devuelve True si lo son, caso contrario devuelve False.
def is_palindrome(first_word, second_word):
    reversed_word = "".join(reversed(second_word))
    return True if (first_word == reversed_word) else False

print("_____________________________________")
print("---------------9.15.3---------------")
print(is_palindrome("hola","aloh"))


#9.15.4
#Esta funcion gira las palabras de una frase. 
#Devuelve la frase girada.
def reverse_sentence(sentence):
    separeted_sentence = sentence.split(" ")
    return " ".join(list(reversed(separeted_sentence)))

print("_____________________________________")
print("---------------9.15.4---------------")
print(reverse_sentence("Hola mundo estoy vivo"))


#9.15.5
#Esta funcion cuenta las letras de cada palabra de una lista de palabras. 
#Devuelve la cantidad de letras.
def total_length(sentences):
    total_letters = 0
    for word in sentences:
        total_letters += len(word)
    return total_letters

print("_____________________________________")
print("---------------9.15.5---------------")
print(total_length(["hola","mundo muerto"]))

#11.11.2
#Esta funcion añade un número al segundo valor de una tupla de listas. 
#Devuelve la tupla.
def append_number(tupla:tuple, value):
    list_modify = list(tupla)
    list_modify[1].append(value)
    dic = {str(num):0 for num in list_modify}
    return dic


list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)
print("_____________________________________")
print("---------------11.11.2---------------")
print(append_number(t, 6))


#11.11.3
#Esta funcion devolverá una nueva palabra dado el valor de cambio que le pasemos
def shift_word(word, shift):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = range(len(letters))
    letter_map = dict(zip(letters, numbers))
    limit = len(letter_map)
    palabra =""
    for char in word:
        if char in letter_map:
            new_letra = letters[((letter_map[f'{char}']+shift) % limit)]
            palabra += new_letra

    return palabra

print("_____________________________________")
print("---------------11.11.3---------------")
print(shift_word("melon",16))

#10.11.3
#Esta funcion revisa si la palabra dado tiene letras duplicadas. 
#Devuelve True si las tiene, caso contrario devuelve False.
def has_duplicates(word):
    word_list = set(word)
    return True if (len(word_list)< len(word)) else False

print("_____________________________________")
print("---------------10.11.3---------------")
print(has_duplicates("hola"))

#10.11.4
#Esta funcion devolverá las claves de un diccionario en las cuales su valor sea >1. 
def find_repeats(char_dic):
    keys_gt_1 = []
    for val in char_dic:
        if char_dic[val] > 1:
            keys_gt_1.append(val)
    return keys_gt_1

print("_____________________________________")
print("---------------10.11.4---------------")
print(find_repeats({"a":1, "b":2, "c":4, "d":0}))


#10.11.5
#Esta funcion devuelve un diccionario que será la union de los dos pasados como parametro
def add_counter(first_dic, second_dic):
    new_dic = {}
    for char in first_dic:
        if char not in new_dic:
            new_dic[char] = first_dic[char]
        else:
            new_dic[char] += first_dic[char]

    for char in second_dic:
        if char not in new_dic:
            new_dic[char] = second_dic[char]
        else:
            new_dic[char] += second_dic[char]
    return new_dic

print("_____________________________________")
print("---------------10.11.5---------------")
print(add_counter({"a":1, "b":2, "c":4, "d":4},{"t":1, "o":2, "c":4, "a":1}))
