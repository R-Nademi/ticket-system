from model.repository.file_manager import file_name

from view.ticket_view import load_data


def print_hi(name):
    print(f'hi, {name}')

if file_name == '_main_':
    load_data()
    print_hi('pycharm')
