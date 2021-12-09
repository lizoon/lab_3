def f(s):
    print('hui')
    if s != '':
        file = open(s, "r")
        file_ = open('2.txt', "w")
        for line in file:
            if line != '\n':
                new_line = ' '.join(line.split())
                file_.write(new_line + '\n')
                print(new_line)
        file.close()
        file_.close()
