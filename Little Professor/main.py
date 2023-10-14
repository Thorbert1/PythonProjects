import random

questions = 10
numbers_to_add = 4

def main():
    answer_sheet = generateQuestions() 
    print(answer_sheet)
    for question in range(len(answer_sheet)):
        ask_question(question, answer_sheet)

        answer = input("Answer: ")
        if check_answer(answer, answer_sheet[question][numbers_to_add]):
            print("EEE")
            wrongAns = wrongAns + 1

def generateQuestions() -> list:
    ls = [[random.randint(0, 9) for i in range(numbers_to_add)] for j in range(questions)]
    for item in ls:
        sum = 0
        for ele in range(len(item)):
            sum = sum + int(item[ele])
        item.append(sum)
    return ls

def ask_question(num, ans):
    print(f"{convert_to_question(ans[num])}")

def check_answer(a, b):
    if a == b:
        return True
    else: return False

def convert_to_question(ls):
    str = ls[0]
    for item in range(len(ls) - 2): #(len(ls) - 2) is to compensate for answer index and first list item
        str = f"{str} + {ls[item + 1]}"      
    return str

if __name__ == "__main__":
    main()