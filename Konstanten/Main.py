from aufgaben import Aufgaben

def mache_aufgaben(aufgaben_nr):
    if aufgaben_nr == Aufgaben.PUTZEN:
        print("Hol den Besen")
    elif aufgaben_nr == Aufgaben.KOCHEN:
        print("Geh in die Küche")
    elif aufgaben_nr == Aufgaben.SPIELEN:
        print("Let's go and play")

mache_aufgaben(Aufgaben.PUTZEN)