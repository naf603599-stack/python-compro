<<<<<<< HEAD
def example_a_plus_mode():
    with open('example_a+.txt'+'a+')as file:
        file.seek(0)
        content = file.read()
        print("Current content of the file:")
        print(content)
        file.write("Appending a new line at the ena.\n")
        file.seek(0)
        update_content=file.read()
        print("\n Updated content of the fle:")
        print(update_content)
=======
def example_a_plus_mode():
    with open('example_a+.txt'+'a+')as file:
        file.seek(0)
        content = file.read()
        print("Current content of the file:")
        print(content)
        file.write("Appending a new line at the ena.\n")
        file.seek(0)
        update_content=file.read()
        print("\n Updated content of the fle:")
        print(update_content)
>>>>>>> 0c8a140320000645ebb57b05ba11c74ce7305e4c
example_a_plus_mode