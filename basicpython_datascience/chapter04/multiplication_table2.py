def main():
    multi_table()


def multi_table():
    while True:
        num = int(input('Enter a integer number 1~9.: '))
        if num == 0:
            print('Finish mulltiplications.')
            exit()
        elif 0 > num or num > 9:
            continue
        else:
            print(f'Start {num} multiplications.')
            for i in range(1, 10):
                print(f'{num} X {i} = {num * i}')


if __name__ == '__main__':
    main()
