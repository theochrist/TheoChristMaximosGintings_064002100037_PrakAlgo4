print("*******PROGRAM KONVERSI BILANGAN*******")
print("1. Bilangan Desimal ke Bilangan Biner")
print("2. Bilangan Biner ke Bilangan Desimal")
print("3. Exit")
print("***************************************")
xinput = input("Silahkan Pilih Menu : ")

if xinput == '1' :
    print ("Program Hitung bilangan Desimal ke Biner")
    number = int(input("Masukkan Bilangan Desimal : "))
    biner = ""

    while number > 0 :
        modulo = number % 2

        if modulo == 1 :
            biner = "1" + biner
        else :
            biner = "0" + biner
        number = number // 2
    print ("Nilai Biner Adalah ", biner)

elif xinput == '2' :
    print ("Program Hitung bilangan Biner ke Desimal")
    biner = input("Masukkan Bilangan Biner : "'')
    desimal = 0
    pangkat = len(biner)-1

    for i in range(len(biner)) :
        idesimal = int(biner[i]) * 2 ** pangkat
        desimal += idesimal
        pangkat -= 1
    print("Nilai Desimal Adalah ", desimal)

elif xinput == '3' :
    print("program dihentikan !!!")
    exit()
else :
    print("Inputan Salah")
    print("program dihentikan !!!")
    exit()