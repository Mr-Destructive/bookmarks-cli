import os

def delete_id():

    id_file = '.dailydevid.txt'
    os.remove(id_file)
    print("daily.dev id successfully deleted")
