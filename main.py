text = input("Введите текст: ")
text = text.lower()
puncte = ['.', ',', ':',  ';', '!', '?', '/']
for i in puncte:
    text = text.replace(i, '')
slova = text.split()
word_frequency = {}

print("Количество разных слов:", len(set(slova)))

for slovo in slova:
    if slovo in word_frequency:
        word_frequency[slovo] += 1
    else:
        word_frequency[slovo] = 1
print("Частота слов: ")
for slovo, frequency in word_frequency.items():
#<html>

    print(f"{slovo}: {frequency}")

