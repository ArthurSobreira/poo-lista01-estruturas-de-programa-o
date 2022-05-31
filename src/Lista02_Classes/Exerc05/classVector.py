class Vector:
    def __init__(self, initial_list):
        self.__initial_list = initial_list

    # Getter and Setter __initial_list
    @property
    def initial_list(self):
        return self.__initial_list

    @initial_list.setter
    def initial_list(self, new_list):
        self.__initial_list = new_list
