# import matplotlib.pyplot as plt

# myString = "Hello world"
# print(myString);

# newString = input()
# print(newString)

# firstNumber = int(input())
# print(firstNumber)

# Add 2 to the first number
# newNumber = firstNumber + 2
# print(newNumber)

# creating a list
# x = [1,2,3,4]
# y = [1,2,1,2]
# Creates a new figure
# plt.figure()
# Plot the x data vs the y data
# plt.plot(x,y)
# plt.xlabel('x values')
# plt.ylabel('y values')

# Creating list of strings
# listA = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# Creating list of integers
# listB = [1,2,3,4,5,6,7,8,9,10,11,12]

# Get the length of list A
# lengthOfListA = len(listA)
# Get the length of list B
# lengthOfListB = len(listB)
# Print all of list A
# print(listA)
# Print all of list B
# print(listB)
# Print all of list A and B
# print(listA,listB)

# Print each element in list A row by row
# for i in range(lengthOfListA):
#     print(listA[i])

# Problem 1
# Find the largest number in the list below
# listC = [7,-1,3,11,-2,-1,10]

# Problem 2
# Find the smallest even number in the list below
# listD = [8,1,2,-9,42,-8,11,-13,23,-12,31,16]

# Problem 3
# Find the product of the largest odd and smallest odd number in the list below
# listE = [7,-1,3,11,-2,-1,10,8,1,2,-9,42,-8,11,-13,23,-12,31,16]

# Problem 4
# Sum all the values found in the list of strings
# listF = ['11', '-22', '33', '-44', '55', '-66', '77', '-88', '99']

target_grade = float(input('Enter target final grade %: '))
current_grade = float(input('Enter current grade %: '))
final_weight = float(input('Enter final weight %: '))
current_weight = 100 - final_weight
grade = ((target_grade * 100) - (current_grade * current_weight)) / final_weight
print('final exam grade %: ', grade)