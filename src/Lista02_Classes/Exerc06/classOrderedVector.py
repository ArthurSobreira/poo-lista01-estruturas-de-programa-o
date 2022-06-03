from src.Lista02_Classes.Exerc05.classVector import Vector


class OrderedVector(Vector):
    def insert_string(self, string):
        self.initial_vector.append(string)
        self.initial_vector = sorted(self.initial_vector)

