import math
import random
a = [] #tworzymy pustą listę i przypisujemy ją do zmiennej a
a.append(random.randint(1, 99)) #dodawanie na koniec listy 'a' losowo utworzonej liczby o wartości 1-99, wykonanej 10 razy
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
for i in range(10): #tworzymy pętle która będzie powtarzana w przedziale od 0 do 9
    g = int(input("Enter an integer from 1 to 99: ")) #pobieramy wpisywaną wartość od użytkownika, rzutujemy wartość na typ integer i przypisujemy zmienną
    while a[i] != g: #rozpoczynamy pętle która trwa dopóki element i z listy a jest różny od wartości pobranej od użytkownika
        if g < a[i]: #jeżeli wartość pobrana od użytkownika jest mniejsza od kolejnego elementu z listy a
            print("guess is low") #wyświetla powiadomienie w konsoli, że zgadywana liczba jest za mała
            g = int(input("Enter an integer from 1 to 99: "))
        elif g > a[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 99: "))
        else:
            break
    print("you guessed it!")

b = []
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
for i in range(10):
    g = int(input("Enter an integer from 1 to 49: "))
    while b[i] != g:
        if g < b[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
        elif g > b[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")