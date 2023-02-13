cats = [{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]

def main():
    c = 0
    while True:
        print(c,end=' ->')
        c += 1
        if c == 1000: 
            print('1000 -> byebye')
            break

if __name__ == '__main__':
    main()