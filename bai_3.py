# Nhập vào chuỗi s
s = ("Hi John, welcome to python programming for beginner!")
print(s)
#Câu a
if "python" in s:
    print('a) Yes "python" in s')

#Câu b
x = " John"
if x in s:
    s1 = x
    s = (s.replace(x,""))
print ('b) s1= ',s1)
print ('Chuoi s sau khi Extract "John" là: ',s)

#Câu c
print('c) So lan xuat hien của ky tu "o" là: ',s.count('o'))
s = s.split()

#Câu d
print ('d) Chuoi s sau khi dung split() function: ',s)
print('So tu trong chuoi s la: ',len(s))