import re
print(re.search(r"Py.*n","Pygmalion"))

print(re.search(r"Py.*n","Python Programming"))

print(re.search(r"[a-z]*n","Python Programming"))

print(re.search(r"[a-z]*n","Pyn"))

print(re.search(r"o+l+","goldfish"))

print(re.search(r"p?each","To each their own"))

print(re.search(r"p?each","I like peaches"))

# Escaping Character

print(re.search(r".com","Welcome"))

print(re.search(r"\.com","Welcome"))

print(re.search(r"\.com","mydomin.com"))

print(re.search(r"\w*","This is an example"))

print(re.search(r"\w*","And_this_is_another_one"))

print(re.search(r"A.*a","Argentina"))

print(re.search(r"^A.*a$","Azerbaijan"))

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern,"_this_is_a_valid_variable_name"))