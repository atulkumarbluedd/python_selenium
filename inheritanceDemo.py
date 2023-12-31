from OOPsdemo import calculator


class childimpl(calculator):
    num2=200

    def __init__(self):
        calculator.__init__(self, 3, 4)
    def getcompleteData(self):
        self.getData(self.num2, self.num2)
        print(self.num2)

obj=childimpl()
obj.getcompleteData()