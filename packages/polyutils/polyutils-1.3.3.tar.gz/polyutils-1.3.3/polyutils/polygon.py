import numpy as np

DECIMALS = 6


def triangularize_list(array):
    """Create triples (triangularize) from given array."""
    new = []

    if len(array) is 3:
        return [array]

    for i in range(1, len(array) - 1):
        new.append([array[0], array[i], array[i + 1]])

    return new


def change_vertex(coordinates, value):
    """Sum the value to the coordinates."""
    coordinate_list = []
    for i in range(len(coordinates)):
        coordinate_list.append(coordinates[i] + value)
    return tuple(coordinate_list)


class Polygon:
    """
    This class represents the most primitive Polygon ever, with some
    attributes useful (or not) for this package.
    """

    def __init__(
            self, vertices, faces, color=tuple(np.random.rand(3)),
            volume=0, id_pol=0, triangular=False):

        """
        Create a Polygon object.

        :param vertices: 3 triples of vertices, each representing the x, y and z values
        :param faces: list of lists of integers that forms a face
        :param color: a triple containing values between 0 and 1
        :param volume: a float that represents the volume
        :param id_pol: some identification
        :param triangular: True for triangularize the FACES.
        """
        self.__vertices = vertices
        self.__volume = volume
        self.__faces = faces
        self.__color = tuple(color)
        self.__id_pol = id_pol

        if triangular:
            self.triangularize_faces()

    def resize(self, scale=1):
        """
        Resize the polygon by given rate.

        :param scale: a scale rate that multiplies all the vertices.
        :return:
        """
        vertex_list = []
        for v in self.__vertices:
            a = [i * scale for i in v]
            vertex_list.append(a)

        # TODO this changes the volume too, fix-it later.

        self.__vertices = vertex_list

    def round_vertices(self, decimals=DECIMALS):
        """Round the vertices to given decimals."""

        vertex_list = []
        for v in self.__vertices:
            a = np.round(v, decimals=decimals)
            vertex_list.append(tuple(a))

        self.__vertices = vertex_list

    def rotate(self, alpha, beta, gamma):
        """
        Rotate the Polygon on space.

        :param alpha: rotation ANGLE on x axis
        :param beta: rotation ANGLE on y axis
        :param gamma: rotation ANGLE on z axis
        :return:
        """
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

        vertex = [*zip(*self.vertices)]

        new_v = []

        for i in vertex:
            v = np.matmul(rotation, i)
            new_v.append(tuple(v))

        new_v = [*zip(*new_v)]

        self.__vertices = new_v

    @staticmethod
    def load_from_obj(file_path):

        """
        Read a Wavefront OBJ File and creates a Polygon fron it.

        :param file_path: path/of/file.obj
        :return: an object of type Polygon
        """
        # TODO: this ony works in simpler OBJ, no texture
        # and material vertices are considered.
        file = open(file_path, 'r')

        lines = file.readlines()
        id_pol = 0
        vertices = []
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
                vertices.append(v)

            elif attribute[0] == 'f':
                f = [int(i) - 1 for i in attribute[1:]]
                faces.append(f)

            elif attribute[0] == 'c':
                color = tuple(
                    [float(attribute[1]),
                     float(attribute[2]),
                     float(attribute[3])]
                )

        vertices = [*zip(*vertices)]

        p = Polygon(
            vertices=vertices,
            faces=faces,
            color=color,
            id_pol=id_pol,
        )
        p.triangularize_faces()

        return p

    def get_obj(self, index=0, total=0):
        """Return the Wavefront OBJ File notation to string format."""

        v = [*zip(*self.vertices)]
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

    def change_position(self, offset):
        """
        Sum the given value to the vertices of a polygon,
        moving it on space.

        :param offset: a triple (x,y,z)
        :return:
        """
        vertex_list = []
        for key, v in enumerate(self.__vertices):
            a = change_vertex(v, offset[key])
            vertex_list.append(a)

        self.__vertices = vertex_list

    def move_to_origin(self):
        """Move the polygon to origin by its minimum vertices."""

        minimum = np.array(
            [
                min(self.vertices[0]),
                min(self.vertices[1]),
                min(self.vertices[2])
            ]
        )

        v = self.vertices

        new_vertices = []
        for i in range(len(v)):
            line = np.array(list(v[i])) - minimum[i]
            new_vertices.append(tuple(line))

        self.__vertices = new_vertices

    def triangularize_faces(self):
        """Triangularize all FACES of the polygon."""

        f = []
        for i in self.__faces:
            f.extend(triangularize_list(i))

        self.faces = f

    @property
    def vertices(self):
        """Return the list of vertices of the polygon."""
        return self.__vertices

    @vertices.setter
    def vertices(self, new_vertices):
        self.__vertices = new_vertices

    @property
    def faces(self):
        """Return the list of FACES of the polygon."""
        return self.__faces

    @faces.setter
    def faces(self, new_faces):
        self.__faces = new_faces

    @property
    def color(self):
        """Return the color of the polygon."""
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @property
    def id_pol(self):
        """Return the id of the polygon."""
        return self.__id_pol

    @id_pol.setter
    def id_pol(self, new_id_pol):
        self.__id_pol = new_id_pol

    @property
    def volume(self):
        """Return the volume of the polygon."""
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        self.__volume = new_volume

    def show_info(self, complex_mode=False):
        """A PrettyPrint of the polygon and its attributes"""

        print('id_pol:\t', self.id_pol)

        if not complex_mode:
            print('vertices:\t', self.vertices)
        else:
            print('vertices:\t')
            for i in self.vertices:
                print('\t\t', i)

        if not complex_mode:
            print('FACES:\t', self.faces)
        else:
            print('FACES:\t')
            for i in self.faces:
                print('\t\t', i)

        print('color:\t', self.color)

    def dilate(self, rate=.1):
        """
        Dilate a polygon, i.e., expands it
        and keeps it on same position.

        """
        old_vertices = self.vertices
        new_vertices = []

        for vertex in old_vertices:

            new_vertex = list(vertex)
            k = []
            for i in new_vertex:
                i *= rate
                k.append(i)
            new_vertices.append(tuple(k))

        self.vertices = new_vertices
        p = (1 - rate) / 2
        self.change_position(offset=(p, p, p))
