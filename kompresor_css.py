import os
import string

def czytaj(nazwa):
    plik = open(nazwa, "r")
    informacje = plik.read()
    plik.close()
    return informacje

def zapisz(nazwa, informacje):
    plik = open(nazwa, "w")
    plik.write(informacje)
    plik.close()

nazwa_pliku = input("Podaj nazwę pliku css: ")

informacje_z_pliku = czytaj(nazwa_pliku)

informacje = informacje_z_pliku.replace(" ", "")
informacje = informacje.replace("\n", "")

nazwa_wynikowa = "kompresja.css"

zapisz(nazwa_wynikowa, informacje)
