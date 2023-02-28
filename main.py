def proc1():
    n = int(input('Введите нoiжное количество слов: '))
    result = ''
    for i in range(n):
        x = input(f"ввод слов {i + 1}:")
        result += x + " "
    print("результат:", result.strip())


def proc2():

    result = []

    while (wd := str(input())) != "stop":
          result.append(wd)
    print(" ".join(result))
proc1(), proc2()

