from linecache import getline 

FILE = "660000_parole_italiane.txt"

def file_length(file_name):
    s = 0
    e = -1
    while s != e:
        getline(file_name, 1). 

def find(file_name, word):
    print(getline(file_name, 1).rstrip())
        

def main():
    c = 0
    with open(FILE, "r") as file:
        for line in file:
            print(line.rstrip())
            c += 1
            if c >= 10:
                break
    find(FILE, word)

if __name__ == "__main__":
    main()
