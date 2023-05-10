import re

match = re.search(r'na+', 'naaaaver') # naaaa
print(match.group())
match = re.search(r'a+', 'naavaaaar') # aa
print(match.group())
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # 1 2   3
print(match.group())
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # 12  3
print(match.group())
match = re.search(r'\d\s*\d\s*\d', 'xx123xx') # 123
print(match.group())
match = re.search(r'^b\w+', 'naver') # None
print(match)
match = re.search(r'v\w+', 'naver') # ver
print(match.group())