import os 
import time as ss

def clear():
    if os.name == "nt":
        os.system('cls')  # For Windows
    else:    
        os.system('clear')  # For Linux/OS X

def belah_Ketupat():
    clear()

    print("""
+=========================+
|     *Belah Ketupat*     |
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
+=================================+
| *Menghitung Luas Belah Ketupat* |
+=================================+
| d = Diagonal, L = Luas          |  
+=================================+
| Rumus :                         | 
|    L = 1/2 x d1 x d2            |
|    L = 1/2 x AC x BD            |
+=================================+
        """)

        d1 = int(input("Masukan Diagonal 1: "))
        d2 = int(input("Masukan Diagonal 2: "))

        L = 1*d1/2*d2
        print()
        print("Luas Belah Ketupat: " + str(int(L)) + " cm2")
        print("Jadi Luas Belah Ketupat Adalah, " + str(int(L)) + " cm2")
        print()
        
    elif code == 2:
        clear()  

        print("""
+======================================+
| *Menghitung Kelililng Belah Ketupat* |       
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
        print("Keliling Belah Ketupat : " + str(int(K)) + " cm")
        print("Jadi Keliling Belah Ketupat Adalah, " + str(int(K)) + " cm")
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
        belah_Ketupat()

belah_Ketupat()        


