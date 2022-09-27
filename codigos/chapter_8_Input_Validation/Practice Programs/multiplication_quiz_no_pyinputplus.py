from time import sleep, time
from random import randint

def main() -> None:
    title_message: str = 'Welcome to the Multiplication Game!!!'
    print('-'*len(title_message))
    print(title_message)
    print('-'*len(title_message))
    while True:
        try:
            msg: str = 'Choose the number of questions, min = 1 and max = 37: '
            n_questions: str = input(msg).strip()
            if not n_questions.isdecimal() or int(n_questions) not in list(range(1,38)):
                raise ValueError
            n_questions: int = int(n_questions)
            break
        except ValueError:
            print(f'"{n_questions}" is not an allowed value.')
        finally:
            print('-'*len(msg+str(n_questions)))
    correct: int = 0
    correct_answer = -1
    time_limit: int = 8
    done: list[int] = [-1]
    for question_n in range(1,n_questions + 1):
        while correct_answer in done:
            n1: int = randint(0,9)
            n2: int = randint(0,9)
            correct_answer: int = n1 * n2
        done.append(correct_answer)
        wrong: int = 0
        tempo: float = time()
        for i in range(3):
            answer: str = input(f'{question_n}: {n1} X {n2} = ').strip()
            tempo2: float = time()
            tempo_dif: float = tempo2 - tempo
            if tempo_dif > time_limit:
                print(f'Acabou seu limite de tempo de {time_limit} segundos')
                wrong += 1
                break
            if answer.isdecimal():
                if int(answer) == correct_answer:
                    print('Correct!')
                    correct += 1
                    sleep(1)
                    break
            print('Incorrect!')
            wrong += 1
        print('-'*len('nn: n X n = nn'))
    print('========'+'RESULTADOS'+'========')
    print('Number of questions:\t', n_questions,'\nCorrects:\t\t',correct,'\nWrongs:\t\t\t', wrong)
    return


if __name__ == '__main__':
    main()
