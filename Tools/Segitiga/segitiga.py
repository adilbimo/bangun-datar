import os
import time as sc 

def clear():
    if os.name == "nt":
        os.system('cls')  # For Windows
    else:    
        os.system('clear')  # For Linux/OS X



def persegiPanjang():
    print("""
+=========================+
|       *Segitiga*        |   
+=========================+
| [1] Menghitung Luas     |
| [2] Menghitung Keliling |
| [0] Exit                |              
+=========================+
|    Pilih Salah Satu !   |  
+=========================+
    """)

    code = int(input("Pilih: "))

    if code == 1:
        clear()

        print("""
+============================+
| *Menghitung Luas Segitiga* |
+============================+
| a = Alas, t = Tinggi,      |
| L = Luas                   |
+============================+
| Rumus :                    |
|    L = 1/2 x a x t         |
+============================+
        """)

        a = int(input("Masukan Alas: "))
        t = int(input("Masukan Tinggi: "))

        L = int(0.5 * a * t)
        print()
        print("Hasil = " + str(int(L)) + " cm2")
        print("Jadi Luas Segitiga Adalah, " + str(int(L)) + " cm2")
        print()

    elif code == 2:
        clear()

        print("""
+================================+
| *Menghitung Keliling Segitiga* |
+================================+
| a, b, c = Sisi, K = Keliling   |   
+================================+
| Rumus :                        |
|    K = a + b + c               |
+================================+
        """)

        a = int(input("Masukan Sisi a: "))
        b = int(input("Masukan Sisi b: "))
        c = int(input("Masukan Sisi c: "))

        K = int(a + b + c)

        print()
        print("Hasil = " + str(K) + " cm")
        print("Jadi Keliling Persegi Panjang Adalah, " + str(K) + " cm")
        print()
        
    elif code == 0:
        text = "bye "
        for i in range(11):
            print(text ,  end=" ")

            for a in range(i + 1):
                print(". " ,  end=" ")
                sc.sleep(0.4)
                clear()
            print()
    else:
        print("error")
        sc.sleep(2)
        persegiPanjang()

persegiPanjang()