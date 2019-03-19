import os, sys
#запускать из командной строки
def walker(root):
    for (thisdir, subsdir, filenames) in os.walk(root):
        print('['+ thisdir +']')
        for fname in filenames:
            path = os.path.join(thisdir, fname)
            print(path)

if __name__ == "__main__":
    walker(sys.argv[1])