class List(list):
    def __init__(self):
        super(list, self).__init__()

    def hello(self):
        print("hello")

    List = []
    

a = List()
a.hello()

a.List.hello()