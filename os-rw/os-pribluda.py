import os, random

root_dir = './os-rw/root_dir'
files = os.path.join(root_dir, "log")
archive = os.path.join(root_dir, "arhive")

def init_enviroment(root_dir):
    if not os.path.isdir(root_dir):
        os.mkdir(root_dir)
        os.mkdir(archive)

def gen_log():
    error_or_not = ("Error", "Succes")
    for i in range(1, 5 + 1):
        s = files + '_' + str(i) + ".txt"
        with open(s, 'w', encoding='utf-8') as file:
            file.write(random.choice(error_or_not))

def read_log():
    s = os.listdir(root_dir)
    for i in s:
        t = os.path.join(root_dir, i)
        if os.path.isdir(t) == False:
            with open(t, 'r', encoding='utf-8') as file:
                read_file = file.read()
                if read_file == "Succes":
                    os.remove(t)
                else:
                    u = os.path.join(archive, i)
                    with open(u, 'w', encoding='utf-8') as file2:
                        file2.write(read_file)

def cleaning():

    for i in os.listdir(archive):
        y = os.path.join(archive, i)
        os.remove(y)

b = init_enviroment(root_dir), gen_log(), read_log(), cleaning()