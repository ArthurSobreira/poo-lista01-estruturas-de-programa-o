from src.Lista02_Classes.Exerc05.classVector import Vector


class OrderedVector(Vector):
    def order(self):
        return sorted(self.initial_vector)

    def insert_string(self, string):
        self.initial_vector.append(string)
        self.initial_vector = sorted(self.initial_vector)

    def merge(self, vector_obj):
        par_vector = vector_obj.initial_vector
        main_vector = self.initial_vector
        new_obj = OrderedVector(par_vector + main_vector)
        return new_obj
