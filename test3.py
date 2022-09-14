class addition1:  # class
    def set_value(self,val1,val2):
        self.val1 = val1
        self.val2 = val2

    def display(self):
       print(self.val1+self.val2)


obj = addition1()  # object declare
obj.set_value(101,3.50)
obj.display()