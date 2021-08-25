# Здесь представлены решения задач из курса Python: основы и применение
# Тема урока: регулярные выражения

# import sys
# import re
#
# pattern = r'cat.*cat'
# for line in sys.stdin:
#     line = line.rstrip()
#     match = re.search(pattern, line)
#     if match:
#         print(line)





# import sys
# import re
#
# pattern = r'\bcat\b'
# for line in sys.stdin:
#     line = line.rstrip()
#     match = re.search(pattern, line)
#     if match:
#         print(line)





# import sys
# import re
#
# pattern = r'z.{3}z'
# for line in sys.stdin:
#     line = line.rstrip()
#     match = re.search(pattern, line)
#     if match:
#         print(line)




# import sys
# import re
#
# pattern = r'\\'
# for line in sys.stdin:
#     line = line.rstrip()
#     match = re.search(pattern, line)
#     if match:
#         print(line)





# import sys
# import re
#
# pattern = r'\b(\w+)\1\b'
# for line in sys.stdin:
#     line = line.rstrip()
#     match = re.search(pattern, line)
#     if match:
#         print(line)




# import sys
# import re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub('human', 'computer', line))





# import sys
# import re
#
# pattern = r'\b[Aa]+\b'
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(pattern, 'argh', line, count=1))





# import sys
# import re
#
# pattern = r'cat.*cat'
# for line in sys.stdin:
#     line = line.rstrip()
#     pattern = r'\b(\w)(\w)'
#     print(re.sub(pattern, r'\2\1', line))





# import sys
# import re
#
# pattern = r'(\w)\1+'
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(pattern, r'\1', line))