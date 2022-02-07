import re
#
#
# def first_word(text: str) -> str:
#     """
#     returns the first word in a given text.
#     """
#     # your code here
#     text_without_dots = re.sub('[$\w\s]', '', text)
#     return text_without_dots.split()[0]
#
#
# if __name__ == "__main__":
#     print("Example:")
#     print(first_word("Hello world"))
#     print(first_word("don't touch it"))
#
#     # # These "asserts" are used for self-checking and not for an auto-testing
#     # assert first_word("Hello world") == "Hello"
#     # assert first_word(" a word ") == "a"
#     # assert first_word("don't touch it") == "don't"
#     # assert first_word("greetings, friends") == "greetings"
#     # assert first_word("... and so on ...") == "and"
#     # assert first_word("hi") == "hi"
#     # assert first_word("Hello.World") == "Hello"
#     # print("Coding complete? Click 'Check' to earn cool rewards!")

text = "don't, touch it"
first_word = text.split()[0]
text_without_dots = re.sub(r'$[\w\s]', '', first_word)
print(text_without_dots)
