# Q1. -> A
# def max_kernel(num_list, k):
#     result = []

#     for i in range(len(num_list) - k + 1):
#         result.append(max(num_list[i:i + k]))

#     return result


# assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
# num_lst = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
# k = 3
# print(max_kernel(num_lst, k))

# Q2. -> A
# def character_count(word):
#     character_statistics = {}

#     for character in word:
#         if character in character_statistics:
#             character_statistics[character] += 1
#         else:
#             character_statistics[character] = 1

#     return character_statistics


# assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
# print(character_count("smiles"))

# Q3. -> C
# def count_word(file_path):
#     counter = {}

#     with open(file_path, 'r') as file:
#         for line in file:
#             line = line.lower()
#             words = line.split()

#             for word in words:
#                 if word in counter:
#                     counter[word] += 1
#                 else:
#                     counter[word] = 1

#     return counter


# file_path = "../practice_exercise/P1_data.txt"
# result = count_word(file_path)
# assert result['who'] == 3
# print(result['man'])

# Q4. -> C
# def levenshein_distance(token1, token2):
#     # Initialize the matrix
#     distance_matrix = [[0 for _ in range(len(token2) + 1)]
#                        for _ in range(len(token1) + 1)]

#     # Fill the first row
#     for i in range(len(token1) + 1):
#         distance_matrix[i][0] = i

#     # Fill the first column
#     for j in range(len(token2) + 1):
#         distance_matrix[0][j] = j

#     # Fill the rest of the matrix
#     for i in range(1, len(token1) + 1):
#         for j in range(1, len(token2) + 1):
#             if token1[i - 1] == token2[j - 1]:
#                 distance_matrix[i][j] = distance_matrix[i - 1][j - 1]
#             else:
#                 distance_matrix[i][j] = 1 + min(distance_matrix[i - 1][j - 1],
#                                                 distance_matrix[i - 1][j], distance_matrix[i][j - 1])

#     # Get the distance
#     distance = distance_matrix[-1][-1]

#     return distance


# assert levenshein_distance("hi  ", "hello") == 4.0
# print(levenshein_distance("hola", "hello"))

# Q5. -> A
# def check_the_number(N):
#     list_of_numbers = []
#     result = ""
#     for i in range(1, 5):
#         list_of_numbers.append(i)

#     if N in list_of_numbers:
#         result = "True"
#     if N not in list_of_numbers:
#         result = "False"
#     return result


# N = 7
# assert check_the_number(N) == "False"
# N = 2
# results = check_the_number(N)
# print(results)

# Q6. -> C
# def my_function(data, max, min):
#     result = []
#     for i in data:

#         if i < min:
#             result.append(min)
#         elif i > min:
#             result.append(max)
#         else:
#             result.append(i)

#     return result


# my_list = [5, 2, 5, 0, 1]
# max = 1
# min = 0
# assert my_function(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
# my_list = [10, 2, 5, 0, 1]
# max = 2
# min = 1
# print(my_function(max=max, min=min, data=my_list))

# Q7. -> A
# def my_function(x, y):

#     x.extend(y)

#     return x


# list_num1 = ["a", 2, 5]
# list_num2 = [1, 1]
# list_num3 = [0, 0]
# assert my_function(list_num1, my_function(list_num2, list_num3)) == [
#     "a", 2, 5, 1, 1, 0, 0]
# list_num1 = [1, 2]
# list_num2 = [3, 4]
# list_num3 = [0, 0]
# print(my_function(list_num1, my_function(list_num2, list_num3)))

# Q8. -> C
# def my_function(n):
#     min = n[0]
#     for i in n:
#         if i < min:
#             min = i
#     return min


# my_list = [1, 22, 93, -100]
# assert my_function(my_list) == -100

# my_list = [1, 2, 3, -1]
# print(my_function(my_list))

# Q9. -> D
# def my_function(n):
#     max = n[0]
#     for i in n:
#         if i > max:
#             max = i
#     return max


# my_list = [1001, 9, 100, 0]
# assert my_function(my_list) == 1001

# my_list = [1, 9, 9, 0]
# print(my_function(my_list))

# Q10. -> C
# def My_function(intergers, number=1):
#     return any(
#         element == number for element in intergers
#     )


# my_list = [1, 3, 9, 4]
# assert My_function(my_list, -1) == False

# my_list = [1, 2, 3, 4]
# print(My_function(my_list, 2))

# Q11. -> A
# def my_function(list_nums=[0, 1, 2]):
#     var = 0
#     for i in list_nums:
#         var += i
#     return var / len(list_nums)


# assert my_function([4, 6, 8]) == 6
# print(my_function())

# Q12. -> A
# def my_function(data):
#     var = []
#     for i in data:
#         if i % 3 == 0:
#             var.append(i)
#     return var


# assert my_function([3, 9, 4, 5]) == [3, 9]
# print(my_function([1, 2, 3, 5, 6]))

# Q13. -> C
# def my_function(y):
#     var = 1
#     while (y > 1):
#         var = var * y
#         y = y - 1
#     return var


# assert my_function(8) == 40320
# print(my_function(4))

# Q14. -> C
# def my_function(x):
#     return x[::-1]


# x = 'I can do it'
# assert my_function(x) == 'ti od nac I'
# x = 'apricot'
# print(my_function(x))

# Q15. -> C
# def function_helper(x):
#     # if x > 0 return 'T' else return 'N'
#     return 'T' if x > 0 else 'N'


# def my_function(x):
#     res = [function_helper(x) for x in data]
#     return res


# data = [10, 0, -10, -1]
# assert my_function(data) == ['T', 'N', 'N', 'N']
# data = [2, 3, 5, -1]
# print(my_function(data))

# Q16. -> A
# def function_helper(x, data):
#     for i in data:
#         # if x == i return 0
#         if x == i:
#             return 0
#     return 1


# def my_function(data):
#     res = []
#     for i in data:
#         if function_helper(i, res):
#             res.append(i)
#     return res


# lst = [10, 10, 9, 7, 7]
# assert my_function(lst) == [10, 9, 7]

# lst = [9, 9, 8, 1, 1]
# print(my_function(lst))
