import re

pattern = r'[defghij]'  # d~i에 일치하는 패턴
text = 'Hello, World!'

result = re.findall(pattern, text)
print(result)  # ['e', 'd']