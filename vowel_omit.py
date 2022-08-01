vowels='aeiou'

sentence='I am awesome'

filtered_sentence=''.join([letter for letter in sentence if letter not in vowels])
print(filtered_sentence)