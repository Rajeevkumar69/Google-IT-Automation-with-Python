import re

print (re.search(r"[a-zA-Z]{5}","a ghost"))
print (re.search(r"[a-zA-Z]{5}","a scary ghost appeared"))
print (re.findall(r"[a-zA-Z]{5}","a scary ghost appeared"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "A Scary ghost appered"))
print(re.findall(r"\w{5,}", "I really likes strewberries"))
print(re.findall(r"\w{5,10}", "I really likes strewberries"))
print(re.findall(r"s\w{,20}", "I really likes strewberries"))

log = "July 31 07:51:48 myComputerBadProcess[123456] :ERROR Performing package upgrade"
regex = r"\[{\d+}\]"
result = re.search(regex,log)
if result is None:
        print("It's None")
else:
        print(result[1])

result = re.search(regex ,"A Completely different string that also has number [123456789]")
if result is None:
        print("It's None")
else:
        print(result[1])

result = re.search(regex, "99 Elephant in a [cage]")
print(result)


def extractPID(log_line):
        regex = r"\[(\d+)\]"
        result = re.search(regex,log_line)
        if result is None:
                return ""
        return result[1]
print(extractPID(log))

print(extractPID("99 Elephant in a [cage]"))

data = re.split(r"[.?!]","One Sentence, Another One ? and Last One!")
print(data)

data = re.split(r"([.?!])","One Sentence, Another One ? and Last One!")
print(data)

data =  re.sub(r"[\w.%+-]+@[\w.-]+","[REDACTED]","Recieved an email for support_learningpython@gmail.com")
print(data)

data = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2\1", "Lovelance Ada" )
print(data)