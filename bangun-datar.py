# Coded By Bimo :v
# Follow My Instagram : @piw0.deb


import os
from time import sleep

def clear():
    if os.name == "nt":
        os.system('cls')  # For Windows
    else:    
        os.system('clear')  # For Linux/OS X

def bangun_datar():

    clear()

    print("""

+=====================+
|    *Bangun Datar*   | 
+=====================+
|  *Menghitung Luas*  |
|         &           |  
|     *Keliling*      |
+=====================+  
| [1] Persegi Panjang |
| [2] Persegi         |
| [3] Lingkaran       |
| [4] Segitiga        |  
| [5] Jajar Genjang   |    
| [6] Belah Ketupat   |
| [7] Layang Layang   |  
| [8] Trapesium       |      
| [0] Exit            |
|                     |
+=====================+
| Pilih Salah Satu !  |
+=====================+
    """)

    pilih = int(input("Pilih >>> "))

    if pilih == 1:
        clear()

        def path():
            if os.name == "nt":                    # For Windows
                os.chdir("Tools\Persegi-Panjang")
                os.system("python persegi_Pj.py")
            else:                                   # For Linux/ OS X
                os.chdir("Tools\Persegi-Panjang")
                os.system("python3 persegi_Pj.py")          
        path()

    elif pilih == 2:
        clear()

        def path():
            if os.name == "nt":
                os.chdir("Tools\Persegi")
                os.system("python persegi.py") # For Windows
            else:
                os.chdir("Tools\Persegi")
                os.system("python3 persegi.py")    # For Linux/ OS X
        path()

    elif pilih == 3:
        clear()

        def path():
            if os.name == "nt":
                os.chdir("Tools\Lingkaran")
                os.system("python lingkaran.py") # For Windows
            else:
                os.chdir("Tools\Lingkaran")
                os.system("python3 lingkaran.py")    # For Linux/ OS X
        path()

    elif pilih == 4:
        clear()   

        def path():
            if os.name == "nt":
                os.chdir("Tools\Segitiga")
                os.system("python segitiga.py")  # For Windows
            else:
                os.chdir("Tools\Segitiga")
                os.system("python3 segitiga.py")    # For Linux/ OS X
        path() 

    elif pilih == 5:
        clear()   

        def path():
            if os.name == "nt":
                os.chdir("Tools\jajar-Genjang")
                os.system("python jajar-genjang.py")  # For Windows
            else:
                os.chdir("Tools\Segitiga")
                os.system("python3 segitiga.py")    # For Linux/ OS X
        path()   

    elif pilih == 6:
        clear()   

        def path():
            if os.name == "nt":
                os.chdir("Tools\Belah-ketupat")
                os.system("python ketupat.py")  # For Windows
            else:
                os.chdir("Tools\Belah-ketupat")
                os.system("python3 ketupat.py")    # For Linux/ OS X
        path()  

    elif pilih == 7:
        clear()   

        def path():
            if os.name == "nt":
                os.chdir("Tools\Layang-layang")
                os.system("python layang.py")  # For Windows
            else:
                os.chdir("Tools\Layang-layang")
                os.system("python3 layang.py")    # For Linux/ OS X
        path()

    elif pilih == 8:
        clear()   

        def path():
            if os.name == "nt":
                os.chdir("Tools\Trapesium")
                os.system("python trapesium.py")  # For Windows
            else:
                os.chdir("Tools\Trapesium")
                os.system("python3 trapesium.py")    # For Linux/ OS X
        path()      

    elif pilih == 0:
            text = "bye "

            for i in range(10):
                print(text ,  end=" ")
                for a in range(i + 1):
                    print(". " ,  end=" ")
                    sleep(0.3)
                    clear()
                print()
                
    else:
        print("error")
        sc.sleep(2)
        bangun_datar()    

bangun_datar()        




