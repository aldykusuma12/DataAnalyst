nama = input('masukan nama anda: ')
berat =  int(input('masukan berat badan (dalam kg): '))
tinggi = int(input('masukan tinggi badan (dalam cm): '))

BMI = (berat/(tinggi*tinggi)) * 10000
print(BMI)
if BMI > 0:
    if BMI < 18.5:
        print(nama +', anda kekurangan berat badan')
    elif BMI < 24.9:
        print(nama +', anda normal')
    elif BMI < 29.9:
        print(nama +', anda kelebihan berat badan')
    else:
        print(nama +', anda kegemukan')
else:
    print('masukin yang bener')
