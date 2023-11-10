def lasit_datni():
    
    datnes_nosaukums=input("Ievadīt datnes nosaukumu:")
    try:
    # Kā ielādēt datnes saturu?
        with open(datnes_nosaukums, 'r') as ff:
           saturs=ff.read()
             # print(saturs)
            # izvadi 
        print(f"simbolu skaits datnē ir {len(saturs)}")

        # izvadi pirmos 10 simbolus
        print(f"Pirmie 10 simboli ir:{saturs[:10]}")
          
        # izvadi pirmo un pedejo simbolu
        print(f"izvadit pirmo un pedejo simbolu: {saturs[0]} un {saturs[-1]}")
    except FileNotFoundError:
       print("Datne nav atrasta!")
    except ValueError:
        print("Datu kļūda!")
    






if __name__=="__main__":
    lasit_datni()