import pandas
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter : row.code for (index, row) in nato_alphabet.iterrows()}
text = input("Enter a word: ")
output = {letter: nato_dict[letter] if letter in nato_dict else "Not Found" for letter in text.upper()}
print("The Value of each letter is:")
for key, value in output.items():
    print(f"{key}: {value}")