import os 
import time as ss

def clear():
    if os.name == "nt":
        os.system('cls')  # For Windows
    else:    
        os.system('clear')  # For Linux/OS X

def trapesium():
    clear()

    print("""
+=========================+
|       *Trapesium*       |
+=========================+
| [1] Menghitung Luas     |  
| [2] Menghitung Keliling |  
| [0] Exit                |  
+=========================+
|    Pilih Salah Satu!    |
+=========================+
    """)

    code = int(input("Pilih: "))

    if code == 1:
        clear()
        print("""
+==================================+
|    *Menghitung Luas Trapesium*   |
+==================================+
| (a,b) = Sisi Sejajar, t = Tinggi |
| L = Luas                         |  
+==================================+
| Rumus :                          | 
|    L = 1/2 x (a + b) x t         |
+==================================+
        """)

        a = int(input("Masukan a: "))
        b = int(input("Masukan b: "))
        t = int(input("Masukan t: "))

        L = (a+b) * t / 2
        print()
        print("Luas Trapesium: " + str(int(L)) + " cm2")
        print("Jadi Luas Trapesium Adalah, " + str(int(L)) + " cm2")
        print()
        
    elif code == 2:
        clear()  

        print("""
+======================================+
|   *Menghitung Kelililng Trapesium*   |       
+======================================+
| s = sisi, K = Keliling               | 
+======================================+
| Rumus :                              |
|    K = s + s + s + s                 |
|    K = AB + BD + CD + DA             | 
+======================================+        
        """)  

        ab = int(input("Masukan Sisi AB: "))
        bc = int(input("Masukan Sisi BC: "))
        cd = int(input("Masukan Sisi CD: "))
        da = int(input("Masukan Sisi DA: "))

        K = ab + bc + cd + da
        print()
        print("Keliling Trapesium : " + str(int(K)) + " cm")
        print("Jadi Keliling Trapesium Adalah, " + str(int(K)) + " cm")
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
        clear()
        print("error")
        sleep(2)
        trapesium()

trapesium()        


