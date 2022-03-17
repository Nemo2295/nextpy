import functools
import string
import time
import winsound
from gtts import gTTS
import os
import base64
from tkinter import *
from PIL import ImageTk, Image


# exercise 1.1.2

def double(letter):
    return str(letter) * 2


def double_letter(my_str):
    return "".join(list(map(double, my_str)))


print(double_letter("python"))  # 'ppyytthhoonn'
print(double_letter("we are the champions!"))  # 'wwee  aarree  tthhee  cchhaammppiioonnss!!'


# exercise 1.1.3

def is_divided_by_four(num):
    return num % 4 == 0


def four_dividers(number):
    return list(filter(is_divided_by_four, range(1, number)))


print(four_dividers(9))  # [4,8]
print(four_dividers(3))  # []


# exercise 1.1.4

def add(a, b):
    return int(a) + int(b)


def sum_of_digits(number):
    return functools.reduce(add, str(number))


print(sum_of_digits(1234))


# exercise 1.3.1

def intersection(list_1, list_2):
    return list(set([x for x in list_1 if x in list_2]))


if __name__ == '__main__':
    print(intersection([1, 2, 3, 4], [8, 3, 9]))
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))


# exercise 1.3.2

def is_prime(number):  # works correctly only for numbers larger than 4
    return str(number) + " is prime number --> " + str(
        True not in list(set([True if number % num == 0 else False for num in range(3, number, 2)])))


# exercise 1.3.3

def is_funny(string_1):  # works only for not empty string
    return False not in set([True if char == "a" or char == "h" else False for char in set(string_1)])


# exercise 1.3.4

def break_password(cypher_text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    password_1 = ""
    for char in cypher_text:
        if char in abc:
            index = abc.find(char) + 2
            password_1 += abc[index]
        else:
            password_1 += char
    return password_1


password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"

print(break_password(password))  # unlock with the code: nine four one two

password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"


def break_password(cypher_text):
    return "".join([(chr(ord(letter) + 2)) if letter.isalpha() else letter for letter in cypher_text])


print(break_password(password))


# exercise 1.5

def longest_name(file_path):
    with open(file_path, "r") as file_text:  # Temporarily open a file and read the content
        return sorted(file_text.readlines(), key=len)[-1]
        # file_text.readlines() --> Content extraction from file to a list of strings
        # sorted creates a new list in which all objects are sorted by the length of their chars, from short to long
        # sorted [-1] returns the last object in the list which has the most chars


def count_chars_in_file_text(file_path):
    with open(file_path, "r") as file_text:  # Temporarily open a file and read the content
        return len("".join(file_text.readlines()).replace("\n", ""))
        # file_text.readlines() --> Content extraction from file to a list of strings
        # the list of string from text includes "\n" in the end of each line and therefore in the end pf each string
        # .replace("\n", "")) --> cleans the string from the unnecessary chars
        # "".join --> convert the list of string to one long string
        # len --> count the amount of chars in the string, which was the value needed for this exercise


def print_shortest_names_1(file_path):
    with open(file_path, "r") as file_text:  # Temporarily open a file and read the content
        sorted_list = sorted(file_text.readlines(), key=len)
        shortest_name_length = sorted_list[0]
        for name in sorted_list:
            if len(name) <= len(shortest_name_length):
                print(name)
        return ""


def print_shortest_names_2(file_path):
    with open(file_path, "r") as file_text:
        sorted_list = sorted(file_text.readlines(), key=len)
        return [print(name) for name in sorted_list if len(name) <= len(sorted_list[0])]


def write_to_text():
    with open(r"C:\Users\dorit\Desktop\לומדים פייתון\names.txt", "r") as file_text:
        list_of_names = (("".join(file_text.readlines())).split())
        length_of_songs = "\n".join(list([str(len(name)) for name in list_of_names]))
    with open(r"C:\Users\dorit\Desktop\לומדים פייתון\names.txt", "w") as file_text:
        file_text.write(length_of_songs)


def write_to_text_2():
    with open(r"C:\Users\dorit\Desktop\לומדים פייתון\names.txt", "r") as file_text:
        list_of_names = (("".join(file_text.readlines())).split())
    with open(r"C:\Users\dorit\Desktop\לומדים פייתון\names.txt", "w") as file_text:
        file_text.write(("\n".join(list([str(len(name)) for name in list_of_names]))))


def choose_song_by_length():
    user_input = int(input("please enter length of a name:"))
    with open(r"C:\Users\dorit\Desktop\לומדים פייתון\names.txt", "r") as file_text:
        list_of_names = (("".join(file_text.readlines())).split())
        return [print(name) for name in list_of_names if len(name) == user_input]


if __name__ == '__main__':
    print(longest_name(r"C:\Users\dorit\Desktop\לומדים פייתון\names.txt"))
    print(count_chars_in_file_text(r"C:\Users\dorit\Desktop\לומדים פייתון\names.txt"))
    print(print_shortest_names_1(r"C:\Users\dorit\Desktop\לומדים פייתון\names.txt"))
    print(print_shortest_names_2(r"C:\Users\dorit\Desktop\לומדים פייתון\names.txt"))
    print(choose_song_by_length())
    print(write_to_text())
    print(write_to_text_2())


# exercise 2.2.2

class Octopus:

    def __init__(self, ):
        self.age = 1

    def birthday(self, ):
        self.age += 1

    def get_age(self, ):
        print("the age of the animal is", self.age)


def main():
    paul_der_krake = Octopus()  # famous Octopus who predicted the results of soccer matches in the 2010 world cup
    kraken = Octopus()  # mythical giant sea monster from scandinavian folklore
    kraken.birthday()
    paul_der_krake.get_age()
    kraken.get_age()


main()


# exercise 2.3.3

class Octopus:
    counter = 0

    def __init__(self, name="Octavio", ):
        self._age = 1
        self._name = name
        Octopus.counter += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        print("the age of the animal is", self._age)

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        print("the new name of the animal is", self._name)


def main():
    octopus = Octopus()
    kraken = Octopus("kraken")
    octopus.get_name()
    kraken.get_name()
    kraken.set_name("kraken_2")
    kraken.get_name()
    print(Octopus.counter)


main()


# exercise 2.3.4

class Pixel:

    def __init__(self):
        self._x = 0
        self._y = 0
        self._red = 0
        self._green = 0
        self._blue = 0

    def set_coordinates(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        grey_color = (int(self._red) + int(self._green) + int(self._blue)) // 3
        self._red = grey_color
        self._green = grey_color
        self._blue = grey_color

    def print_pixel_info(self):

        if self._red == 0 and self._blue == 0 and self._green > 50:
            print(str({"X": self._x, "Y": self._y, "Color": (self._red, self._green, self._blue)}) + " green")
        if self._red == 0 and self._green == 0 and self._blue > 50:
            print(str({"X": self._x, "Y": self._y, "Color": (self._red, self._green, self._blue)}) + " blue")
        if self._blue == 0 and self._green == 0 and self._red > 50:
            print(str({"X": self._x, "Y": self._y, "Color": (self._red, self._green, self._blue)}) + " red")
        else:
            print({"X": self._x, "Y": self._y, "Color": (self._red, self._green, self._blue)})


def main():
    new_pixel = Pixel()
    new_pixel.set_coordinates(5, 6)
    new_pixel._red = 250
    new_pixel._green = 0
    new_pixel._blue = 0
    new_pixel.print_pixel_info()
    new_pixel.set_grayscale()
    new_pixel.print_pixel_info()


main()


# exercise 2.4.2


class BigThing:

    def __init__(self, argument):
        self._parameter = argument

    def size(self):
        if type(self._parameter) == int:
            return self._parameter
        else:
            return len(self._parameter)


class BigCat(BigThing):  # inheritance of attributes and methods from BigThing to BigCat

    def __init__(self, argument, weight=0):
        BigThing.__init__(self, argument)
        self._weight = weight

    def size(self):
        print(super().size())
        if 0 > self._weight:
            return "wrong number is inserted"
        if 0 < self._weight < 15:
            return "ok"
        if 15 < self._weight < 20:
            return "fat"
        if self._weight > 20:
            return "very fat"


def main():
    my_thing = BigThing("balloon")
    your_thing = BigThing("999")
    print(my_thing.size())
    print(your_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


main()


#  exercise 2.5

#  exercise 2.5

class Animal:
    _zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        print(self._name)

    def is_hungry(self):
        if self._hunger > 0:
            return True
        else:
            return False

    def feed(self):
        self._hunger -= 1

    def talk(self):
        print("animal sound")


class Dog(Animal):

    def __init__(self, name, hunger=0):
        Animal.__init__(self, name, hunger)

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):

    def __init__(self, name, hunger=0):
        Animal.__init__(self, name, hunger)

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):

    def __init__(self, name, hunger=0, stink_level=6):
        Animal.__init__(self, name, hunger)
        self._stink_count = stink_level

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):

    def __init__(self, name, hunger=0):
        Animal.__init__(self, name, hunger)

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):

    def __init__(self, name, hunger=0, color="green"):
        Animal.__init__(self, name, hunger)
        self._color = color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky", 0)
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 1450)
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky_junior = Skunk("Stinky_Junior", 80)
    clair = Unicorn("clair", 80)
    mcfly = Dragon("McFly", 80)
    zoo_lst = [brownie, zelda, stinky, keith, lizzy, doggo, kitty, stinky_junior, clair, mcfly]
    for animal in zoo_lst:
        count_feeding_cycles = 0
        if animal._hunger > 0:
            while animal._hunger > 0:
                animal.feed()
                count_feeding_cycles += 1
        print(str(type(animal))[17:-2], ",", animal._name, ",",
              animal._hunger, ",", count_feeding_cycles, ",", animal._zoo_name)
        animal.talk()
        if isinstance(animal, Dog) is True:
            Dog.fetch_stick()
        if isinstance(animal, Cat) is True:
            animal.chase_laser()
        if isinstance(animal, Skunk) is True:
            animal.stink()
        if isinstance(animal, Unicorn) is True:
            animal.sing()
        if isinstance(animal, Dragon) is True:
            animal.breath_fire()


if __name__ == "__main__":
    main()


# exercise 3.2.5

def read_file(file_name):
    print("__CONTENT_START__")
    try:
        print(open(file_name, "r").read())
    except IOError:
        print("__NO_SUCH_FILE__")
    finally:
        print("__CONTENT_END__")


def main():
    file_name_1 = r"C:\Users\dorit\Desktop\לומדים פייתון\names.txt"  # correct file path
    read_file(file_name_1)
    file_name_2 = r"C:\Users\dorit\Desktop\names.txt"  # Non-existing file path
    read_file(file_name_2)


if __name__ == "__main__":
    main()


# exercise 3.3.2

class UnderAgeError(Exception):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f"{self._name} is under the age of 18. therefore he is not allowed to come to the party, in" \
               f"{18 - self._age} years he will be able to join a party like this"


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAgeError(name, age)
    except UnderAgeError:
        print(f"{name} is under the age of 18 and therefore is not allowed to come to the party, in {18 - age}"
              f" years he will be able to join a party like this.")
    else:
        print("You should send an invite to " + name)


def main():
    send_invitation("Nemo", 20)
    send_invitation("Shon", 17)


if __name__ == "__main__":
    main()


#  exercise 3.4

class UsernameTooShortError(Exception):

    def __str__(self):
        return "The username is too short"


class UsernameTooLongError(Exception):

    def __str__(self):
        return "The username is too long"


class UsernameContainsIllegalCharacterError(Exception):

    def __init__(self, illegal_char, index_of_illegal_char):
        self._illegal_char = illegal_char
        self._index_of_illegal_char = index_of_illegal_char

    def __str__(self):
        return f"The username contains an illegal character \" {self._illegal_char} \" at index " \
               f"{self._index_of_illegal_char}"


class PasswordTooShortError(Exception):

    def __str__(self):
        return "The password is too short"


class PasswordTooLongError(Exception):

    def __str__(self):
        return "The password is too long"


class PasswordMissingCharacter(Exception):

    def __str__(self):
        return "The password is missing a character"


class PasswordMissingUppercaseCharacterError(PasswordMissingCharacter):

    def __str__(self):
        return "The password is missing a character (Uppercase)"


class PasswordMissingLowercaseCharacterError(PasswordMissingCharacter):

    def __str__(self):
        return "The password is missing a character (Lowercase)"


class PasswordMissingPunctuationCharacterError(PasswordMissingCharacter):

    def __str__(self):
        return "The password is missing a character (Special)"


class PasswordMissingNumbersCharacterError(PasswordMissingCharacter):

    def __str__(self):
        return "The password is missing a character (Number Digit)"


def check_input(username, password_1):
    uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
    numbers_chars = "0123456789"
    punctuation_chars = "#$%&'()*+, -./:;<=>?@[]^`{|}~\\_"
    illegal_chars = "#$%&'()*+, -./:;<=>?@[]^`{|}~\\"
    valid_chars = "_" + lowercase_chars + uppercase_chars
    valid_chars_count = 0
    lowercase_char_count = 0
    uppercase_char_count = 0
    punctuation_char_count = 0
    numbers_char_count = 0
    try:
        if len(username) < 3:
            raise UsernameTooShortError
        elif len(username) > 16:
            raise UsernameTooLongError
        for i in username:
            if i in illegal_chars:
                index_of_illegal_char = username.find(i)
                illegal_char = i
                raise UsernameContainsIllegalCharacterError(illegal_char, index_of_illegal_char)
            elif i in valid_chars or i in numbers_chars:
                valid_chars_count += 1

        if len(password_1) < 8:
            raise PasswordTooShortError
        elif len(password_1) > 40:
            raise PasswordTooLongError

        for i in password_1:
            if i in uppercase_chars:
                uppercase_char_count += 1
            if i in lowercase_chars:
                lowercase_char_count += 1
            if i in punctuation_chars:
                punctuation_char_count += 1
            if i in numbers_chars:
                numbers_char_count += 1

        if uppercase_char_count == 0:
            raise PasswordMissingUppercaseCharacterError
        if lowercase_char_count == 0:
            raise PasswordMissingLowercaseCharacterError
        if numbers_char_count == 0:
            raise PasswordMissingNumbersCharacterError
        if punctuation_char_count == 0:
            raise PasswordMissingPunctuationCharacterError

        if valid_chars_count == len(username) and min(uppercase_char_count, lowercase_char_count, numbers_char_count,
                                                      punctuation_char_count) > 0:
            print("username and password is ok")

    except UsernameTooShortError:
        print("The username is too short")
    except UsernameTooLongError:
        print("The username is too long")
    except UsernameContainsIllegalCharacterError:
        print(f"The username contains an illegal character \"{illegal_char}\" at index {index_of_illegal_char}.")
    except PasswordTooShortError:
        print("The password is too short")
    except PasswordTooLongError:
        print("The password is too long")
    except PasswordMissingUppercaseCharacterError:
        print("The password is missing a character (Uppercase)")
    except PasswordMissingLowercaseCharacterError:
        print("The password is missing a character (Lowercase)")
    except PasswordMissingNumbersCharacterError:
        print("The password is missing a character (Number Digit)")
    except PasswordMissingPunctuationCharacterError:
        print("The password is missing a character (Special)")


def main():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")


if __name__ == "__main__":
    main()


#  exercise 4.1.2

#  solution without generators

def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    list_of_words_in_sentence = sentence.split()
    translated_sentence = ""
    for word in list_of_words_in_sentence:
        if word in words:
            translated_word = words[word]
            translated_sentence += translated_word + " "
    return translated_sentence[:-1]


#  solution with generator

def translate_with_generator(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    list_of_words_in_sentence = sentence.split()
    return " ".join(list(words[word] for word in list_of_words_in_sentence))
    # words is the dictionary, and word is the key, therefor words[word] return the value of that key (the english word)
    # list --> convert the generator type to a list
    # " ".join --> convert the list to a string


def main():
    print(translate("la gato esta en la casa"))
    print(translate_with_generator("la gato esta en la casa"))


if __name__ == "__main__":
    main()


#  exercise  4.1.3

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    if n == 1:
        return 2
    else:
        prime_numbers = (n for n in range(n + 1, n * n) if is_prime(n))
    return next(prime_numbers)


def main():
    print(first_prime_over(5))
    print(first_prime_over(11))
    print(first_prime_over(101))


if __name__ == "__main__":
    main()


#  exercise 4.3.4


def get_fibo_1(n):
    fibo_lst = [0, 1]
    for i in range(n):
        next_fibo = fibo_lst[-2] + fibo_lst[-1]
        fibo_lst.append(next_fibo)
    return fibo_lst


def get_fibo_2():
    fibo_lst = [0, 1]
    for i in range(10):
        temp_fibo_num = fibo_lst[-2] + fibo_lst[-1]
        fibo_lst.append(temp_fibo_num)
        yield temp_fibo_num


def get_fibo_3():
    for i in get_fibo_2():
        print(i)


def main():
    print(get_fibo_1(10))
    print("----------------------")
    fibo_gen = get_fibo_2()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print("----------------------")
    get_fibo_3()


if __name__ == "__main__":
    main()


#  exercise 4.4


def gen_secs():
    for sec in range(60):
        yield sec


def gen_minutes():
    for minute in range(60):
        yield minute


def gen_hours():
    for hour in range(24):
        yield hour


def gen_time():
    for x in gen_hours():
        for y in gen_minutes():
            for z in gen_secs():
                yield "%02d:%02d:%02d" % (x, y, z)


def gen_years(start=2019, end=2020):
    for year in range(start, end):
        yield year


def gen_months(start=1):
    for month in range(start, 13):
        yield month


def is_leap_year(year):
    if int(year) % 4 == 0:
        if int(year) % 100 == 0:
            if int(year) % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def gen_days(month, year, start=1):
    # days_end = days_of_month[month] if month !=2 else 28 + is_leap_year(year)
    if month == 1:
        for day in range(start, 32):
            yield day
    elif month == 2:
        if is_leap_year(year):
            for day in range(start, 30):
                yield day
        if not is_leap_year(year):
            for day in range(start, 29):
                yield day
    elif month == 3:
        for day in range(start, 32):
            yield day
    elif month == 4:
        for day in range(start, 31):
            yield day
    elif month == 5:
        for day in range(start, 32):
            yield day
    elif month == 6:
        for day in range(start, 31):
            yield day
    elif month == 7:
        for day in range(start, 32):
            yield day
    elif month == 8:
        for day in range(start, 32):
            yield day
    elif month == 9:
        for day in range(start, 31):
            yield day
    elif month == 10:
        for day in range(start, 32):
            yield day
    elif month == 11:
        for day in range(start, 31):
            yield day
    elif month == 12:
        for day in range(start, 32):
            yield day


def gen_date_1():  # dd/mm/yyyy hh:mm:ss.
    for a in gen_years(2400, 2401):
        for b in gen_months():
            for c in gen_days(b, a):
                for d in gen_time():
                    yield "%02d:%02d:%02d" % (c, b, a) + " " + d


def gen_date_2():  # dd/mm/yyyy hh:mm:ss.
    count = 0
    for a in gen_years(2400, 2401):
        for b in gen_months():
            for c in gen_days(b, a):
                for d in gen_time():
                    count += 1
                    if count % 1000000 == 0:
                        yield "%02d:%02d:%02d" % (c, b, a) + " " + d


def main():
    start = time.time()
    for date in gen_date_1():
        print(date)
    end = time.time()
    print("This function ran for" + str(end - start) + " seconds")


if __name__ == "__main__":
    main()

#  exercise 5.1.2


frequency = {"la": 220, "si": 247, "do": 261, "re": 293, "mi": 329, "fa": 349, "sol": 392}
notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
list_of_notes = notes.split("-")
list_of_notes_2 = [note.split(",") for note in list_of_notes]


def main():
    for note in list_of_notes_2:
        print(note[0], frequency[(note[0])], int(note[1]))
        winsound.Beep(frequency[(note[0])], int(note[1]))


if __name__ == "__main__":
    main()

#  exercise 5.2.2

numbers = iter(list(range(1, 101)))


def main():
    try:
        for i in numbers:
            print(i)
            next(numbers)
            next(numbers)
    except StopIteration:
        print("no more numbers for you")


if __name__ == "__main__":
    main()


#  exercise 5.2.3


def bills_options(bills_in_wallet, money_desired=100):
    list_of_combination_of_bills = []
    count_of_bills_options = 0
    for bills_quantity in range(1, len(bills_in_wallet) + 1):
        list_of_combinations = [list(combination) for combination in
                                itertools.combinations(bills_in_wallet, bills_quantity) if
                                sum(combination) == money_desired]
        for combination in list_of_combinations:
            if combination not in list_of_combination_of_bills:
                list_of_combination_of_bills.append(combination)
                count_of_bills_options += 1
    return f"there are {count_of_bills_options} combinations possible and they are {list_of_combination_of_bills}"


def main():
    bills_in_wallet = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    print(bills_options(bills_in_wallet, 100))


if __name__ == "__main__":
    main()


# exercise 5.3.2

class MusicNotes:

    def __init__(self, note_name, octave_number, frequency_1):
        self._note = note_name
        self._octave = octave_number
        self._frequency = frequency_1

    def get_note_name_and_frequency(self):
        return f"The frequency of \"{self._note}\" in the {self._octave} is {self._frequency}."


class OctaveMusicNotes:

    def __init__(self):
        self._MusicNotesList = []
        self._MusicNoteIndex = -1

    def add_music_note(self, new_music_note):
        self._MusicNotesList.append(new_music_note)

    def __iter__(self):
        return self

    def __next__(self):
        self._MusicNoteIndex += 1
        if self._MusicNoteIndex >= len(self._MusicNotesList):
            raise StopIteration()
        else:
            return self._MusicNotesList[self._MusicNoteIndex].get_note_name_and_frequency()


def main():
    music_note_list = OctaveMusicNotes()

    music_note_list.add_music_note(MusicNotes("La", "First octave", 55))
    music_note_list.add_music_note(MusicNotes("Si", "First octave", 61.74))
    music_note_list.add_music_note(MusicNotes("Do", "First octave", 65.41))
    music_note_list.add_music_note(MusicNotes("Re", "First octave", 73.42))
    music_note_list.add_music_note(MusicNotes("Mi", "First octave", 82.41))
    music_note_list.add_music_note(MusicNotes("Fa", "First octave", 87.31))
    music_note_list.add_music_note(MusicNotes("Sol", "First octave", 98))

    music_note_list.add_music_note(MusicNotes("La", "Second octave", 110))
    music_note_list.add_music_note(MusicNotes("Si", "Second octave", 123.48))
    music_note_list.add_music_note(MusicNotes("Do", "Second octave", 130.82))
    music_note_list.add_music_note(MusicNotes("Re", "Second octave", 146.84))
    music_note_list.add_music_note(MusicNotes("Mi", "Second octave", 164.82))
    music_note_list.add_music_note(MusicNotes("Fa", "Second octave", 174.62))
    music_note_list.add_music_note(MusicNotes("Sol", "Second octave", 196))

    music_note_list.add_music_note(MusicNotes("La", "Third octave", 220))
    music_note_list.add_music_note(MusicNotes("Si", "Third octave", 246.96))
    music_note_list.add_music_note(MusicNotes("Do", "Third octave", 261.64))
    music_note_list.add_music_note(MusicNotes("Re", "Third octave", 293.68))
    music_note_list.add_music_note(MusicNotes("Mi", "Third octave", 329.64))
    music_note_list.add_music_note(MusicNotes("Fa", "Third octave", 349.24))
    music_note_list.add_music_note(MusicNotes("Sol", "Third octave", 392))

    music_note_list.add_music_note(MusicNotes("La", "Fourth octave", 440))
    music_note_list.add_music_note(MusicNotes("Si", "Fourth octave", 493.92))
    music_note_list.add_music_note(MusicNotes("Do", "Fourth octave", 523.28))
    music_note_list.add_music_note(MusicNotes("Re", "Fourth octave", 587.36))
    music_note_list.add_music_note(MusicNotes("Mi", "Fourth octave", 659.28))
    music_note_list.add_music_note(MusicNotes("Fa", "Fourth octave", 698.48))
    music_note_list.add_music_note(MusicNotes("Sol", "Fourth octave", 784))

    music_note_list.add_music_note(MusicNotes("La", "Fifth octave", 880))
    music_note_list.add_music_note(MusicNotes("Si", "Fifth octave", 987.84))
    music_note_list.add_music_note(MusicNotes("Do", "Fifth octave", 1046.56))
    music_note_list.add_music_note(MusicNotes("Re", "Fifth octave", 1174.72))
    music_note_list.add_music_note(MusicNotes("Mi", "Fifth octave", 1318.56))
    music_note_list.add_music_note(MusicNotes("Fa", "Fifth octave", 1396.96))
    music_note_list.add_music_note(MusicNotes("Sol", "Fifth octave", 1568))

    for note in music_note_list:
        print(note)


if __name__ == "__main__":
    main()


# exercise 5.4 with docstring


def check_id_valid(id_number):  # This function works only when input is an int
    """
    This function checks if an Israeli ID is valid or not.
    :param id_number: given Israeli ID number from user
    :type id_number: int # but also can accept string
    :return: The function return True if the Israeli ID is valid, and False if not
    :rtype: boolean
    """
    doubled_id_number_list = [int(str(id_number)[i]) * 2 if i % 2 == 1 else int(str(id_number)[i]) for i in range(9)]
    # The line above creates a list in which every number in the ID and if he is in even index is doubled by 2, and
    # if the number is in the odd index then it just adds him to the list
    separated_digits = [int((str(number))[0]) + int((str(number))[1]) if len(str(number)) == 2 else number for
                        number in doubled_id_number_list]
    #  The line above creates a list of the sum of separated digits of every number from the list doubled_id_number_list
    if sum(separated_digits) % 10 == 0:
        return True
    else:
        return False


class IDIterator:
    """
    This class generates 10 valid Israeli ID numbers after given Israeli ID from user input
    """

    def __init__(self, id_start=100000000, id_end=999999999):
        """
        This method initialize default values of attributes for the generator
        :param id_start: The minimal possible valid value of Israeli ID
        :type id_number: int
        :param id_end: given ID number from user
        :type id_number: int
        """
        self._id = range(id_start + 1, id_end)
        # The reason for adding 1 to id_start is to make sure that the function will not return the given israeli ID
        # in 1 of the 10 new israeli ID generated
        self._id_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        """
        This is a customized iterator that return the next valid Israeli ID number
        """
        self._id_index += 1
        if self._id_index >= len(self._id):
            raise StopIteration()
        else:
            if check_id_valid(self._id[self._id_index]):
                return self._id[self._id_index]


def id_generator(id_start=100000000, id_end=999999999):
    """
    This function generates 10 valid Israeli ID numbers after given Israeli ID from user input
    :param id_start: The minimal possible valid value of Israeli ID
    :type id_start: int
    :param id_end: given ID number from user
    :type id_end: int
    :return: The function returns 10 valid ID numbers that are after the given user input ID
    :rtype: int
    """
    counter = 0
    for israeli_id in range(id_start + 1, id_end):
        # The reason for adding 1 to id_start is to make sure that the function will not return the given israeli ID
        # in 1 of the 10 new israeli ID generated
        if counter > 9:
            break
        else:
            if check_id_valid(israeli_id) and type(israeli_id) == int:
                counter += 1
                yield israeli_id


def main():
    user_id_input = input("ENTER ID:")
    user_method_input = input("Generator or Iterator? (gen/it)?")
    if user_method_input == "gen":
        for israeli_id in id_generator(int(user_id_input)):
            print(israeli_id)
    if user_method_input == "it":
        counter = 0
        for israeli_id in IDIterator(int(user_id_input)):
            if counter > 9:
                break
            else:
                if type(israeli_id) == int:
                    counter += 1
                    print(israeli_id)


if __name__ == "__main__":
    main()


# exercise 6.1.3 # You need to download and install PIL or pillow package to your computer and install them


#  from tkinter import *
#  from PIL import ImageTk, Image


def open_img():
    img = Image.open(r"C:\Users\dorit\Desktop\IMG_20191214_153205.jpeg")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(my_first_tk, image=img)
    panel.image = img
    panel.pack()


my_first_tk = Tk()
my_first_tk.geometry("350x350")
my_first_tk.title("Next.py exercise 6.1.3")
label = Label(my_first_tk, text="What is my favorite picture?")
button = Button(my_first_tk, text="click here to check out", bg="green", width=25, command=open_img)
label.pack()
button.pack()
my_first_tk.mainloop()


# exercise 6.1.4, read more here https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/

#  import base64

def main():
    base64_message = 'CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW1tfX11dLS0tLS4KICAgICAgICAgICAgICA7LS0t' \
                     'LS0tLS0tLS0tLS58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICAgIHx8ICAgLi0tW1tfX11dLS0t' \
                     'LgogICAgICAgICAgICAgIHwgICAgICAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCAgICAg' \
                     'ICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X19fX19fX19fX19fX3wvICB8ICAgICAgICAg' \
                     'ICB8fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX19fX3wvCgo= '
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print(message)


if __name__ == "__main__":
    main()


# exercise 6.2.5, this exercise is requires 3 python files

#  create a new file and name it "file_1"


class GreetingCard:

    def __init__(self):
        self._recipient = "Dana Ev"
        self._sender = "Eyal Ch"

    def greeting_msg(self):
        print(f"The sender is {self._sender},and the recipient is {self._recipient}")


#  create a new file and name it "file_2"

#  from file_1 import GreetingCard (delete "#" and copy this line to file_2)


class BirthdayCard(GreetingCard):

    def __init__(self, sender_age=0):
        GreetingCard.__init__(self)
        self._sender_age = sender_age

    def greeting_msg(self):
        super().greeting_msg()
        print(f"Happy birthday, by the way the sender age is {self._sender_age}")


#  create third file and name it main, and copy

#  from file_1 import GreetingCard. delete "#" and copy this line to main file.
#  from file_2 import BirthdayCard. delete "#" and copy this line to main file.


def main():
    first_greeting_card = GreetingCard()
    first_greeting_card.greeting_msg()
    first_birthday_card = BirthdayCard()
    first_birthday_card.greeting_msg()


if __name__ == "__main__":
    main()


#  exercise 6.3.3

#  click in the same time the button windows + r and then write cmd in command line
#  in the cmd write -> pip install gTTS
#  other option is to open pycharm and then file -> settings -> python interpreter -> + -> gTTS

#  from gtts import gTTS
#  import os


def main():
    my_text = "first time i'm using a package in next.py course"
    language = 'en'
    my_obj = gTTS(text=my_text, lang=language, slow=False)
    my_obj.save("welcome.mp3")
    os.system("welcome.mp3")


if __name__ == "__main__":
    main()


#  exercise 6.4

#  import Image

def main():
    first = (
        146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170,
        355, 169, 346, 167, 335, 170, 329, 170, 320, 170, 310, 171, 301, 173, 290,
        178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194,
        307, 191, 312, 190, 316, 190, 321, 192, 331, 193, 338, 196, 341, 197, 346,
        199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197, 383, 196, 387, 192,
        389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402,
        216, 401, 219, 397, 219, 393, 216, 390, 215, 385, 215, 379, 213, 373, 213,
        365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311,
        215, 306, 216, 296, 218, 290, 221, 283, 225, 282, 233, 284, 238, 287, 243,
        290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291, 273, 289, 278, 287,
        279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294,
        291, 296, 295, 299, 300, 301, 304, 304, 320, 305, 327, 306, 332, 307, 341,
        306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302,
        393, 324, 391, 333, 387, 328, 375, 329, 367, 329, 353, 330, 341, 331, 328,
        336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343, 269, 344, 262, 346,
        259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295,
        349, 298, 354, 293, 356, 286, 354, 279, 352, 268, 352, 257, 351, 249, 350,
        234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137,
        339, 132, 330, 122, 327, 120, 314, 116, 304, 117, 293, 118, 284, 118, 281,
        122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134, 228, 136, 221, 137,
        214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159,
        134, 157, 134, 160, 130, 170, 125, 176, 114, 176, 102, 173, 103, 172, 108,
        171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124,
        115, 120, 115, 115, 117, 113, 120, 109, 122, 102, 122, 100, 121, 95, 121,
        89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100, 130, 108,
        132, 110, 133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149,
        77, 155, 81, 162, 90, 165, 97, 167, 99, 171, 109, 171, 107, 161, 111,
        156, 113, 170, 115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259,
        136, 266, 139, 276, 143, 290, 148, 310, 151, 332, 155, 348, 156, 353, 153,
        366, 149, 379, 147, 394, 146, 399
    )
    second = (
        156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186,
        150, 179, 155, 175, 157, 168, 157, 163, 157, 159, 157, 158, 164, 159, 175,
        159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212, 147, 215, 146,
        218, 143, 220, 132, 220, 125, 217, 119, 209, 116, 196, 115, 185, 114, 172,
        114, 167, 112, 161, 109, 165, 107, 170, 99, 171, 97, 167, 89, 164, 81,
        162, 77, 155, 81, 148, 87, 140, 96, 138, 105, 141, 110, 136, 111, 126,
        113, 129, 118, 117, 128, 114, 137, 115, 146, 114, 155, 115, 158, 121, 157,
        128, 156, 134, 157, 136, 156, 136
    )
    all_dots = first + second
    new_image = Image.new("RGB", (640, 480))
    for i in range(0, len(all_dots), 2):
        x = all_dots[i]
        y = all_dots[i + 1]
        new_image.putpixel((x, y), (255, 255, 255, 255))

    new_image.save("Next.py exercise 6.4.png")
    new_image.show()


if __name__ == "__main__":
    main()
