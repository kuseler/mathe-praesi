import random
import matplotlib.pyplot as plt

def versuch(wechsel):
    # Tür 1 ist das Auto, Türen 2 und 3 sind Ziegen
    gewaehlte_tuer = random.randint(1, 3) # zufällige Tür mit der Nummer 1-3
    if wechsel: # Wenn es wechselt, 
        revealed_door = 3 if gewaehlte_tuer==2 else 2
        available_doors = [i for i in range(1,4) if i not in (gewaehlte_tuer, revealed_door)]
        gewaehlte_tuer = random.choice(available_doors)
    if gewaehlte_tuer == 1:
        return "Auto"
    else:
        return "Ziege"


def main():
    m = [run_trial(True) for i in range(100000)]
    o = [run_trial(False) for i in range(100000)]
    print(f'Siegquote mit Wechsel:  {m.count("Auto")/1000}% \nSiegquote ohne Wechsel: {o.count("Auto")/1000}%')
    plot_res(m,o)


def plot_res(p1, p2):
    bes = ["Mit Wechsel", "Ohne Wechsel"]
    erg1 = [p1.count("Auto")/1000,p1.count("Ziege")/1000]
    erg2 = [p2.count("Auto")/1000,p2.count("Ziege")/1000]    
    plt.bar(bes,erg1, color='r')
    plt.bar(bes, erg2, bottom=erg1, color='b')
    plt.legend(["Siege", "Niederlagen"])
    plt.show()


main()
