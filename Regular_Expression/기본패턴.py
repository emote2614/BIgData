import re

match = re.search(r'ave', 'naver')
print(match.group()) # ave
match = re.search(r'ers', 'naver')
print(match) # None
match = re.search(r'..r', 'naver')
print(match.group()) # ver
match = re.search(r'\d\d\d', 'na000ver')
print(match.group()) # 000
match = re.search(r'\w\w\w', '#@naver*%')
print(match.group()) # nav