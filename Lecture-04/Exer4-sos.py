num_columns=int(input("ENTER THE NUMBER OF COLUMNS : "))
for i in range(1, 101):
    print(f"{i:>3}", end="")
    if i % num_columns == 0 :
        print()