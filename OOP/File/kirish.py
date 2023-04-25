# f = open('OOP/File/test1.txt', 'a')
# sonlar = [str(x) + ' ' for x in range(1, 11)]
# for i in sonlar:
    # f.write(str(i) + ' ')
# f.writelines(sonlar)
# f.close()

# with open('OOP/File/test2.txt', 'a') as f:
#     f.write('\nTest2')
#     f.close()

f = open('OOP/File/test1.txt', 'r')
text = f.read()
f.close()

# text.strip()
print(text.split('\n'))
# for i in text.split(' ')[:-1]:
#     print(int(i)**2, end=' ')


