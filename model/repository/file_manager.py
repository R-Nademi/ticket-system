import os
import pickle

file_name = "ticket.dat"


def check_file():
    return os.path.exists(file_name)


def read_from_file():
    if check_file():
        try:

            if os.path.getsize(file_name) > 0:
                with open(file_name, "rb") as file:
                    return pickle.load(file)
            else:

                return []
        except Exception as e:
            print("Error reading file !!!", e)

            os.remove(file_name)
            open(file_name, "wb").close()
            return []
    else:

        open(file_name, "wb").close()
        return []

def write_to_file(data_list):
    with open(file_name, "wb") as file:
        pickle.dump(data_list, file) # noqa