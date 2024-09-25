#             # BASICS

# # def function(num, num1, op):
# #     run = True
# #     while run:

# #         if op == "+":
# #             print(num + num1)
# #         elif op == "-":
# #             print(num - num1)
# #         elif op == "*":
# #             print(num * num1)
# #         elif op == "/":
# #             print(num /num1)   
# #     v = input("do you want to continue to calculate? enter Yes or No:")
# #     condition = v.lower()
# #     if condition == "no":
# #         run = False
# #     elif condition == "yes":
# #         run = True
# #     else:
# #         print("enter only yes or no")
# # num = int(input("enter a number:"))
# # num1 = int(input("enter another:"))
# # op = input("enter an operator:")
# # print(function(num, num1, op))
        
#                     # CODE NOM.2
# # import random
# # def rock_paper_scissors():
# #     run = True
# #     while run:
# #         user = input("enter rock, paper or scissors:")
# #         chose = ["rock", "paper","scissors"]
# #         program = random.randint(chose)
# #         if user == "rock" and program == "scissors":
# #             print("you win","\nprogram =", program, "you =",user)
# #         elif user == "rock" and program == "paper":
# #             print("you lose","\nprogram =", program, "you =",user)
# #         elif user == "rock" and program == "rock":
# #             print("it's a draw","\nprogram =", program, "you =",user)
# #         elif user == "paper" and program == "rock":
# #             print("you win","\nprogram =", program, "you =",user)
# #         elif user == "paper" and program == "scissors":
# #             print("you lose","\nprogram =", program, "you =",user)
# #         elif user == "paper " and program == "paper":
# #             print("it's a draw","\nprogram =", program, "you =",user)
# #         elif user == "scissors" and program == "paper":
# #             print("you win","\nprogram =", program, "you =",user)
# #         elif user == "scissors" and program == "rock":
# #             print("you lose","\nprogram =", program, "you =",user)
# #         elif user == "scissors" and program == "scissors":
# #             print("it's a draw","\nprogram =", program, "you =",user)
# #     v = input("do you wish to continue? Yes or no:")
# #     condition = v.lower()
# #     if condition == "yes":
# #         run = True
# #     elif condition == "no":
# #         run = False
# #     else:
# #         print("Yes or No!")
# # rock_paper_scissors()            


#                     # TWO-SUM
# # def two_sum(a, target):   
# #     for i in range(0,len(a)):       # the first element
# #         for j in range(i+1, len(a)):          # the second element 
# #             if a[i] + a[j] == target:             
# #                 return {i:a[i],j:a[j]}
# # a = [2,7,11,15]
# # target = 9
# # print(two_sum(a, target)


#                     #  Sort an array but they are 0 and 1 only, code nom.3
# # def sort_array(a,n):
# #     count = 0
# #     for i in range(0,n):
# #         if (a[i] == 0):
# #             count = count + 1
# #     for i in range(0,count):
# #         a[i] = 0
# #     for j in range(count,n):
# #         a[i] = 1
# # a = [0,0,1,0,1,1,0]
# # n = len(a)
# # sort_array(a,n)
# # print("The sorted Array is:",a)
# # for i in range(0,n):
# #     print(a[i],end=" ")


# #                          merge the array and then sort them, code nom.4
# # def sort_array(a,a1,n,m):
# #     i,j = 0,0
# #     while i<m and j<n:
# #         if a[i] > a1[j]:
# #             print(a[i],end = " ")
# #             i+=1
# #         elif a1[j] < a[i]:
# #             print(a1[j],end = " ")
# #             j+=1
# #         else:
# #             print(a1[j],end = " ")
# #             i+=1
# #             j+=1
# #     while i < m:
# #         print(a[i], end = " ")
# #         i+=1
# #     while j < n:
# #         print(a1[j],end = " ")
# #         j+=1
# # a = [1,2,8,9]
# # a1 = [2,3,5,7]
# # m = len(a)
# # n = len(a1)
# # print(sort_array(a,a1,n,m))


# #                            Quick sort, code nom.5
# def quick_sort(a,left, right):
#     pivot = a[right]
#     i = left -1
#     for j in range(left, right):
#         if a[j] <= pivot:
#             i = i+1
#             (a[i], a[j]) = (a[j],a[i])
#     (a[right],a[i+1]) = (a[i+1],a[right])
#     return i+1
# def partition(a, left, right):
#     if left < right:
#         pi = partition(a, left, right)

#         quick_sort(a,left, pi-1)

#         quick_sort(a,pi+1,right)
# a = [2,7,1,9]
# print("Given Array:",a)
# quick_sort(a,0,len(a)-1)
# print("Sorted Array:",a)



# def rotarion(a, n, a_size):   # n = how many times the array is rotated
#     for i in range(n):
#         rotate(a,a_size)
# def rotate(a, a_size):
#     temp = a[0]
#     for i in range(a_size -1):
#         a[i] = a[i+1]
#     a[a_size-1] = temp
# def printArray(a,a_size):
#     for i in range(a_size):
#         print("% d"%a[i], end = " ")
#     print("\n")
# a = [1,2,3,4,5]
# printArray(a, len(a))
# rotarion(a,2,len(a))
# printArray(a, len(a))



a = [3,4,5,1,2]
n = len(a)
count = 0
for i in range(1,n):
    if (a[i-1]>a[i]):
        count +=1
if (a[n-1]>a[0]):
    count+=1
print(count<=1)



