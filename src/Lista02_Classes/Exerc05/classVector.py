class Vector:
    def __init__(self, initial_vector):
        self.__initial_vector = initial_vector

    def __str__(self):
        return str(self.initial_vector)

    def __len__(self):
        return len(self.initial_vector)

    def __getitem__(self, index):
        try:
            return self.initial_vector[index]
        except IndexError:
            return False

    def insert(self, value):
        self.initial_vector.append(value)

    # Getter and Setter __initial_vector
    @property
    def initial_vector(self):
        return self.__initial_vector

    @initial_vector.setter
    def initial_vector(self, new_vector):
        self.__initial_vector = new_vector
