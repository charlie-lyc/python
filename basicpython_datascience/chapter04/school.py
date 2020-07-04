
def main():
    school_is()


def school_is():
    birth_year = int(input('Enter birth year : '))
    age = 2020 - birth_year + 1
    if 20 <= age <= 26:
        print('University')
    elif 17 <= age < 20:
        print('High Shchool')
    elif 14 <= age < 17:
        print('Middle School')
    elif 8 <= age < 14:
        print('Elementry School')
    else:
        print('Not student')


if __name__ == '__main__':
    main()
