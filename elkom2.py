list1 = list(map(int,input("\nMasukkan angka : ").strip().split()))

Ganjil, Genap = 0, 0

for num in list1:
    if num % 2 == 0:
        Genap += 1
    else:
        Ganjil += 1

if Genap == 0 :
    print("Tidak ada bilangan genap")
else :
    print("Terdapat bilangan genap")