# Rubrica Telefonica base senza funzioni

# 1️⃣ Creiamo la rubrica come dizionario vuoto
rubrica = {}

# 2️⃣ Ciclo principale
while True:
    print("\nMenu:")
    print("1. Aggiungi contatto")
    print("2. Cerca contatto per nome")
    print("3. Aggiungi numero a un contatto")
    print("4. Rimuovi numero da un contatto")
    print("5. Modifica nome di un contatto")
    print("6. Cerca a chi appartiene un numero")
    print("7. Esci")
    
    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        # Aggiungi contatto
        nome = input("Inserisci il nome del contatto: ")
        numero = input("Inserisci il numero di telefono: ")
        rubrica[nome] = [numero]
        print("Contatto aggiunto!")

    elif scelta == "2":
        # Cerca contatto
        nome = input("Inserisci il nome da cercare: ")
        if nome in rubrica:
            print("Numeri di", nome, ":", rubrica[nome])
        else:
            print("Contatto non trovato.")

    elif scelta == "3":
        # Aggiungi numero
        nome = input("Nome del contatto: ")
        if nome in rubrica:
            numero = input("Numero da aggiungere: ")
            rubrica[nome].append(numero)
            print("Numero aggiunto!")
        else:
            print("Contatto non trovato.")

    elif scelta == "4":
        # Rimuovi numero
        nome = input("Nome del contatto: ")
        if nome in rubrica:
            numero = input("Numero da rimuovere: ")
            if numero in rubrica[nome]:
                rubrica[nome].remove(numero)
                print("Numero rimosso!")
            else:
                print("Numero non trovato.")
        else:
            print("Contatto non trovato.")

    elif scelta == "5":
        # Modifica nome
        vecchio_nome = input("Nome attuale: ")
        if vecchio_nome in rubrica:
            nuovo_nome = input("Nuovo nome: ")
            rubrica[nuovo_nome] = rubrica.pop(vecchio_nome)
            print("Nome modificato!")
        else:
            print("Contatto non trovato.")

    elif scelta == "6":
        # Cerca numero
        numero = input("Numero da cercare: ")
        trovato = False
        for nome, numeri in rubrica.items():
            if numero in numeri:
                print("Il numero appartiene a", nome)
                trovato = True
                break
        if not trovato:
            print("Numero non trovato nella rubrica.")
