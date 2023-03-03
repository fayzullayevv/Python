# 1
# def new_func():
#     a = int(input())
#     if a>0:
#         return a+1
#     else:
#         return a

# print(new_func())


# 2
# def new_func():
#     a = int(input())
#     if a>0:
#         return a+1
#     else:
#         return a-2

# print(new_func())


# 3
# def new_func():
#     a = int(input())
#     if a>0:
#         return a+1
#     elif a<0:
#         return a-2
#     elif a==0:
#         a=10
#         return a

# print(new_func())


# 4
# def new_func(a,b,c):
#     if a<0 and b>0 and c>0:
#         return '2ta'
#     elif a>0 and b<0 and c>0:
#         return '2ta'
#     elif a>0 and b>0 and c<0:
#         return '2ta'
#     elif a<0 and b<0 and c>0:
#         return '1ta'
#     elif a>0 and b<0 and c<0:
#         return '1ta'
#     elif a<0 and b>0 and c<0:
#         return '1ta'
#     else:
#         return '3ta'

# print(new_func(a=int(input()),b=int(input()),c=int(input())))


# 5
# def new_func(a,b,c):
#     if a<0 and b>0 and c>0:
#         return '2ta musbat 1ta manfiy'
#     elif a>0 and b<0 and c>0:
#         return '2ta musbat 1ta manfiy'
#     elif a>0 and b>0 and c<0:
#         return '2ta musbat 1ta manfiy'
#     elif a<0 and b<0 and c>0:
#         return '1ta musbat 2ta manfiy'
#     elif a>0 and b<0 and c<0:
#         return '1ta musbat 2ta manfiy'
#     elif a<0 and b>0 and c<0:
#         return '1ta musbat 2ta manfiy'
#     else:
#         return '3ta musbat'

# print(new_func(a=int(input()),b=int(input()),c=int(input())))


# 6
# def new_func(a,b):
#     if a>b:
#         return a
#     elif a<b:
#         return b
#     elif a==b:
#         return 'teng'

# print(new_func(a=int(input()),b=int(input())))


# 7
# def new_func(a,b):
#     if a>b:
#         return b
#     elif a<b:
#         return a
#     elif a==b:
#         return 'teng'

# print(new_func(a=int(input()),b=int(input())))


# 8
# def new_func(a,b):
#     if a>b:
#         return a,b
#     elif a<b:
#         return b,a

# print(new_func(a=int(input()),b=int(input())))


# 9
# def new_func(a,b):
#     if a>b:
#         b+=10
#         return b,a
#     elif a<b:
#         return a,b

# print(new_func(a=int(input()),b=int(input())))



# 10
# def new_func(a,b):
#     if a!=b:
#         return b+a
#     elif a==b:
#         return 0

# print(new_func(a=int(input()),b=int(input())))


# 11
# def new_func(a,b):
#     if a!=b:
#         if a>b:
#             return a
#         if a<b:
#             return b
#     elif a==b:
#         return 0

# print(new_func(a=int(input()),b=int(input())))


# 12
# def new_func(a,b,c):
#     if a<b and a<c:
#         return a
#     elif b<a and b<c:
#         return b
#     elif c<a and c<b:
#         return c

# print(new_func(a=int(input()),b=int(input()),c=int(input())))


# 14
# def new_func(a,b,c):
#     if a<b and a<c and b>c:
#         return a,b
#     elif a<b and a<c and c>b:
#         return a,c
#     elif b<a and b<c and a>c:
#         return b,a
#     elif b<a and b<c and c>a:
#         return b,c

# print(new_func(a=int(input()),b=int(input()),c=int(input())))


# 16
# def new_func(a,b,c):
#     if a<b<c:
#         a*2
#         b*2
#         c*2
#         return a,b,c
#     else:
#         a = -a
#         b = -b
#         c = -c
#         return a,b,c

# print(new_func(a=int(input()),b=int(input()),c=int(input())))


# 17
# def new_func(a,b,c):
#     if a<b<c or a>b>c:
#         a*2
#         b*2
#         c*2
#         return a,b,c
#     else:
#         a = -a
#         b = -b
#         c = -c
#         return a,b,c

# print(new_func(a=int(input()),b=int(input()),c=int(input())))


# 18
# def new_func(a,b,c):
#     if a==b:
#         return a,c
#     elif a==c:
#         return a,b
#     elif b==c:
#         return b,a

# print(new_func(a=int(input()),b=int(input()),c=int(input())))


# 19
# def new_func(a,b,c,d):
#     if a==b==c:
#         return a,d
#     elif a==b==d:
#         return a,c
#     elif b==c==d:
#         return b,a

# print(new_func(a=int(input()),b=int(input()),c=int(input()),d=int(input())))


# 20
# a = int(input())
# b = int(input())
# c = int(input())
# if b-a>c-a:
#     print(b+a)
# elif b-a<c-a:
#     print(c+a)


# 22
# def new_func(x,y):
#     if x<0 and y>0:
#         return '1-chorak'
#     elif x>0 and y>0:
#         return '2-chorak'
#     elif x<0 and y<0:
#         return '3-chorak'
#     elif x>0 and y<0:
#         return '4-chorak'

# print(new_func(x = int(input()),y = int(input())))


# 24
# import math
# def new_func(x):
#     if x>0:
#         return 2*math.sin(x)
#     elif x<=0:
#         return x-6

# print(new_func(x = int(input())))


# 25
# def new_func(x):
#     if x<-2 or x>2:
#         return 2*x
#     else:
#         return -3*x

# print(new_func(x = int(input())))


# 26
# def new_func(x):
#     if x<=0:
#         return -x
#     elif 0<x<2:
#         return x**2
#     elif x>=2:
#         return 4

# print(new_func(x = int(input())))


# 29
# def new_func(x):
#     if x>0 and x%2>0:
#         return 'musbat toq son'
#     elif x<0 and x%2==0:
#         return 'manfiy juft son'
#     elif x==0:
#         return 'son nolga teng'

# print(new_func(x = int(input())))


# 30
# def new_func(x):
#     if x>=10 and x%2==0:
#         return 'ikki xonali juft son'
#     elif x>=100 and x%2>0:
#         return 'uch xonali toq son'

# print(new_func(x = int(input())))

