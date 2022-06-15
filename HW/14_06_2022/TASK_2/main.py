


class Main:
    def __init__(self):
        self.global_list = []
        for x in range(1, 1000):
            name = "_" + str(x)
            index = str(x)
            value = "_A" + str(x)
            local_list = [name, index, value]
            self.global_list.append(local_list)
            # name=’_1’, index=1, value=’_A1’

mass = Main()
print(mass.global_list)