import os
import re

# 특정 파일 이름 찾기
filename = r'test.txt'
found_files = [f for f in os.listdir('.') if re.match(filename, f)]
print('특정 파일 이름 찾기:', found_files)

# 파일 경로 찾기
filepath = r'/Users/cbs/Desktop/PHTYON/빅데이터/과제/BIgData/Regular_Expression/test.txt'
found_files = [os.path.join(root, f) for root, dirs, files in os.walk('.') for f in files if re.match(filepath, os.path.join(root, f))]
print('파일 경로 찾기:', found_files)

# 파일 확장자 찾기
extension = r'\.txt$'
found_files = [f for f in os.listdir('.') if re.search(extension, f)]
print('파일 확장자 찾기:', found_files)

# 패턴으로 파일 찾기
pattern = r'^test_\d+\.txt$'
found_files = [f for f in os.listdir('.') if re.match(pattern, f)]
print('패턴으로 파일 찾기:', found_files)
