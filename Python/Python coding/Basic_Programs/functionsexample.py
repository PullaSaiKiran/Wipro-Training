# #functions
# def add(n1 , n2):
#     return n1+n2
#
# def sub(n1 , n2):
#     return n1 - n2
#
# def mul(n1 , n2):
#     return n1 * n2
#
# def div():
#     pass
#
#
#
#
#
# #driver
#
# num1=int(input("enter a number"))
# num2=int(input("enter another number"))
#
# result=add(num1,num2)
# print("Addition as result: ",result)
#
# result=sub(num1,num2)
# print("subtraction as result: ",result)
#
# result=mul(num1,num2)
# print("Multiplication as result: ",result)
#

# #ARBITARY
# def add(*nums):
#     sum=0
#     for n in nums:
#         sum +=n
#     return sum
# #
# #
# #
# # numbers = list()
# # count=int(input("How Many Numbers Do you want to print ?? "))
# # for _ in range(1,count+1):
# #     numbers.append(int(input("No: ")))
# #
# # print(numbers)
# print(add(5,6,8))
# print(add(7.66,6,8))
# print(add(5,6,8,3,2,4,7,8))
#
# def add(n1, n2, n3=10):
#     return n1+n2+n3
#
# num1=int(input("enter a number"))
# num2=int(input("enter another number"))
#
# print(add(num1,num2))
# print(add(num1,num2,n3=100))



### Lambda Function
#
# num1=int(input("enter a number"))
# num2=int(input("enter another number"))
# add = lambda n1,n2 : n1+n2
# print('Addition Of Two Numbers:',add(num1,num2))
#
#
#
#
# number = [1, 2, 3, 4, 5]
# sq = lambda num: num**2
# print(list(map(sq, number)))

# number = [1, 2, 3, 4, 5]
# sq = lambda nums: [num*num for num in nums]
# print(tuple(sq(number)))


