# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# # in a hyphen-separated sequence after sorting them alphabetically

data_hypen = input("Enter  ahypen-seperated sequence of words :")
hypen_words =data_hypen.split('-')
hypen_words.sort()
sorted_hypen_word = ('-'.join(hypen_words))
print(sorted_hypen_word)