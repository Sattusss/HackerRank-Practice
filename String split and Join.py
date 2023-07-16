def splitandjoin(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = splitandjoin(line)
    print(result)
    