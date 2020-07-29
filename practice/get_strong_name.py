import get_ascii_number as gs


def main(name1, name2):
    num1 = gs.main(name1)
    num2 = gs.main(name2)

    if num1 > num2:
        return name1
    return name2

print(main('john', 'tom'))