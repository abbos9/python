# 1
# numbers = [12, 132, 33, 243232, 31, 3232323, 23, 234, 2432, 43, 43, 434, 4, 343, 23, 32, 3, 221, 2, 12, ]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# 2
# numbers = [12, 132, 33, 243232, 31, 3232323, 23, 234, 2432, 43, 43, 434, 4, 343, 23, 32, 3, 221, 2, 12, ]
# max_num =max(numbers)
# numbers[5] = max_num
# print(numbers)


# 3
# numbers = [-1, 12, -4, 12, 22, 44, -89, -65, 12, 22, 444, -876, 21]
# count = []
# for num in numbers:
#     if num > 0:
#         count.append(num)
# print(count)

# homework
# 1
# numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
# max_num = max(numbers)
# min_num = min(numbers)
# numbers.pop(9)
# numbers.remove(11)
# numbers.insert(9, min_num)
# numbers.insert(0, max_num)
# print(numbers)
# 2
# numbers = [12, 123, 323, 2323, 23232, 3212, 32, 43, 5, 4567, 788, 9]
# nums = numbers[0]
# for num in numbers:
#     if num % 2 == 0 and nums < num:
#         nums = num
# print(nums)
# 3
# numbers = [12, 123, 323, 2323, 23232, 3212, 32, 43, 5, 4567, 788, 9]
# nums = numbers[0]
# for num in numbers:
#     if num % 2 != 0 and nums < num:
#         nums = num
# print(nums)
# 4
# numbers = [12, 123, 323, 2323, 23232, 3212, 32, 43, 5, 4567, 788, 9]
# toq = 0
# juft = 0
# for num in numbers:
#     if num % 2 == 0:
#         juft += num
#     elif num % 2 != 0:
#         toq += num
# print(juft + toq)
# 5
# numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
#
# for num in numbers:
#     if num % 2 == 0:
# # bilmadim 5 qanaqa qilish kereligini
# 6
# numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99, 190]
#
# max_num = max(numbers)
# min_num = min(numbers)
#
# max_indexs = numbers.index(max_num)
# min_indexs = numbers.index(min_num)
#
# numbers[max_indexs] = max_num
# numbers[min_indexs] = min_num
# print(numbers)
# 7
nums = [11, 33, 4, 65, 7, 8, 500, 40, 32]
min_num = nums[0]

for num in nums:
    if num % 2 != 0 and num < min_num:
        min_num = num

print(min_num)
