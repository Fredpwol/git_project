def dummy(name):
    print(f"Your name is {name}!")
    return name

if __name__ == "__main__":
    name = dummy(input("Enter your name: "))
    with open('man.txt', 'a', encoding='UTF8') as f:
        f.write(name + "\n")