
def main():
    multi_table()


def multi_table():
    num = 0
    while 0 >= num or num > 9:
        num = int(input('Enter a number : '))
    print(f'Start {num} multiplications.')
    for i in range(1, 10):
        print(f'{num} X {i} = {num * i}')


if __name__ == '__main__':
    main()
