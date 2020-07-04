
def main():
    cel_temp = input('Enter celsius temprature : ')
    cel_to_fah(cel_temp)


def cel_to_fah(cel_temp):
    fah_temp = (float(cel_temp) * 1.8)+32
    print('Fahrenheit temprature :', fah_temp)


if __name__ == '__main__':
    main()
