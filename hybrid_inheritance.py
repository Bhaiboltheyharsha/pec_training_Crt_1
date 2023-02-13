class writing:
    def way_of_writing(self):
        print("left_hand")
        print("right_hand")


class pen(writing):
    def properties(self):
        print("colour")
        print("cost")


class pencil(writing):
    def properties(self):
        print("colour")
        print("cost")


class products(pen, pencil):
    pass


obj = products()
obj.properties()
