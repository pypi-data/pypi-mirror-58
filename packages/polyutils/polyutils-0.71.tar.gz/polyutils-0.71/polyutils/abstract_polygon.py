from abc import abstractmethod
import numpy as np

DECIMALS = 5


def triangularize_list(elements):
    new = []
    if len(elements) is 3:
        return [elements]
    for i in range(1, len(elements) - 1):
        new.append([elements[0], elements[i], elements[i + 1]])
    return new


class AbstractPolygon:
    def __init__(self, vertex, faces, color=np.random.rand(1, 3), volume=0, id_pol=0, triangular=False):
        self.__vertex = vertex
        self.__volume = volume
        self.__faces = faces
        self.__color = tuple(color)
        self.__id_pol = id_pol

        if triangular:
            self.triangularize_faces()

    def resize(self, scale=1):
        vertex_list = []
        for v in self.__vertex:
            a = [i * scale for i in v]
            vertex_list.append(a)

        self.__vertex = vertex_list

    def round_vertices(self, decimals=DECIMALS):
        vertex_list = []
        for v in self.__vertex:
            a = np.round(v, decimals=decimals)
            vertex_list.append(a)

        self.__vertex = vertex_list

    def rotate(self, alpha, beta, gamma):
        rotation_x = np.array([[1, 0, 0],
                               [0, np.cos(alpha), -np.sin(alpha)],
                               [0, np.sin(alpha), np.cos(alpha)]])

        rotation_y = np.array([[np.cos(beta), 0, np.sin(beta)],
                               [0, 1, 0],
                               [-np.sin(beta), 0, np.cos(beta)]])

        rotation_z = np.array([[np.cos(gamma), -np.sin(gamma), 0],
                               [np.sin(gamma), np.cos(gamma), 0],
                               [0, 0, 1]])

        rotation_xy = np.matmul(rotation_x, rotation_y)
        rotation = np.matmul(rotation_xy, rotation_z)

        vertex = [*zip(*self.vertex)]

        new_v = []
        for i in vertex:
            v = np.matmul(rotation, i)
            new_v.append(tuple(v))

        new_v = [*zip(*new_v)]

        self.__vertex = new_v

    def get_obj(self, index, total):

        v = [*zip(*self.vertex)]
        file = ''

        name = 'o\tpol_{0:03d}-{1:03d}'.format(index, total)

        vertex = ''
        for i in v:
            vertex += 'v\t' + str(i[0]) + '\t' + str(i[1]) + '\t' + str(i[2])
            vertex += '\n'

        faces = ''
        for i in self.faces:
            face = 'f\t'
            for j in i:
                face += str(j + 1) + '\t'
            faces += face + '\n'

        color = 'c\t'
        color += str(self.color[0]) + '\t' + str(self.color[1]) + '\t' + str(self.color[2])

        file += name + '\n'
        file += vertex
        file += faces
        file += color

        return file

    @staticmethod
    def change_position(v_tuple, offset):
        coordinate_list = []
        for i in range(len(v_tuple)):
            coordinate_list.append(v_tuple[i] + offset)
        return tuple(coordinate_list)

    def change_vertex(self, offset):
        vertex_list = []
        for key, v in enumerate(self.__vertex):
            a = self.change_position(v, offset[key])
            vertex_list.append(a)

        self.__vertex = vertex_list

    def move_to_origin(self):
        minimo = np.array([min(self.vertex[0]), min(self.vertex[1]), min(self.vertex[2])])

        v = self.vertex

        c = []
        for i in range(len(v)):
            line = np.array(list(v[i])) - minimo[i]
            c.append(tuple(line))

        self.__vertex = c

    def triangularize_faces(self):
        f = []
        for i in self.__faces:
            f.extend(triangularize_list(i))

        self.faces = f

    @property
    def vertex(self):
        return self.__vertex

    @vertex.setter
    def vertex(self, new_vertex):
        self.__vertex = new_vertex

    @property
    def faces(self):
        return self.__faces

    @faces.setter
    def faces(self, i):
        self.__faces = i

    @property
    def color(self):
        return self.__color

    @property
    def id_pol(self):
        return self.__id_pol

    @id_pol.setter
    def id_pol(self, i):
        self.__id_pol = i

    @property
    def volume(self):
        return self.__volume

    def show(self):
        print('id_pol:\t', self.id_pol)
        print('vertex:\t', self.vertex)
        print('faces:\t', self.faces)
        print('color:\t', self.color)

    @abstractmethod
    def dilate(self):
        return
