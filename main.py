from pycollections import MyPyCollections
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--list", help="Get the data stored in a list", type=str, required=False)
    parser.add_argument("--set", help="Get the data stored in a set", type=str, required=False)
    args = parser.parse_args()
    if str(args.list).__eq__("yes"):
        pycl = MyPyCollections().MyList()
        pycl.printData()
    elif str(args.set).__eq__("yes"):
        pycs = MyPyCollections.MySet()
        pycs.printData()
    else:
        print(parser.print_usage())
