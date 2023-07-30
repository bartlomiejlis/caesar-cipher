def Cezar (klucz, tekst):
  szyfrogram = ""
  # Długość tekstu jawnego
  dl = len(tekst)

  for i in range(0, dl):
    if tekst[i] == " ":
      kod = ord(" ")
    else:
      kod = ord(tekst[i]) + klucz
      if (kod > ord("Z")):
        kod = kod - 26
    szyfrogram = szyfrogram + chr(kod)

  return szyfrogram

jawny = input("Podaj tekst: ")
# Stała liczba przesunięć kolejnych liter tekstu jawnego
klucz = int(input("Podaj klucz szyfrowania: "))

print("\nSzyfrogram:", Cezar(klucz, jawny))