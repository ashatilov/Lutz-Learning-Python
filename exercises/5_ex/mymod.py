def countLines(name):
    with open(name) as f:
        print(len(f.readlines()))

def countChars(name):
    with open(name) as f:
        print(sum([len(line) for line in f]))

def test(name):
    countLines(name)
    countChars(name)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print('Enter filename to test')
    else:
        test(sys.argv[1])
