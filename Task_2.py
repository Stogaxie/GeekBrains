lst = []
n = (int(input("Введите размер списка: ")))
print(f"Размер списка: {n} ")

for i in range(0, n):
    print("Введите элемент списка:")
    item = (input())
    lst.append(item)
print(f"Введенный список: {lst} ")

uplst = lst
x = 0
for i in range(int(len(uplst) / 2)):
    uplst[x], uplst[x + 1] = uplst[x + 1], uplst[x]
    x += 2
print(f"Список с заменами: {uplst}")
