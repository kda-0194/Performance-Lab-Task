# На вход в качестве аргументов программы поступают два файла:
# tests.json и values.json (в приложении к заданию находятся примеры этих файлов)
# values.json содержит результаты прохождения тестов с уникальными id
# tests.json содержит структуру для построения отчёта на основе прошедших тестов
# (вложенность может быть большей, чем в примере)
# Напишите программу, которая формирует файл report.json с заполненными полями value для структуры tests.json
# на основании values.json.
# Пример: Часть структуры tests.json: {"id": 122, "title": "Security test", "value": "", "values":
# [{"id": 5321, "title": "Confidentiality", "value": ""}, {"id": 5322, "title": "Integrity", "value": ""}]}
# После заполнения в соответствии с values.json: {"values": [{"id": 122, "value": "failed"},
# {"id": 5321,"value": "passed"}, {"id": 5322,"value": "failed"}]}
# Будет иметь следующий вид в файле report.json: \
# {"id": 122, "title": "Security test", "value": "failed", "values":
# [{"id": 5321, "title": "Confidentiality", "value": "passed"},
#  {"id": 5322, "title": "Integrity", "value": "failed"}]}

import json
import argparse
import os

class Parse():
    response = {}

    def __init__(self, file1, file2) -> None:
        self.file1 = file1
        self.file2 = file2

    def open_json(self, path):
        with open(path, 'rb') as file:
            print(file)
            result = json.load(file)
        return result

    def run_sript(self):
        value = self.open_json(self.file1)
        test = self.open_json(self.file2)
        self.parse_json(value, False)
        self.parse_json(test, True)
        report_json = json.dumps(test, indent=4)
        return report_json

    def parse_json(self, test, write=False):
        if isinstance(test, dict):
            for item in test:
                if isinstance(test.get(item), list):
                    for x in test.get(item):
                        if not write:
                            self.change_value(x)
                            if x.get('values'):
                                self.parse_json(x['values'], write)
                        elif write:
                            self.write_json(x)
                            if x.get('values'):
                                self.parse_json(x['values'], write)
        elif isinstance(test, list):
            for i in test:
                if not write:
                    self.change_value(i)
                elif write:
                    self.write_json(i)
                self.parse_json(i, write)

    def change_value(self, dct):
        id = dct.get('id')
        value = dct.get('value')
        self.response[id] = value

    def write_json(self, dct):
        dct['value'] = self.response.get(dct['id'])

def task3(file1, file2):
    task = Parse(file1, file2)
    return task.run_sript()

def save_report(report):

    with open(f'{os.getcwd()}/report.json', 'w') as f:
        f.write(report)

def cli_parser():
    parser = argparse.ArgumentParser(description='Task3')
    parser.add_argument('file1', help='path to file1.json values')
    parser.add_argument('file2', help='path to file2.json tests')
    return parser.parse_args()

def main():
    namespace = cli_parser()
    report = task3(namespace.file1, namespace.file2)
    save_report(report)

if __name__ == '__main__':
    main()