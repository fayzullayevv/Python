#1
# k = int(input())
# n = int(input())
# for i in range(n):
#     print(k)

#2
# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     print(i)


#3
# a = int(input())
# b = int(input())
# for i in range(b,a+1):
#     print(i)


#4
# a = int(input())
# for i in range(11):
#     print(i*a)




#7
# s = 0 
# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     s+=i
# print(s)


#8
# s = 1
# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     s*=i
# print(s)


#9
# s = 1
# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     s=i**2
# print(s)


#10
# a = 0
# n = int(input())
# for i in range(1,n+1):
#     s=1/i
#     a=a+s
# print(a)


#11
# a = 0
# n = int(input())
# for i in range(1,n+1):
#     s=(i+1)**2
#     a=a+s
# print(a)


#15
# a = int(input())
# n = int(input())
# print(a**n)


#16
# a = int(input())
# n = int(input())
# for i in range(1,n+1):
#     print(a**i)


#17
# s = 0
# a = int(input())
# n = int(input())
# for i in range(1,n+1):
#     f=a**i
#     s=s+f
# print(s)


#18
# s = 0
# a = int(input())
# n = int(input())
# for i in range(1,n+1):
#     a = a**i
#     s+=1
# print(s)


#19
# a = 1
# n = int(input())
# for i in range(1,n+1):
#     print(i*a)


#20
# a = 1
# s = 0 
# n = int(input())
# for i in range(1,n+1):
#     a = a*i
#     s = s+a
# print(s)


#21
# a = 1
# s = 0 
# n = int(input())
# for i in range(1,n+1):
#     a = 1/(a*i)
#     s = s+a
# print(s)


#22
# a = 1
# s = 0 
# x = int(input())
# n = int(input())
# for i in range(1,n+1):
#     a = x**i/(a*i)
#     s = s+a
# print(s)

# 31
# def sonlar(n):
#     if n==0:
#         return 2
#     else:
#         return 2+1/sonlar(n-1)
    
# print(sonlar(n = int(input())))


# 32
# def sonlar(n):
#     if n==0:
#         return 1
#     else:
#         return (sonlar(n-1)+1)/n
    
# print(sonlar(n = int(input())))
#f(1) = 2
# f(2) = 1,5
# f(3) = 0,8



# 33
# def fibonachi(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return (fibonachi(n-2)+fibonachi(n-1))
    
# print(fibonachi(n = int(input())))


# 34
# def sonlar(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#        return (sonlar(n-2)+2*sonlar(n-1))/3
    
# print(sonlar(n = int(input()))) 
 

# 35
# def sonlar(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     elif n==3:
#         return 1
#     else:
#        return sonlar(n-1)+sonlar(n-2)-2*(sonlar(n-3))
    
# print(sonlar(n = int(input()))) 


# 36
# n = int(input())
# k = int(input())
# s = 0
# for i in range(n):
#     result = i**k
#     s+=result
# print(s)


# 37
# n = int(input())
# s = 0
# for i in range(1,n+1):
#     result = i**i
#     s+=result
# print(s)



# 38
# n = int(input())
# s = 0 
# for i in range(1,n+1):
#     result = i**(n-i+1)
#     s+=result
# print(s)



# 39
# a = int(input())
# for i in range(1,a+1):
#     for k in range(i):
#         print(i)
