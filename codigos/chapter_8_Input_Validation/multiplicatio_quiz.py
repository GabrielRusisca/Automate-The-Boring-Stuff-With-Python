import pyinputplus as pyin
from random import randint
from time import sleep

def main():
    correct_answer = -1
    correct_answers = [-1]
    title_message = 'Welcome to the Multiplication Game!!!'
    print('-'*len(title_message))
    print(title_message)
    print('-'*len(title_message))
    number_questions = pyin.inputInt('Choose the number of questions: ', min=1, lessThan=38)
    print(len('Choose the number of questions: '+ str(number_questions))*'-')
    correct = 0
    for question_number in range(number_questions):
        while correct_answer in correct_answers:        
            n1 = randint(0,9)
            n2 = randint(0,9)
            correct_answer = n1 * n2
        correct_answers.append(correct_answer)
        try:
            pyin.inputStr(prompt=f'{question_number + 1}: {n1} X {n2} = ',strip=' ', allowRegexes=[f'^{correct_answer}$'],blockRegexes=[(r'.*','>>> Incorrect!')], limit= 3, timeout=10)
        except pyin.RetryLimitException:
            print('Incorrect for the third time! Next question!')
        except pyin.TimeoutException:
            print('10 Timeout limit surpassed! Next question!')
        else:
            print('>>> Correct!!!')
            correct += 1
        sleep(1)
        print('-'*len('questions answeredaa'))
        print(f'{question_number + 1} questions answered\n{correct} correct answers\n{question_number + 1 - correct} wrong answers')
        print('-'*len('nn questions answered'))
    if correct == number_questions:
        print(f'{"Congratulations, you are a master mathematician!":-^60}')
    elif correct/number_questions >= 0.8:
        print('Almost there, try again and don\'t give up!')
    elif correct/number_questions >= 0.6:
        print('That\'s a good result but you should practice more!')
    else:
        print('That\'s a bad score, study more and try again!')
    return len(correct_answers)

if __name__ == '__main__':
    main()
