"""
Given a list of strings made up of the characters 'a' and 'b', 
create a regular expression that will
match strings that begin and end with the same
letter.

Example : 
'a', 'aa', and 'bababbb' match.
'ab'and 'baba' do not match.
"""

import re

regularExpression = r'^(a.*a | b.*b)$'
pattern = re.compile(regularExpression)
query = int(input())
result = ['False'] * query

for i in range(query):
    someString = input ()
    if pattern.match(someString):
        print(f"'{query}' matches ✅")

print(result)