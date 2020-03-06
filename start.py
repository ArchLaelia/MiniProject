import maintxt
import sys


def GUI():
    print("something")
    # här ska den anropa GUI programmet


def TXT():
    maintxt.main()
    # här ska den arnopa TXT programmet


def start():
    if __name__ == "__main__":
        try:
            sys.argv[1]
        except IndexError:
            print("Specify txt or gui after filename")
            sys.exit()
        if str(sys.argv[1]) == "txt":
            TXT()
        elif str(sys.argv[1]) == "gui":
            GUI()


start()
