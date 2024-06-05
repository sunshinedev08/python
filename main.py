from pycollections import MyPyCollections
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--list", help="Get the data stored in a list", type=bool, required=False)
    parser.add_argument("--set", help="Get the data stored in a set", type=bool, required=False)
    args = parser.parse_args()
    if args.list:
        pycl = MyPyCollections().MyList()
        pycl.printData()
    elif args.set:
        pycs = MyPyCollections.MySet()
        pycs.printData()
