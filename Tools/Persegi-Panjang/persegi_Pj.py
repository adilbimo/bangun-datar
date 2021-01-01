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
| *Persegi Panjang*       |  
+=========================+
| [1] Menghitung Luas     |  
| [2] Menghitung Keliling |
| [0] Exit                |  
+=========================+
| Pilih Salah Satu !      |
+=========================+
    """)

    code = int(input("Pilih: "))

    if code == 1:
        clear()

        print("""
+===================================+
| *Menghitung Luas Persegi Panjang* |
+===============+===================+
| p = Panjang, l = Lebar, L = Luas  |
+===================================+
| Rumus :                           |
|    L = p x l                      |
+===================================+
        """)

        p = int(input("Masukan Panjang: "))
        l = int(input("Masukan Lebar: "))

        L = int(p * l)

        print()
        print("Hasil = " + str(L) + " cm2")
        print("Jadi Luas Persegi Panjang Adalah, " + str(L) + " cm2")
        print()
    elif code == 2:
        clear()

        print("""
+=======================================+
| *Menghitung Keliling Persegi Panjang* |
+=====================+=================+
| p = panjang, l = Lebar, K = Keliling  |
+=======================================+
| Rumus :                               |  
|    K = 2 x (p + l)                    |      
+=======================================+
        """)

        p = int(input("Masukan Panjang: "))
        l = int(input("Masukan Lebar: "))

        K = int(2 * (p + l))

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
                sleep(0.4)
                clear()
            print()
    else:
        print("error")
        sc.sleep(2)
        persegiPanjang()

persegiPanjang()