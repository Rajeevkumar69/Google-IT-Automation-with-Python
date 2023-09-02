# Q1 >
import re

def check_web_address(text):
  pattern = r'^[A-Za-z._-][^/@]*$'
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

# Q2 >

import re

def check_time(text):
    pattern = r"^(0?[1-9]|1[0-2]):[0-5][0-9]\s?[APap][Mm]$"

    # Use re.search to find a match in the text
    result = re.search(pattern, text)

    # Return True if a match is found, otherwise return False
    return result is not None

# Test cases
print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


# Q3 >

import re
def contains_acronym(text):
  pattern = r"\([A-Z1-9][a-zA-Z1-9]*\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

# Q4 >

import re
def check_zip_code (text):
  return re.search(r'\d{5}(?:-\d{4})?', text) != None
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False