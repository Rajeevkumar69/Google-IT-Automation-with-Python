# Q1 .
import re
def transform_record(record):
  new_record = re.sub(r",([\d-]+)",r",+1-\1" ,record)

  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 

print(transform_record("Eli Jones,684-3481127,IT specialist")) 

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 

# Q2 .
import re
def multi_vowel_words(text):
  pattern = r"\b[A-Za-z]*[aeiou]{3,}[A-Za-z]*\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful"))

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))

print(multi_vowel_words("Hello world!")) 

# Q3 .
import re
def convert_phone_number(phone):
  result = re.sub(r'(?<!\S)(\d{3})-(\d{3})-(\d{4}\b)', r'(\1) \2-\3', phone)
  return result

print(convert_phone_number("My number is 212-345-9999."))
print(convert_phone_number("Please call 888-555-1234")) 
print(convert_phone_number("123-123-12345")) 
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) 