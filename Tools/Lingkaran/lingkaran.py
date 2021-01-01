import os 
from time import sleep

def clear():
    if os.name == "nt":
        os.system('cls')  # For Windows
    else:    
        os.system('clear')  # For Linux/OS X



def lingkaran():
    print("""
+=============================================+
|               *Lingkaran*                   |
+=============================================+
| [1] Menghitung Luas (Dengan Jari-Jari)      |
| [2] Menghitung Luas (Dengan Diameter)       |
| [3] Menghitung Keliling (Dengan Jari-Jari)  |
| [4] Menghitung Keliling (Dengan Diameter)   |
| [0] Exit                                    |
+=============================================+
|            Pilih Salah Satu !               |
+=============================================+
    """)

    code = int(input("Pilih: "))

    if code == 1:
        clear()

        print("""
+==============================================+
| *Menghitung Luas Lingkaran Dengan Jari-Jari* |
+=========================+====================+
| phi = 22/7 atau 3,14 , r = Jari-Jari/Radius, | 
| L = Luas                                     | 
+==============================================+
| Rumus :                                      |  
|    L = phi x r x r                           |  
+==============================================+
        """)

        r = int(input("Masukan Jari-Jari: "))
        if r % 7 == 0:
            
            L = 22*r/7*r
            print()
            print("Luas Lingkaran : " + str(int(L)) + " cm2")
            print("Jadi Luas Lingkaran Adalah, " + str(int(L)) + " cm2")
            print()
        else:
            L = 3.14*r*r         
            print()
            print("Luas Lingkaran : " + str(int(L)) + " cm2")
            print("Jadi Luas Lingkaran Adalah, " + str(int(L)) + " cm2")
            print()

    elif code == 2:
        clear()

        print("""
+=============================================+
| *Menghitung Luas Lingkaran Dengan Diameter* |
+=========================+===================+
| phi = 22/7 atau 3,14 , r = Jari-Jari/Radius,|
| L = Luas                                    |
+=============================================+
| Rumus :                                     |   
|    L = phi x r x r                          |  
+=============================================+
        """)

        d = int(input("Masukan Diameter: "))
        if d % 7 == 0:
            r = d / 2
            d = r
            L = 22*r/7*r
            print()
            print("Luas Lingkaran : " + str(int(L)) + " cm2")
            print("Jadi Luas Lingkaran Adalah, " + str(int(L)) + " cm2")
            print()
        else:
            r = d / 2
            d = r
            L = 3.14*r*r         
            print()
            print("Luas Lingkaran : " + str(int(L)) + " cm2")
            print("Jadi Luas Lingkaran Adalah, " + str(int(L)) + " cm2")
            print()

    elif code == 3:
        clear()

        print("""
+==================================================+
| *Menghitung Keliling Lingkaran Dengan Jari-Jari* |
+=========================+========================+
| phi = 22/7 atau 3,14 , r = Jari-Jari/Radius,     |      
| K = Keliling                                     | 
+==================================================+
| Rumus :                                          |
|    K = 2 x phi x r                               |  
+==================================================+
        """)

        r = int(input("Masukan Jari-Jari: "))
        if r % 7 == 0:
            
            K = 2 * 22*r/7
            print()
            print("Keliling Lingkaran : " + str(int(K)) + " cm")
            print("Jadi Keliling Lingkaran Adalah, " + str(int(K)) + " cm")
            print()
        else:
            
            K = 3.14*2*r      
            print()
            print("Keliling Lingkaran : " + str(int(K)) + " cm")
            print("Jadi Keliling Lingkaran Adalah, " + str(int(K)) + " cm")
            print()

    elif code == 4:
        clear()

        print("""
+=================================================+
| *Menghitung Keliling Lingkaran Dengan Diameter* |
+==========================+======================+
| phi = 22/7 atau 3,14 , d = Diameter,            |  
| K = Keliling                                    |
+=================================================+
| Rumus :                                         |  
|    K = phi x d                                  | 
+=================================================+
        """)

        d = int(input("Masukan Diameter: "))
        if d % 7 == 0:
            
            K = 22*d/7
            print()
            print("Keliling Lingkaran : " + str(int(K)) + " cm")
            print("Jadi Keliling Lingkaran Adalah, " + str(int(K)) + " cm")
            print()
        else:
           
            K = 3.14*d   
            print()
            print("Keliling Lingkaran : " + str(int(K)) + " cm")
            print("Jadi Keliling Lingkaran Adalah, " + str(int(K)) + " cm")
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
        lingkaran() 


lingkaran()