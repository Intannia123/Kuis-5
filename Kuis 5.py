print ("PYTHON EXPRESSION")
result_a = 15 % 5
print("a. 15 mod 5:", result_a)

result_b = 12 + 3 * 5 == 75
print("b. 12 + 3 * 5 == 75:", result_b)

result_c = "PML" + "15523"
print("c. \"PML\" + \"15523\":", result_c)

try:
    result_d = "100" + 234
except TypeError:
    result_d = "Error"
print("d. \"100\" + 234:", result_d)

result_e = ((11 % 3) + 2) != 8 / 2
print("e. ((11 % 3) + 2) != 8 / 2:", result_e)

print("EKSPRESI BOOLEAN")
p = 11
q = 5
r = 4

result_2a = (p - r) == (r + q)
print("a. ((p - r) == (r + q)):", result_2a)

result_2b = ((p % 3) + q) != (r % 2)
print("b. (((p % 3) + q) != (r % 2)):", result_2b)

result_2c = (q - 3) == (p % 2 + q)
print("c. ((q - 3) == (p % 2 + q)):", result_2c)

result_2d = (r + q) != ((p * 2) % 2)
print("d. ((r + q) != ((p * 2) % 2)):", result_2d)

result_2e = ((q % 3) + p) > (r % 2)
print("e. ((((q % 3) + p) > (r % 2)):", result_2e)

result_2f = (r + p) <= (q * 5)
print("f. (((r + p)) <= (q * 5)):", result_2f)

print ("==============")
print ("Isian singkat")
print ("nomor 1")
hasil = "Honey" + "Boo" *3
print (hasil)

print ("nomor 2")
capitals = {}
capitals['Murica'] = 'Warshington'
capitals['Germany'] = 'Bonn'
capitals['France'] = 'Paris'
capitals['England'] = 'London'
capitals['Germany'] = 'Berlin'
print(capitals['Germany'])

print ("nomor 3")
a = "23"
b=9
print (int(a)+ b)

print ("nomor 4")
letters = ["a", "b", "o", "c", "p"]
print (letters[1])
print (letters[len(letters)-2])
print (letters + ["x"])
print (letters)

print ("nomor 5")
result = ' '.join('h a n d s'.split())
print (result)

print ("nomor 6")
import json

json_string = """
[
    {"1": "one", "2": "two", "3": "three"},
    {"1": "un", "2": "deux", "3": "trois"},
    {"1": "eins", "2": "zwei", "3": "drei"}
]
"""

data = json.loads(json_string)
result = data[1]["2"]
print(result)

print ("nomor 7")
def pembagi_indeks1(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return -1


vals = [100, 66, 55, 64, 41, 35, 18, 64]
print(pembagi_indeks1(vals, 5))

print ("nomor 8")
def mystery(n, m):
    p = 0
    e = 0
    table = []

    while n >= m:
        p = n
        e += 1
        table.append((p, e))
        n -= m

    print(f"{'Iterasi':<10}{'p':<10}{'e':<10}")
    print("=" * 30)
    for i, (p, e) in enumerate(table, 1):
        print(f"{i:<10}{p:<10}{e:<10}")

    return p
print(f"Output: {mystery(4, 3)}")
