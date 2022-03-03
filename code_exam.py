import pdb



class Tensor():
  
    def __init__(self, data, shape):
        self.data = data
        self.shape = shape

    def multiplyList(self) :
     
        # Multiply elements one by one
        result = 1
        for x in self.shape:
            result = result * x
        return result


    def reshape(self):  ## 'reshape' is an example. feel free to name it whatever you want  
        num_ele = self.multiplyList()

        # If less padding zeros else removing them
        if num_ele > len(self.data):
            il = self.data + [0]*(num_ele - len(self.data))
        elif num_ele < len(self.data):
            il = self.data[0:num_ele]
        else:
            il = self.data

        if len(self.data) != 0:
            # Grouping each dimenstion until the last
            ol = il
            rev_dims = self.shape[::-1]
            for cur_dim in rev_dims[:-1]:

                num_groups = int(len(ol)/cur_dim)
                nl = []
                for i in range(0, num_groups):
                    nl += [ol[i*cur_dim:i*cur_dim + cur_dim]]
                ol = nl
        else:
            il = []
            ol = []

        print(il)
        print(ol)



data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
shape1 = [2,3,2]
tensor1 = Tensor(data1, shape1)
tensor1.reshape()

data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
shape1 = [5, 2]
tensor1 = Tensor(data1, shape1)
tensor1.reshape()
