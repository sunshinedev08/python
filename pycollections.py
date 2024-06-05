class MyPyCollections:
    class MyList:
        def __init__(self):
            # List
            self.__fruits = ["Apple", "Banana", "Grapes", "Orange"]

        def printData(self):
            print("Data From A List")
            print("All Fruits:" + str(self.__fruits))
            print("First Fruit:" + str(self.__fruits[0]))
            print("Last Fruit:" + str(self.__fruits[-1]))
            print("Length:" + str(len(self.__fruits)))

    class MySet:
        def __init__(self):
            self.__data = {"Admin", "NonAdmin"}

        def printData(self):
            print("Data From A Set")
            print(self.__data)

    class MyDict:
        def __init__(self):
            self.__user = {
                "Name": "Admin",
                "Surname": "User",
                "Email Address": "admin.user@example.com",
                "username": "admin.user"
            }

        def printData(self):
            print("Data From A Dictionary")
            print(self.__user)
