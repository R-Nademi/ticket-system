from model.file_manager import file_name
from view.info import load_data


def print_hi(name):
    print(f'hi, {name}')

if file_name == '_mine_':
    load_data()
    print_hi('pycharm')