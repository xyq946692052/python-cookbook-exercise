import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(text)

res1 = re.findall('python', text, flags=re.IGNORECASE)
print(res1)

res2 = re.sub('python', 'snack', text, flags=re.IGNORECASE)
print(res2)


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return world
    return replace

res3 = re.sub('python', matchcase('snack'), text, flags=re.IGNORECASE)
print(res3)
