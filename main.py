def generator_alphabet(start_letter, end_letter):
    start = ord(start_letter)
    end = ord(end_letter)
    while start <= end:
        yield chr(start)
        start += 1

runner = generator_alphabet('A', 'F') #수행보류
for letter in runner:
    print(letter)