# write your code here
import random
import math


def simple_operations(number1, number2, sign):
    if sign == '+':
        return number1 + number2
    elif sign == '-':
        return number1 - number2
    elif sign == '*':
        return number1 * number2


def calculate_square(number):
    return number * number


def result_compare(calculated_result):
    s_marks = 0
    while True:
        try:
            user_result = int(input())
            if user_result == calculated_result:
                s_marks += 1
                print('Right!')
                return s_marks
            else:
                print('Wrong!')
                return 0
        except ValueError:
            print("Incorrect format.")


# program starts here
student_marks = []
while True:
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    try:
        selected_operation = int(input())
        break
    except ValueError:
        print("Incorrect format.")
if selected_operation == 1:
    for i in range(1, 6):
        number_1 = random.randint(2, 9)
        number_2 = random.randint(2, 9)
        operations = ['+', '-', '*']
        selected_sign = random.choice(operations)
        print(f'{number_1} {selected_sign} {number_2}')
        result = simple_operations(number_1, number_2, selected_sign)
        mark_obtained = result_compare(result)
        student_marks.append(mark_obtained)
if selected_operation == 2:
    for i in range(1, 6):
        number_3 = random.randint(11, 29)
        print(number_3)
        sqrt_result = calculate_square(number_3)
        mark_obtained = result_compare(sqrt_result)
        student_marks.append(mark_obtained)
total_marks = sum(student_marks)
if selected_operation == 1:
    description = "simple operations with numbers 2-9"
else:
    description = "integral squares of 11-29"
print(f"Your mark is {total_marks}/5. Would you like to save the result? Enter yes or no.")
response = input()
response = response.upper()
if response == 'YES' or response == 'Y':
    print("What is your name?")
    name = input()
    with open('results.txt', 'a') as file:
        file.write(name + f': {total_marks}/5 in level {selected_operation}({description}).')
        file.write('\n')
        print(f'The results are saved in results.txt".')
else:
    exit()
