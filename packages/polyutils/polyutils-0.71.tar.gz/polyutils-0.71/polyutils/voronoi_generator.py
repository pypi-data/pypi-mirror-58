import pyvoro
from polyutils import Polygon


def get_vertices(vertex_dict):
    v = []
    for i in vertex_dict['vertices']:
        v.append(tuple(i))

    return [*zip(*v)]


def get_faces(l):
    f = []
    for i in l:
        f.append(i['vertices'])
    return f


class PolyGenerator:
    """
        Construtor da classe.
        :param seeds: Porta serial do dispositivo USB GPS
        :param x_lim: limite x máximo do paralelepipedo a ser gerado
        :param y_lim: limite y máximo do paralelepipedo a ser gerado
        :param z_lim: limite x máximo do paralelepipedo a ser gerado
        :param scale: escada do paralelepipedo (default=1)
    """

    def __init__(self, seeds, container, scale=1):
        self.__seeds = seeds
        self.__container = container
        self.__scale = scale
        self.__polygon_array = None

    def get_polygons(self) -> list:
        """"
            Método para extrair os polígonos das células geradas pelo método get_cells
            :return: list do tipo Polygons
        """
        polygons_array = []

        cells = self.get_cells()

        for key, cell in enumerate(cells):
            ve = get_vertices(cell)
            fa = get_faces(cell['faces'])
            seed = cell['original']
            volume = cell['volume']

            polygon = Polygon(vertex=ve,
                              faces=fa,
                              color=seed / self.__scale,
                              volume=volume,
                              id_pol=key,
                              )

            polygons_array.append(polygon)

        self.__polygon_array = polygons_array
        return self.__polygon_array

    def get_cells(self) -> dict:
        """
            Retorna um dicionário de células geradas pelo PyVoro .
            :return: dicionário contendo as células geradas pelo PyVoro
        """
        cells = pyvoro.compute_voronoi(
            points=self.__seeds,
            limits=self.__container,
            dispersion=3,
            # radii=[],
            # periodic=[False, False, False],
        )

        return cells


def main():
    import numpy as np
    from polyviewer import PolyViewer2 as p
    from polyutils import overlap_list, overlap, get_obj_z, is_convex, get_max_z
    from polyutils.placement_rules import bottom_front_left_2
    scale = 10

    container_generate = [[0, scale]] * 3

    num_seeds = 70
    # seeds = np.random.rand(num_seeds, 3) * scale
    #
    # polygons = PolyGenerator(seeds=seeds,
    #                          container=container_generate,
    #                          scale=scale
    #                          )
    #
    # ret = polygons.get_polygons()
    #
    # for r in ret:
    #     r.triangularize_faces()

    # To load from file
    import pickle
    filename = 'voronoi.data'
    file_read_list = open(filename, 'rb')
    ret = pickle.load(file_read_list)

    ret.sort(key=get_max_z)

    container = [20, 20]
    # ret = bottom_front_left_2(ret, container, rotation=True)

    # for i in ret:
    #     if not is_convex(i):
    #         print(i.id_pol)

    # a, b = overlap_list(ret)
    # print(a)
    # for i in b:
    #     print(i.id_pol)

    # # To save in file
    # import pickle
    # filename = 'voronoi.data'
    # file_write_list = open(filename, 'wb')
    # pickle.dump(ret, file_write_list)
    #

    container.append(get_obj_z(ret))
    v = p(lim=container, edges=False, alpha=1)
    v.objects = ret

    print(len(v.objects))

    v.container = container
    v.plot_container_auto(container_opacity=.1, dilate=.05)

    v.add_axes(label='complex')
    v.plot_objects(animate=True, delay=10)
    v.show()


if __name__ == '__main__':
    main()
