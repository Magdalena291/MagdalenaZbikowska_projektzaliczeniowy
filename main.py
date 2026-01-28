from dataset_manager import DatasetManager

dm = DatasetManager()

while True:
    print("\n=== MENU ===")
    print("1. Wczytaj dane CSV")
    print("2. Pokaż pierwsze 5 wierszy")
    print("3. Policz klasy decyzyjne")
    print("4. Podziel dane (train/test/val)")
    print("5. Zapisz podzielone dane")
    print("0. Wyjście")

    choice = input("Wybierz opcję: ")

    if choice == "1":
        dm.load_csv("data/iris.csv", has_header=False)
        print("Dane wczytane.")

    elif choice == "2":
        if not dm.data:
            print("Najpierw wczytaj dane!")
        else:
            dm.print_data(0, 5)

    elif choice == "3":
        if not dm.data:
            print("Najpierw wczytaj dane!")
        else:
            counts = dm.count_classes(4)
            for cls, count in counts.items():
                print(cls, count)

    elif choice == "4":
        if not dm.data:
            print("Najpierw wczytaj dane!")
        else:
            train, test, val = dm.split_data(0.7, 0.15, 0.15)
            print("Train:", len(train))
            print("Test:", len(test))
            print("Validation:", len(val))

    elif choice == "5":
        if not dm.data:
            print("Najpierw wczytaj dane!")
        else:
            train, test, val = dm.split_data(0.7, 0.15, 0.15)
            dm.save_csv(train, "data/train.csv")
            dm.save_csv(test, "data/test.csv")
            dm.save_csv(val, "data/val.csv")
            print("Pliki zapisane.")

    elif choice == "0":
        print("Koniec programu.")
        break

    else:
        print("Niepoprawna opcja.")



