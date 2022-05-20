# Дан массив целых чисел nums. Напишите программу, выводящую минимальное количество ходов,
# требуемых для приведения всех элементов к одному числу.
# За один ход можно уменьшить или увеличить число массива на 1 Пример: nums = [1, 2, 3]
# Решение: [1, 2, 3] => [2, 2, 3] => [2, 2, 2] Минимальное количество ходов: 2
# Элементы массива читаются из файла, переданного в качестве аргумента командной строки.
# Пример: На вход подаётся файл с содержимым: 1 10 2 9 Вывод в консоль: 16

import argparse

def cli_parser():
    parser = argparse.ArgumentParser(description='Task4')
    parser.add_argument('path_to_file', help='path_to_file')
    return parser.parse_args()

def parse_txt(file):
    numbers = []
    with open(file, 'r') as f2:
        while True:
            line = f2.readline().strip()
            if line:
                numbers.append(int(line.split('\n')[0]))
            if not line:
                break
    return numbers

def task4_run(nums):
    nums.sort()
    mid = len(nums) // 2
    res = 0
    for n in nums:
        res += abs(n - nums[mid])
    return res

def main():
    namespace = cli_parser()
    massiv = parse_txt(namespace.path_to_file)
    result = task4_run(massiv)
    print(result)

if __name__ == '__main__':
    main()