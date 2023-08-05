from polyutils.abstract_polygon import AbstractPolygon


class Polygon(AbstractPolygon):
    def __init__(self, vertex, faces, color=None, volume=0, id_pol=0, triangular=False):
        self.__vertex = vertex
        self.__faces = faces
        self.__color = tuple(color)
        self.__volume = volume
        self.__id_pol = id_pol
        super().__init__(vertex=self.__vertex,
                         faces=self.__faces,
                         color=self.__color,
                         volume=self.__volume,
                         id_pol=self.__id_pol,
                         triangular=triangular,
                         )
