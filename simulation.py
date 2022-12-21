import random

def versuch(wechsel):
    # Tür 1 ist das Auto, Türen 2 und 3 sind Ziegen
    gewaehlte_tuer = random.randint(1, 3) # zufällige Tür mit der Nummer 1-3
    if wechsel: # Wenn man wechselt, dann:
        geoeffnete_tuer = 3 if gewaehlte_tuer==2 else 2
        gewaehlte_tuer = 6- (gewaehlte_tuer + geoeffnete_tuer)
    if gewaehlte_tuer == 1:
        return "Auto"
    else:
        return "Ziege"


def main():
    m = [versuch(True) for i in range(100000)]
    o = [versuch(False) for i in range(100000)]
    print(f'Autoquote mit Wechsel:  {m.count("Auto")/1000}% \nAutoquote ohne Wechsel: {o.count("Auto")/1000}%')
    plot_res(m,o)



import matplotlib.pyplot as plt


def plot_res(p1, p2):
    bes = ["Mit Wechsel", "Ohne Wechsel"]
    erg1 = [p1.count("Auto")/1000,p1.count("Ziege")/1000]
    erg2 = [p2.count("Auto")/1000,p2.count("Ziege")/1000]    
    plt.bar(bes,erg1, color='r')
    plt.bar(bes, erg2, bottom=erg1, color='b')
    plt.legend(["Autos", "Ziegen"])
    plt.show()


main()
