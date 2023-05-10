import re

pattern = r'(\d{4})-(\d{2})-(\d{2})'
text = 'Today is 2023-05-10.'

result = re.search(pattern, text)
if result:
    print(result.group())  # 전체 일치 결과: 2023-05-10
    print(result.group(1))  # 첫 번째 그룹: 2023
    print(result.group(2))  # 두 번째 그룹: 05
    print(result.group(3))  # 세 번째 그룹: 10