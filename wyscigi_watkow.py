import threading
import random
import time

# Funkcja, którą będą wykonywać wątki
def watek(id, postep):
    # Losowa liczba iteracji dla wątku
    ilosc_iteracji = random.randint(5, 15)
    for i in range(ilosc_iteracji):
        # Symulacja zadania
        time.sleep(random.uniform(0.1, 0.5))
        # Aktualizacja postępu wątku
        postep[id] = i / ilosc_iteracji
        # Wypisanie postępu wątku
        print(f"Wątek {id}: {postep[id]*100:.2f}% ukończony")

def main():
    # Pobranie liczby dostępnych wątków
    ilosc_watkow = 4 # threading.active_count()
    print("ilość wątków: ")
    print(ilosc_watkow)
    # Inicjalizacja tablicy postępu dla każdego wątku
    postep = [0] * ilosc_watkow
    # Lista przechowująca wątki
    watki = []

    # Tworzenie i uruchamianie wątków
    for i in range(ilosc_watkow):
        watek_nowy = threading.Thread(target=watek, args=(i, postep))
        watki.append(watek_nowy)
        watek_nowy.start()

    # Oczekiwanie na zakończenie wszystkich wątków
    for watek_nowy in watki:
        watek_nowy.join()

    print("Wszystkie wątki zakończyły pracę.")

if __name__ == "__main__":
    main()