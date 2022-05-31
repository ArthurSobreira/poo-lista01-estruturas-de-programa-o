from classVector import Vector


class VectorManage(Vector):
    def insert(self, element):
        self.initial_vector.append(element)

    def get_element(self, index):
        try:
            return self.initial_vector[index]
        except IndexError:
            return False

    def vector_size(self):
        return len(self.initial_vector)
