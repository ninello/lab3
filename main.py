def proc1():
    n = int(input("ввод кол слов:"))
    result = " "
    for i in range(n):
        w = input(f"ввод слов {i + 1}:")
        result += w + " "
    print("результат:", result.strip())

def proc2():
    n = int(input("ввод кол слов:"))
    result = []
    for i in range(n):
        result.append(str(input()))

    result = []
    while(new_word := str(input())) != "stop":
        result.append(new_word)
        print(" ".join(result))


def proc3():
    result = []
    str(input())
    if "ф" or  "Ф" in str:
            print("Ого! Это редкое слово!")
    else:
        print("Эх,это не очень редкое слово")

def proc4():
    import random # библиотека math оказалась слишком навароченной для простого калькулятора
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    s = a + b
    print(a1, '+', b1, '=')
    o = int(input())
    if o == s:
        print('Правильно!')
    else:
        print('Ответ неверный')

def proc41():
    import random
    error_count = 0
    count = 0
    while error_count < 3:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        if int(input(f"{a} + {b} = ")) == a + b:
            count += 1
            print('Правильно!')
        else:
            error_count += 1
            print('Неправильно!')
    print(f"Игра окончена. Правильных ответов {count}")