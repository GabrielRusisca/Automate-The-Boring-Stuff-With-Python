import pyinputplus as pyin
from time import sleep

def main():
    title = 'Welcome to Gabriel\'s Gourmet Burgery'
    print('~'*len(title))
    print(title)
    print('~'*len(title))
    final_cost = 0
    while True:    
        cost = 0
        bread = pyin.inputMenu(prompt='Which type of bread do you want:\n', choices=['Wheat $1', 'White $2', 'Sourdough $3'], numbered=True)
        cost += int(bread[-1])
        protein = pyin.inputMenu(prompt='Which type of protein do you want:\n', choices=['Chicken $3','Turkey $4','Ham $3','Tofu $5'], numbered=True)
        cost += int(protein[-1])
        add_cheese = pyin.inputYesNo(prompt='Would you like to add cheese [Y/N]: ')
        if add_cheese == 'yes':
            cheese = pyin.inputMenu(prompt='Which type of cheese:\n',choices=['cheddar $1','Swiss $2', 'Mozzarella $1'], numbered=True)
            cost += int(cheese[-1])
        add_extra = pyin.inputYesNo('Would you like o add mayo, mustard, lettuce and tomato $1 [Y/N]: ')
        if add_extra == 'yes':
            cost += 1
        print(10*'~','Your tab will be $'+ str(cost),10*'~')
        decision_list = ['Cancel this sandwich and order a new one', 'Repeat the last chosen sandwich 1 or + times and make a new sandwich', 'Repeat the last chosen sandwich 1 or + times and close your tab','Cancel your order and close your tab']
        decision = pyin.inputMenu(prompt='Would you like to:\n',choices= decision_list, numbered=True)
        if decision_list.index(decision) == 0:
            continue
        elif decision_list.index(decision) == 1:
            final_cost += cost * pyin.inputInt('How many sandwichs of this kind would you like: ',min=1)
            continue
        elif decision_list.index(decision) == 2:
            final_cost += cost * pyin.inputInt('How many sandwichs of this kind would you like: ',min=1)
            break
        else:
            print('Thank you for passing by, you\'re welcome to come back anytime!')
            return
    print(10*'~',f'Your bill tonight was ${final_cost}! Pay Up!!!',10*'~')
    sleep(1)
    print('*')
    sleep(1)
    print('*')
    sleep(1)
    print('*')
    sleep(1)
    print('PAAAAYYYY UUUUUUUUPPPP DON\'T RUNNNN AWAYYYYY')



if __name__ == '__main__':
    main()