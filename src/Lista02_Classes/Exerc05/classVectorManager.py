from classVector import Vector


class VectorManage(Vector):
    def insert(self, element):
        self.initial_list.append(element)

    def get_element(self, index):
        if index not in range(self.list_size()):
            return False
        return self.initial_list[index]

    def list_size(self):
        return len(self.initial_list)
