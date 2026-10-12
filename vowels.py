count_vowels = lambda text: sum(1 for char in text.lower() if char in "aeiou")
print(count_vowels("Education"))