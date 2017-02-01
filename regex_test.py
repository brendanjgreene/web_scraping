import re

print "# Using * asterisk - multiple occurrences of the character preceding it"
print re.findall("ab*c", "ac")  # ['ac']
print re.findall("ab*c", "abcd")  # ['abc']
print re.findall("ab*c", "acc")  # ['ac']
print re.findall("ab*c", "abcac")  # ['abc', 'ac']
print re.findall("ab*c", "abdc")  # []
print re.findall("ab*c", "ABC")  # [] case sensitive

print '# Using re.IGNORECASE'
print re.findall("ab*c", "ABC", re.IGNORECASE)  # ['ABC']
