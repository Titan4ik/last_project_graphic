import os


def createFolders():
    for i in range(1,21):
        os.mkdir(str(i))
        with open(f"./{i}/main.py", 'w', encoding='utf-8') as f:
            pass
        with open(f"./{i}/description_of_work.txt", 'w', encoding='utf-8') as f:
            pass
        with open(f"./{i}/useful_links.txt", 'w', encoding='utf-8') as f:
            pass


createFolders()