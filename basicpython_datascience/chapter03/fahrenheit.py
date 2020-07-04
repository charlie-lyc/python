
def main():
    cel_to_fah()


def cel_to_fah():
    cel_temp = input('Enter celsius temprature : ')
    fah_temp = (float(cel_temp) * 1.8)+32
    print('Fahrenheit temprature :', fah_temp)


if __name__ == '__main__':
    main()
