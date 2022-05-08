# 1 => Print

# 1. Define an arbitrary string variable, and print it.
numOfCard = "Fifty Two"
print(numOfCard)

# 2.Define a string (I’m a student), print it.
student = "I'm a student"
print(student)

# 3.Defind a string:
# (How do you think of this course?
# Describe your feeling of this course)
# print it in multiple line.
myFeelings = "FE520,\nAn amazing course taught in a very simple manner.\nThis is my first elective from FE."
print(myFeelings)

print("\n----------------------------------------------------\n")
# 2=> Operator

a = 100
b = 9

# 1. Assign the result of a+b to c, print c out.
c = a+b
print(c)

# 2. Print the result of a/b.
print(a/b)

# 3. Print the integer part of a/b. (Hint: modulo operations)
print((a//b))

# 4. Print the remainder part of a/b. (Hint: modulo operations)
print(a % b)

# 5. Print the result of ab.
print(a*b)

# 6. Determining if a is unequal to b and print the True/False using logic operators.
print(a == b)

# 7. Determining if a is greater to b and print the True/False using logic operators.
print(a > b)

print("\n----------------------------------------------------\n")
# 3=> List Practice

# 1. Define a list Name it List A, whose items should include integer, float, and string. Please notice the length of the list should be greater than 5.
List_A = [22, 14.7, "Prashant", "Mall", 10459371, "Go Ducks"]

# 2. Using extend and append to add another list (Name it List B) to List A, conclude the difference.
List_B = [2, 16, 2022]
List_A.extend(List_B)
print(List_A)
List_A.append(List_B)
print(List_A)

# 3. Insert a string (’FE520’) to the second place of List A, and delete it after that.
List_A.insert(2, "FE520")
print(List_A)
List_A.remove("FE520")
print(List_A)

# 4. Return and delete the last element in the List A, and print the new list.
lastElem = List_A.pop(-1)
print(List_A)

# 5. Return a new list (Name is List C), slicing the List A from the 3rd element to the end.
List_C = List_A[3:]
print(List_C)

# 6. Double the size of List C using ‘+’.
List_C = List_C + List_C
print(List_C)

# 7. Reverse your sequence of List C.
List_C.reverse()
print(List_C)

print("\n----------------------------------------------------\n")
# 4 =>Practice Dictionary

# 1. Define a string of ‘python is an interpreted dynamic programming language’
newString = 'python is an interpreted dynamic programming language'

# 2. Create a list (list A) of single-character strings out of the above string in 1 (e.g.,’hello’->[’h’, ’e’, ’l’, ’l’, ’o’]).
A = list(newString)

# 3. Write a loop to count the number of each unique character into dictionary, where your keys are characters in the list A, and value is the count corresponding to each character. Your result should look like : {’h’: 1, ’e’: 1, ’l’: 2, ’o’: 1}.
dictCount = {}
for char in newString:
    if char in dictCount:
        dictCount[char] += 1
    else:
        dictCount[char] = 1
print(dictCount)

# 4. Print the characters which only show once (count=1) in the output dictionary (Hint: use loop and if statement).
for char in dictCount:
    if dictCount[char] == 1:
        print(char)

print("\n----------------------------------------------------\n")
# 5 => Loop Practice: Sum (15 pts)

# Write a loop for calculate the average of a list.
# For example: if you have a list A = [1, 2, 3, 4, 5, 6], after your loop calculation,
# you need to get a total num equals to 3.5.

List_Loop = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
sum = 0
for elem in List_Loop:
    sum += elem
average = sum/len(List_Loop)
print(average)

print("\n----------------------------------------------------\n")
# 6 => Loop Practice: Gradient Decent

# Dataset
x = [0.18, 1.0, 0.92, 0.07, 0.85, 0.99, 0.87]
y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]

# Variables
w = 0
c = 0
L = 0.001
number_of_iterations = 200

Dw = [0]*len(x)
Dc = [0]*len(x)

y_pred = [""]*len(x)

for index in range(0, number_of_iterations):
    for i in range(len(x)):
        y_pred[i] = (x[i]*w)+c
        Dw[i] = x[i]*(y_pred[i] - y[i])
        Dc[i] = y_pred[i]-y[i]

    totalSum_dw = 0
    for sumDw in Dw:
        totalSum_dw += sumDw

    totalSum_dc = 0
    for sumDc in Dc:
        totalSum_dc += sumDc

    dw = totalSum_dw/len(Dw)
    dc = totalSum_dc/len(Dc)

    w = w - L * dw
    m = w

    c = c - L * dc

print(w)
print(c)
