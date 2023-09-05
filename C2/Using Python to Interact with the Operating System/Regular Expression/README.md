**_REGULAR EXPRESSION_**

.Regular expressions (regexes) are search queries for text that are expressed by string patterns.

.Regular expressions can be used to find specific patterns of text, such as all four-letter words in a file or all error types in an error log.

.Regular expressions are useful for anyone who needs to perform text processing, such as IT specialists, software engineers, system administrators, and data analysts.

.There are many different ways to apply regular expressions, including in Python, command line tools, and text processing tools.

.The principles of regular expressions are the same regardless of the tool or language that is used.

.Regular expressions (regexes) are more powerful and flexible than simply looking for strings in a text.

.Regexes can be used to extract specific patterns of text, even if the pattern is not known in advance.
For example, regexes can be used to extract the process identifier from a log entry, even if the length of the .process identifier is not known.

.Regexes can be used in Python, command line tools, and text processing tools.

.The syntax of regexes can be complex, but they are a powerful tool for text processing.

.Grep is a command line tool that can be used to search for patterns in text files.

.The simplest way to use grep is to pass a string as a pattern to match.

.Grep will print any lines that contain the pattern.

.The -i parameter can be used to make the match case insensitive.

.The dot character (.) matches any character.

.The caret (^) character matches the beginning of a line.

.The dollar sign ($) character matches the end of a line.

**_BASIC REGULAR EXPRESSION_**
.Regular expressions are a powerful tool for matching patterns in text.

.In Python, we can use the re module to apply regular expressions.

.The search function on the re module takes a pattern and a string as input, and returns a match object if the pattern is found in the string.

.The match object has attributes that provide information about the match, such as the start and end positions of the match, and the actual matching string.

.We can use special characters in regular expressions to match specific patterns, such as the beginning of the line (^), any character (.), and a range of characters ([abc]).

.We can also pass additional options to the search function, such as the re.IGNORECASE option, which makes the match case insensitive.

.Character classes are a powerful tool in regular expressions that allow us to match specific groups of characters.

.We can use character classes to match a range of characters, such as all lowercase letters or all digits.

.We can also use character classes to match any character that is not in a specified group.

.We can use the pipe symbol to match either one expression or another.

.The findall function can be used to find all possible matches for a regular expression.

\*[a-z] matches any lowercase letter.

\*[0-9] matches any digit.

\*[a-zA-Z0-9] matches any letter or digit.

\*[^a-z] matches any character that is not a lowercase letter.

\*[a|b] matches either the letter a or the letter b.

.Repeated matches can be used to match a character or group of characters multiple times.

.The star (\*) repetition qualifier matches any character zero or more times.

.The plus (+) repetition qualifier matches any character one or more times.

.The question mark (?) repetition qualifier matches any character zero or one time.

.The repetition qualifiers are greedy, which means they will match as many characters as possible.

.It is possible to modify the repetition qualifiers to make them less greedy.

.The Python implementation of regular expressions includes two additional repetition qualifiers:

.The {n} repetition qualifier matches exactly n occurrences of the character before it.

.The {n,m} repetition qualifier matches at least n and at most m occurrences of the character before it.

.\* matches any character zero or more times.

.O+ matches one or more occurrences of the letter O.

.P? matches either zero or one occurrence of the letter P.

.{2} matches exactly two occurrences of the previous character.

.{3,5} matches at least three and at most five occurrences of the previous character.

.Escape characters are used to match special characters in regular expressions.

.The backslash character (\) is used as an escape character in regular expressions.

.To match an actual dot character, we need to use the escape sequence \..

.We can also use escape sequences to match other special characters, such as the star (\*), plus (+), question mark (?), circumflex (^), dollar sign (\$), and square brackets ([]).

.Python also uses the backslash for a few special sequences that we can use to represent predefined sets of characters. For example, the sequence \w matches any alphanumeric character, including letters, numbers, and underscores.

.Other special sequences include \d for matching digits, \s for matching whitespace characters, and \b for word boundaries.

.We can combine regular expression special characters to create patterns to match the text that we want.

.For example, the pattern A.\*a matches any string that starts and ends with the letter a.

.We can make our patterns stricter by adding the beginning of a line (^) and end of a line (\<span class="math-inline">\) characters. _ For example, the pattern `^a\$` matches any string that only contains the letter `a`. _ We can also use regular expressions to validate strings. For example, the pattern `^[a-zA-Z_]+\` matches any string that starts with a letter or underscore and contains only letters, numbers, or underscores.

**_Advanced Regular Expression_**

.Capturing groups are portions of a regular expression that are enclosed in parentheses.

.They can be used to extract specific information from a string that matches the regular expression.
For example, a capturing group could be used to extract the hostname from a log line.
.To access the information that is captured in a group, you can use the groups() method of the re.Match object.

.The groups() method returns a tuple of all of the captured groups.

.You can also access individual groups by their index.

.The first group contains the text that matched the entire regular expression.

.Subsequent groups contain the text that matched each of the subsequent capturing groups.

.In the video, a function was defined to rearrange names that were stored in the format last name, comma, first name.

.The function used a regular expression with capturing groups to extract the first and last names from the string.

.The function then returned the string with the first name and last name reversed.

.The function was tested with a few names, and it worked as expected.

.However, the function did not work correctly when the name included a middle initial.

.This is because the regular expression only matched letters.
To fix this, the regular expression was updated to include spaces, dots, and dashes.

.The updated function was then able to rearrange names that included middle initials.

.Numeric repetition qualifiers are used to specify the number of times a pattern should be repeated.

.They are written between curly brackets.

.A single number in the curly brackets specifies an exact number of repetitions.

.A range of numbers in the curly brackets specifies a minimum and maximum number of repetitions.

.The open ended qualifiers {n,} and {,m} match a string with at least n or at most m repetitions, respectively.

.Numeric repetition qualifiers can be used with any of the other regular expression metacharacters.

.\d{3} matches a string of exactly three digits.

.[a-z]{5,10} matches a string of five to ten lowercase letters.

.\w{,20} matches a string of up to 20 alphanumeric characters.

**_Extracting a PID Using regexes in Python_**

.findall(): Returns a list of all the substrings that match the regular expression.

.split(): Splits the string into substrings based on the regular expression.

.sub(): Replaces all the substrings that match the regular expression with a new substring.

.compile(): Compiles the regular expression into a regular expression object.

.match(): Returns a match object if the regular expression matches the beginning of the string.

.search(): Returns a match object if the regular expression matches anywhere in the string.

**_Splitting and Replacing_**

.The split() function splits a string into substrings based on a regular expression.

.The sub() function replaces all the substrings that match a regular expression with a new substring.

.The split() function takes two arguments: the string to split and the regular expression to use as a separator.

.The sub() function takes three arguments: the regular expression, the replacement string, and the string to search.

.The sub() function returns a new string with the replacements made.
