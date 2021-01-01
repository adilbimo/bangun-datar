import os 
import time as ss

def clear():
    if os.name == "nt":
        os.system('cls')  # For Windows
    else:    
        os.system('clear')  # For Linux/OS X

def jajarGenjang():
    clear()

    print("""
+=========================+
|     *Jajar Genjang*     |
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
| *Menghitung Luas Jajar Genjang* |
+=================================+
| a = sisi alas, dan t = tinggi   |  
| L = Luas                        |  
+=================================+
| Rumus :                         | 
|    L = a x t                    |
+=================================+
        """)

        a = int(input("Masukan Alas: "))
        t = int(input("Masukan Tinggi:"))

        L = (a * t)
        print()
        print("Luas Jajar Genjang: " + str(int(L)) + " cm2")
        print("Jadi Luas Jajar Genjang Adalah, " + str(int(L)) + " cm2")
        print()
        
    elif code == 2:
        clear()  

        print("""
+======================================+
| *Menghitung Kelililng Jajar Genjang* |       
+======================================+
| a = sisi alas, b = sisi miring       | 
| K = Keliling                         | 
+======================================+
| Rumus :                              |
|    K = 2 x (a + b)                   |
+======================================+        
        """)  

        a = int(input("Masukan Alas: "))
        b = int(input("Masukan Sisi Miring: "))

        K = 2 * (a + b)
        print()
        print("Keliling Jajar Genjang : " + str(int(K)) + " cm")
        print("Jadi Keliling Jajar Genjang Adalah, " + str(int(K)) + " cm")
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
        jajarGenjang()

jajarGenjang()        


