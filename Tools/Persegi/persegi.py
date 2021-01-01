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
|       *Persegi*         |
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
+===========================+
| *Menghitung Luas Persegi* |
+===========================+
| s = Sisi, L = Luas        |
+===========================+
| Rumus :                   |  
|    L = s x s              |
+===========================+
        """)

        s = int(input("Masukan Sisi: "))

        L = int(s * s)
        print()
        print("Hasil = " + str(L) + " cm2")
        print("Jadi Luas Persegi Adalah, " + str(L) + " cm2")
        print()

    elif code == 2:
        clear()

        print("""
+===============================+
| *Menghitung Keliling Persegi* |
+===============================+
| s = Sisi, K = Keliling        |
+===============================+
| Rumus :                       |
|    K = s + s + s + s          |
+===============================+
        """)

        s = int(input("Masukan Sisi: "))

        K = int(s + s + s + s)

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
                sleep(0.3)
                clear()
            print()
    else:
        print("error")
        sc.sleep(2)
        persegiPanjang()

persegiPanjang()