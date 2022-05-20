# Напишите программу, которая рассчитывает положение точки относительно окружности.
# Координаты центра окружности и его радиус считываются из файла1.
# Пример: 1 1 5 Координаты точек считываются из файла2.  Пример: 0 0 1 6 6 6
# Файлы передаются программе в качестве аргументов. Файл с координатами и радиусом окружности - 1 аргумент,
# файл с координатами точек - 2 аргумент. Координаты в диапазоне float.
# Количество точек от 1 до 100 Вывод каждого положения точки заканчивается символом новой строки.
# Соответствия ответов: 0 - точка лежит на окружности 1 - точка внутри 2 - точка снаружи


import argparse

def cli_parser():
    parser = argparse.ArgumentParser(description='Task2')
    parser.add_argument('centr_radius', help='path to file1.txt centr_radius')
    parser.add_argument('points', help='path to file2.txt points')
    return parser.parse_args()

def parse_txt(file1, file2):
    points = []
    with open(file1, 'r') as f1:
        radius_centr = f1.read().split('\n')
    with open(file2, 'r') as f2:
        while True:
            line = f2.readline().strip()
            if line:
                points.append(line.split('\n'))
            if not line:
                break
    points = [[float(k) for k in y[0].split(' ')] for y in points]
    radius_centr = [[float(q) for q in x.split(' ')] for x in radius_centr]
    radius = radius_centr[1][0]
    centr_x = radius_centr[0][0]
    centr_y = radius_centr[0][1]
    result = {
        'radius': radius,
        'centr_x': centr_x,
        'centr_y': centr_y,
        'points': points
    }
    return result

def task2(data):
    xc = data['centr_x']
    yc = data['centr_y']
    r = data['radius']
    data['result'] = []
    for point in data['points']:
        x = point[0]
        y = point[1]
        result = ((x - xc) ** 2 + (y - yc) ** 2) ** 0.5
        if result < r:
            data['result'].append(f'point {x} - {y} : inside')
            print(1)  # точка внутри
        elif result == r:
            data['result'].append(f'point {x} - {y} : on border')
            print(0)  # точка лежит на окружности
        else:
            data['result'].append(f'point {x} - {y} : outside')
            print(2)  # точка снаружи
    return data

def main():
    namespace = cli_parser()
    data = parse_txt(namespace.centr_radius, namespace.points)
    print(task2(data))
