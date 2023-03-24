import random


def heapify(array, n, i):
    max = i
    l = 2 * i + 1
    r = 2 * i + 2

    # agar chap element ildizdan katta bo'lsa
    if l <= n and array[l] > array[max]:
        max = l

    # agar o`ng element ildizdan katta bo'lsa
    if r <= n and array[r] > array[max]:
        max = r

    # agar maksimal i bo'lmasa
    if max != i:
        array[i], array[max] = array[max], array[i]
        heapify(array, n, max)


def heapSort(array):
    n = len(array)
    for i in range(int(n / 2), -1, -1): heapify(array, n - 1, i)
    for i in range(n - 1, 0, -1):

        # massivni oxirgi elementi bilan birinchi elementini almashtirish
        array[i], array[0] = array[0], array[i]

        # massivni oxirgi elementini ro'yxatdan o'chirish va ro'yhatni qayta tiklash
        heapify(array, i - 1, 0)


# Massiv elementlarini kiritish
n = int(input("Massiv uzunligini kiriting>>>"))
a = []
for i in range(n):
    a.append(random.randint(1, 100))


print(a)

# heapSort ya'ni piramida algoritmi bo'yicha saralash funksiyasiga murojaat qilish
heapSort(a)

# Piramida algoritmi bo'yicha saralangan massivni chiqarish
print(a)
