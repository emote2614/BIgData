import re

pattern = r'apple'
text = 'I have an apple and a pineapple.'

result = re.search(pattern, text)
if result:
    print('re.search() 결과:', result.group())
else:
    print('일치하는 부분이 없습니다.')

result = re.match(pattern, text)
if result:
    print('re.match() 결과:', result.group())
else:
    print('일치하는 부분이 없습니다.')

pattern = r'\b\w+'
text = 'Hello, World!'

result = re.findall(pattern, text)
print('re.findall() 결과:', result)

matches = re.finditer(pattern, text)
print('re.finditer() 결과:')
for match in matches:
    print(match.group())