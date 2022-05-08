#Prashant Pramodkumar Mall
#FE520WS - HW02

# Notice: do not change these function name
from operator import truediv
from xml.etree.ElementTree import tostring


def is_palindrome(x):
    # Check if 'x' is an integer data type
    if (type(x) != int):
        return "The input provided is not an Integer."
    # Convert Int to Str and then reverse
    reverse = list(str(x))
    reverse.reverse()
    reverse = "".join(reverse)
    # Check if the reverse is same as orignal input
    if (str(x) == reverse):
        return True
    else:
        return False


def is_anagrams(s, t):
    # Check if 's' & 't' are strings
    if (type(s) != str or type(t) != str):
        return "The input provided is not in String format."
    # If lenght is not same, return false as anagram not possible
    if (len(s) != len(t)):
        return False

    dictOne = {}
    dictTwo = {}
    # Loop through both strings and create a dict with alphabets as keys and number of occurance as value
    for letter in s:
        if letter in dictOne:
            dictOne[letter] = dictOne[letter] + 1
        else:
            dictOne[letter] = 1

    for letter in t:
        if letter in dictTwo:
            dictTwo[letter] = dictTwo[letter] + 1
        else:
            dictTwo[letter] = 1
    # Compare dict
    if (sorted(dictOne) == sorted(dictTwo)):
        return True
    else:
        return False


def top_k_words(s, k):
    #Check if input is of correct format
    if(type(s) != str and type(k) != int):
        return ("The input provided is not in correct format.")

    temp = []
    # Clean data, keep only alplhabents and spaces
    for letter in s:
        if(letter.isalpha() == True or letter == " "):
            temp.append(letter)

    temp = (("".join(temp)).split(" "))

    dictWord = {}
    # Loop through to create a dict
    for word in temp:
        if(word != ''):
            if word in dictWord:
                dictWord[word] = dictWord[word] + 1
            else:
                dictWord[word] = 1

    newList = []
    # Sort the dict according to highest value 
    topNumbers = dict(
        sorted(dictWord.items(), key=lambda item: item[1], reverse=True))
    for i in topNumbers.keys():
        newList.append(i)

    return(newList[:k])


def gradient_descent(x, y, m, c, epochs, L=0.001):
    # CODE FROM SUBMISSION COMMENT 
    # create pairs of (xi,yi) by using dictionary:
    keyValue = {x[epochs][0]: y[epochs] for epochs in range(len(x))}
    loop = 0
    while loop < epochs:
        Dw = []
        Dc = []
        for key, value in keyValue.items():
            y_pred = key * m + c
            valueb = key*(y_pred - value)
            Dw.append(valueb)
            valuec = y_pred - value
            Dc.append(valuec)

        dw = sum(Dw)/len(Dw)
        dc = sum(Dc)/len(Dc)
        m = m - L * dw
        c = c - L * dc
        loop += 1
    return(m, c)


if __name__ == "__main__":

    # Test Question 1

    print("\nQ1")
    q1_test1 = 121
    q1_test2 = -121
    q1_test3 = 0
    q1_answer1 = is_palindrome(q1_test1)
    q1_answer2 = is_palindrome(q1_test2)
    q1_answer3 = is_palindrome(q1_test3)
    print(q1_answer1)
    print("right answer: True")
    print("--------------")
    print(q1_answer2)
    print("right answer: False")
    print("--------------")
    print(q1_answer3)
    print("right answer: True")

    print("\nQ2")
    q2_test1_s = "anagram"
    q2_test1_t = "nagaram"
    q2_answer1 = is_anagrams(q2_test1_s, q2_test1_t)
    print(q2_answer1)
    print("right answer: True")

    print("--------------")
    q2_test2_s = "python"
    q2_test2_t = "py"
    q2_answer2 = is_anagrams(q2_test2_s, q2_test2_t)
    print(q2_answer2)
    print("right answer: False")
    print("--------------")

    # test question 3
    print("\nQ3")
    q3_test1_s = "   i love python, he    love coding python. the course is about python. "
    q3_test1_k = 2
    q3_answer = top_k_words(q3_test1_s, q3_test1_k)
    print(q3_answer)
    print("right: answer:")
    print("['python', 'love']")

    print("\nQ4")

    x = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    m = 0
    c = 0
    q4_epochs200 = 200
    q4_epochs500 = 500
    q4_epochs1000 = 1000
    q4_epochs2000 = 2000
    q4_epochs3000 = 3000
    q4_answer1 = gradient_descent(x, y, m, c, q4_epochs200)
    q4_answer2 = gradient_descent(x, y, m, c, q4_epochs500)
    q4_answer3 = gradient_descent(x, y, m, c, q4_epochs1000)
    q4_answer4 = gradient_descent(x, y, m, c, q4_epochs2000)
    q4_answer5 = gradient_descent(x, y, m, c, q4_epochs3000)
    print(q4_answer1)
    print("right answer:")
    print("17.724810647355827, 22.97599012903927")
    print("--------------")
    print(q4_answer2)
    print("right answer:")
    print("35.97890301691016, 46.54235227399102")
    print("--------------")
    print(q4_answer3)
    print("right answer:")
    print("52.816639894324545, 68.05971340716786")
    print("--------------")
    print(q4_answer4)
    print("right answer:")
    print("64.56549666509812, 82.46678636085996")
    print("--------------")
    print(q4_answer5)
    print("right answer:")
    print("67.42648874428104, 85.32444456113602")
    print("--------------")
