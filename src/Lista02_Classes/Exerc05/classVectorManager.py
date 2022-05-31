from classVector import Vector


class VectorManage(Vector):
    def insert(self, element):
        self.initial_vector.append(element)

    def get_element(self, index):
        if index not in range(self.list_size()):
            return False
        return self.initial_vector[index]

    def list_size(self):
        return len(self.initial_vector)
