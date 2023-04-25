# with open('OOP/File/11.txt','r') as f:
#     file_txt = f.read()
#     print(file_txt)
#     file_txt = file_txt.strip()
#     nums_str = file_txt.split('#')
#     print(nums_str)
#     for i in range(1,len(nums_str)):
#         print(nums_str[i])
#         ans = input(f"{i}. javobingiz: ")
#         print('=============')



#     # print(nums_str)
#     # nums_list = list(map(int, nums_str))
#     # print(nums_list)
#     # nums_list = []
#     # for i in nums_str:
#     #     if i!='':
#     #         nums_list.append(int(i))

#     # max_numb = max(nums_list)
#     # min_numb = min(nums_list)
#     # sum_numb = max_numb+min_numb
#     # d = abs((nums_list[0]-nums_list[-1]))
# #
# # with open('result.txt','w') as g:
# #     maximal="Eng katta qiymat: "+str(max_numb)
# #     minimal="\nEng kichik qiymat: "+str(min_numb)
# #     summa="\nEng katta va Eng kichik qiymatlari yig'indisi: "+str(sum_numb)
# #     d="\nbirinchi va oxirgi komponentning farqi: "+str(d)

# #     g.writelines([maximal,minimal, summa, d])


s = """
*****
    *
*****
    *
*****
"""
bir = s[7]
uch = s[11]
besh = s[19]
yetti = s[25:30]
if bir == ' ' and besh == ' ' and yetti == '*****':
    print(3)
if bir == '*' and besh == ' ' and yetti == '*****':
    print(9)
# print(bir, uch, besh, yetti)
# print('================================')
# with open('OOP/File/test.txt','r') as f:
#     file_txt = f.read()
#     print(file_txt)