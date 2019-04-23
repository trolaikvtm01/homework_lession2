l = [23, 4.3, 4.2, 31, 'python', 1, 5.3, 9, 1.7]
print('list vua khoi tao la: ',l)
l.remove(l[4])
print('a) list sau khi remove "python": ',l)
l.sort()
print ('b) list duoc xep theo gia tri tang dan: ',l)
l.reverse()
print('   list duoc xep theo gia tri giam dan: ',l)
if 4.2 in l:
    print('c) yes, 4.2 in list')