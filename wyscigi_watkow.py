# import threading
# import random
# import time
# from tqdm import tqdm

# # Funkcja, którą będą wykonywać wątki
# # def watek(id, postep):
    # # # Losowa liczba iteracji dla wątku
    # # ilosc_iteracji = random.randint(15, 15)
    # # for i in range(ilosc_iteracji):
        # # # Symulacja zadania
        # # time.sleep(random.uniform(0.1, 0.1))
        # # # Aktualizacja postępu wątku
        # # postep[id] = i / ilosc_iteracji
        # # # Wypisanie postępu wątku
        # # print(f"Wątek {id}: {postep[id]*100:.2f}% ukończony")

# def watek(id, postep):
    # # Losowa liczba iteracji dla wątku
    # ilosc_iteracji = random.randint(5, 15)
    # for _ in tqdm(range(ilosc_iteracji), desc=f'Wątek {id}'):
        # # Symulacja zadania
        # time.sleep(random.uniform(0.1, 0.5))


# def main():
    # # Pobranie liczby dostępnych wątków
    # ilosc_watkow = 1 # threading.active_count()
    # print("ilość wątków: ")
    # print(ilosc_watkow)
    # # Inicjalizacja tablicy postępu dla każdego wątku
    # # postep = [0] * ilosc_watkow
    # # Lista przechowująca wątki
    # watki = []

    # # Tworzenie i uruchamianie wątków
    # for i in range(ilosc_watkow):
        # # watek_nowy = threading.Thread(target=watek, args=(i, postep))
        # watek_nowy = threading.Thread(target=watek, args=(i, None))
        # watki.append(watek_nowy)
        # watek_nowy.start()

    # # Oczekiwanie na zakończenie wszystkich wątków
    # for watek_nowy in watki:
        # print("liczba aktywnych wątków: ")
        # print(threading.active_count())
        # watek_nowy.join()

    # print("\n\n\n\n")
    # # print("liczba aktywnych wątków: ")
    # # print(threading.active_count())
    # print("Wszystkie wątki zakończyły pracę.")

# if __name__ == "__main__":
    # main()
    
    
# Program to count active threads
# active_count() method from Threading Module
import threading
import time
# Methods for three threads..
def thread1_Subroutine(i):
    time.sleep(2)
    print("Thread-1: Number of active threads:", threading.active_count())
    print('Thread 1 Value:', i)

def thread2_Subroutine(i):
    print("Thread-2: Number of active threads:", threading.active_count())
    print('Thread 2 Value:', i)
    
def thread3_Subroutine(i):
    time.sleep(5)
    print("Thread-3: Number of active threads:", threading.active_count())
    print("Thread 3 Value:", i)
    
def thread4_Subroutine(i):
    time.sleep(7)
    print("Thread-4: Number of active threads:", threading.active_count())
    print("Thread 4 Value:", i)
    
def thread5_Subroutine(i):
    time.sleep(9)
    print("Thread-5: Number of active threads:", threading.active_count())
    print("Thread 5 Value:", i)
    
# Creating sample threads
thread1 = threading.Thread(target=thread1_Subroutine, args=(100,), name="Thread1")
thread2 = threading.Thread(target=thread2_Subroutine, args=(200,), name="Thread2")
thread3 = threading.Thread(target=thread3_Subroutine, args=(300,), name="Thread3")
thread4 = threading.Thread(target=thread4_Subroutine, args=(400,), name="Thread4")
thread5 = threading.Thread(target=thread5_Subroutine, args=(500,), name="Thread4")
print("START: Current active thread count: ", threading.active_count())
# Calling start() method to initialize execution
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread5.join() # Wait for thread-3 to join.