# 1. Palindrome

# def palindrome(num):
#     number = num
#     no = int(str(num)[::-1])
#     if no == number:
#         print(f'{number} is Palindrome number')
#     else:
#         print(f'{number} is not Palindrome number')
# palindrome(int(input('Enter no : ')))


# 2. Add elements of both list and create new list. Using list comprehension.
# l = [1,2,3,4,5,6]
# l1 = [10,20,30,40,50,60]
#
# add = [(l[i]+l1[i]) for i in range(len(l))]
# print(add)

# 3. Narcissist Number
# narcissistic numbers are numbers that can be represented by some kind of mathematical
# manipulation of their digits. A whole number,
# or integer, that is the sum of the nth powers of its digits
# (e.g., 153 = 13 + 53 + 33)

# def narcissistic(num):
#     number = num
#     power = len(str(num))
#     sum = 0
#     while num>0:
#         d1=num%10
#         sum=sum+d1**power
#         num=num//10
#     if sum == number:
#         print(f'{number} is Narcissistic number')
#     else:
#         print(f'{number} is not Narcissistic number')
#
#
# narcissistic(num=int(input('Enter no : ')))

# 4. Sort values of dictionary in a list.

# dict = {'a':5, 'b':2, 'c':8, 'd':15}
# l = []
# for i in dict.values():
#     l.append(i)
# print(sorted(l))

# 5. Call constructor of parent class.

# class A:
#     def __init__(self):
#         print('parent class constructor')
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print('Child class constructor')
# b = B()


# 6. Prime Number

# def prime(num):
#     count = 0
#     for i in range(2,num):
#         if num % i == 0:
#             count+=1
#             break
#     if count == 0:
#         print(f'{num} is prime number')
#     else:
#         print(f'{num} is not prime number')
# prime(int(input('enter no : ')))

# 7. Fibonacci Number

# def fibbonacci(num):
#     x = 0
#     y = 1
#     for i in range(num):
#         print(x)
#         a = x
#         x = y
#         y = a+y
#
# fibbonacci(int(input('Enter no upto you want to print series: ')))

# 8. l =[a, d, c, v, h, a, d, c]
# Create list having duplicates only.

# l = ['a', 'd', 'c', 'v', 'h', 'a', 'd', 'c']
# l1 = []
# for i in l:
#     if l.count(i) > 1:
#         l1.append(i)
# print(l1)

# 9. Count of each alphabet in 'success'

# st = 'success'
# print(set(st))
# for i in set(st):
#     print('count of ',i,'-->',st.count(i))

# 10. Define models for attendance system of school.

# 11. Find highest possible product of three numbers from a list.

# l = [10, 2, 5, 8, 1, 30, 5]
# l1 = sorted(l)
# print(l1[-1]*l1[-2]*l1[-3])

# 12. Get second highest number from the list.

# l = [10, 2, 5, 8, 1, 5, 20, 20, 20]
# l1 = sorted(set(l))
# print(l1[-2])

# 13. Set intersection

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
# print(s1.intersection(s2))
print(s1&s2)

