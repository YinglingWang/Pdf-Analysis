# import re
# m = re.match(r'\d+\.\d+\.\d+\.\d+','190.128.kkk.2')
# print(m)

# import sys
# import difflib
#
# def read_file(filename):
#     try:
#         with open(filename, 'r') as f:
#             return f.readlines()
#     except IOError:
#         print("ERROR" % filename)
#         sys.exit(1)
#
# def compare_file(file1, file2, out_file):
#     file1_content = read_file(file1)
#     file2_content = read_file(file2)
#     d = difflib.HtmlDiff()
#     result = d.make_file(file1_content, file2_content)
#     with open(out_file, 'w') as f:
#         f.writelines(result)
#
# if __name__ == '__main__':
#     compare_file(r'/Users/yinglingwang/change.txt', r'/Users/yinglingwang/origin.txt', r'/Users/yinglingwang/result.html')

