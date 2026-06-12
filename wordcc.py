sentence =input(" enter a sentence: ").lower()

words = sentence.split()
word_count =len(words)
char_count =len(sentence.replace(" ",""))

print(f"words:{word_count}")
print(f"characters(no spaces):{char_count}")

frequency ={}
for word in words :
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

most_common = max(frequency , key = frequency.get)
print(f"most repeated word :'{most_common}'({frequency[most_common]}times)") 

least_common = min(frequency,key = frequency.get)
print(f"least_common:'{most_common}'({frequency[least_common]}times)")