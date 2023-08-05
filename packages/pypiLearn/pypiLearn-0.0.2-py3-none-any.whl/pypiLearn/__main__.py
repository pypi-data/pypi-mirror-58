import sys
import time

from test import Test

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print("Wellcome to use pypiLearn.")
    print("Version:{0}".format(Test.__version__))

    t = Test()
    t.sayhello()

if __name__ == "__main__":
    main()
