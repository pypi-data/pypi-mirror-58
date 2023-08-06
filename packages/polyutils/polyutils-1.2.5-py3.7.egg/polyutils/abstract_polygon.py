import numpy as np

DECIMALS = 6


def triangularize_list(elements):
    new = []
    if len(elements) is 3:
        return [elements]
    for i in range(1, len(elements) - 1):
        new.append([elements[0], elements[i], elements[i + 1]])

    return new


class AbstractPolygon:
    def __init__(
            self, vertex, faces, color=tuple(np.random.rand(3)),
            volume=0, id_pol=0, triangular=False):

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
            vertex_list.append(tuple(a))

        self.__vertex = vertex_list

    def rotate(self, alpha, beta, gamma):

        rotation_x = np.array(
            [
                [1, 0, 0],
                [0, np.cos(alpha), -np.sin(alpha)],
                [0, np.sin(alpha), np.cos(alpha)]
            ]
        )

        rotation_y = np.array(
            [
                [np.cos(beta), 0, np.sin(beta)],
                [0, 1, 0],
                [-np.sin(beta), 0, np.cos(beta)]
            ]
        )

        rotation_z = np.array(
            [
                [np.cos(gamma), -np.sin(gamma), 0],
                [np.sin(gamma), np.cos(gamma), 0],
                [0, 0, 1]
            ]
        )

        rotation_xy = np.matmul(rotation_x, rotation_y)
        rotation = np.matmul(rotation_xy, rotation_z)

        vertex = [*zip(*self.vertex)]

        new_v = []

        for i in vertex:
            v = np.matmul(rotation, i)
            new_v.append(tuple(v))

        new_v = [*zip(*new_v)]

        self.__vertex = new_v

    @staticmethod
    def load_from_obj(file_path):

        file = open(file_path, 'r')

        lines = file.readlines()
        id_pol = 0
        vertex = []
        faces = []
        color = (.5, .5, .5)

        for line in lines:

            attribute = line.split()

            if line == '\n':
                continue

            if attribute[0] == 'o':
                id_pol = attribute[1]

            elif attribute[0] == 'v':
                v = [float(i) for i in attribute[1:]]
                vertex.append(v)

            elif attribute[0] == 'f':
                f = [int(i) - 1 for i in attribute[1:]]
                faces.append(f)

            elif attribute[0] == 'c':
                color = tuple(
                    [float(attribute[1]),
                     float(attribute[2]),
                     float(attribute[3])]
                )

        vertex = [*zip(*vertex)]

        from polyutils import Polygon
        p = Polygon(
            vertex=vertex,
            faces=faces,
            color=color,
            id_pol=id_pol
        )
        p.triangularize_faces()

        return p

    def get_obj(self, index=0, total=0):

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
        color += str(self.color[0]) + '\t'
        color += str(self.color[1]) + '\t'
        color += str(self.color[2])

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

        minimo = np.array(
            [
                min(self.vertex[0]),
                min(self.vertex[1]),
                min(self.vertex[2])]
        )

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
    def faces(self, new_faces):
        self.__faces = new_faces

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @property
    def id_pol(self):
        return self.__id_pol

    @id_pol.setter
    def id_pol(self, new_id_pol):
        self.__id_pol = new_id_pol

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        self.__volume = new_volume

    def show_info(self, complex_mode=False):

        print('id_pol:\t', self.id_pol)

        if not complex_mode:
            print('vertex:\t', self.vertex)
        else:
            print('vertex:\t')
            for i in self.vertex:
                print('\t\t', i)

        if not complex_mode:
            print('faces:\t', self.faces)
        else:
            print('faces:\t')
            for i in self.faces:
                print('\t\t', i)

        print('color:\t', self.color)

    def dilate(self, rate=.1):

        old_vertex = self.vertex
        new_vertex = []

        for vertice in old_vertex:
            new_vertice = list(vertice)
            k = []
            for i in new_vertice:
                i *= rate
                k.append(i)
            new_vertex.append(tuple(k))

        self.vertex = new_vertex
        p = (1 - rate) / 2
        self.change_vertex(offset=(p, p, p))
