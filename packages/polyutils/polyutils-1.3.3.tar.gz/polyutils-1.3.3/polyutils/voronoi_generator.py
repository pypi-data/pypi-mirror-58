from polyutils import Polygon
import pyvoro


def get_vertices(vertex_dict):
    v = []
    for i in vertex_dict['vertices']:
        v.append(tuple(i))

    return [*zip(*v)]


def get_faces(face):
    f = []
    for i in face:
        f.append(i['vertices'])
    return f


class PolyGenerator:

    def __init__(self, seeds, container, scale=1):
        self.__seeds = seeds
        self.__container = container
        self.__scale = scale
        self.__polygon_array = None

    def get_polygons(self) -> list:
        polygons_array = []

        cells = self.get_cells()

        for key, cell in enumerate(cells):
            ve = get_vertices(cell)
            fa = get_faces(cell['faces'])
            seed = cell['original']
            volume = cell['volume']

            polygon = Polygon(vertices=ve,
                              faces=fa,
                              color=seed / self.__scale,
                              volume=volume,
                              id_pol=key,
                              )

            polygons_array.append(polygon)

        self.__polygon_array = polygons_array
        return self.__polygon_array

    def get_cells(self) -> dict:
        cells = pyvoro.compute_voronoi(
            points=self.__seeds,
            limits=self.__container,
            dispersion=3,
            # radii=[],
            # periodic=[False, False, False],
        )

        return cells


def generate(num_seeds):
    import numpy as np
    scale = 10
    container_generate = [[0, scale]] * 3

    seeds = np.random.rand(num_seeds, 3) * scale

    polygons = PolyGenerator(seeds=seeds,
                             container=container_generate,
                             scale=scale
                             )

    ret = polygons.get_polygons()

    for r in ret:
        r.triangularize_faces()

    return ret


def main():
    from polyutils.overlapping import is_convex

    # To load from file
    import pickle
    filename = 'voronoi.data'
    file_read_list = open(filename, 'rb')
    ret = pickle.load(file_read_list)

    container = [20, 20]

    # SOME BULLSHIT I''L NEED LATER
    # ret = bottom_front_left_2(ret, container, rotation=True)

    # for new_id_pol in ret:
    #     if not is_convex(new_id_pol):
    #         print(new_id_pol.id_pol)

    # a, b = overlap_list(ret)
    # print(a)
    # for new_id_pol in b:
    #     print(new_id_pol.id_pol)

    # # To save in file
    # import pickle
    # filename = 'voronoi.data'
    # file_write_list = open(filename, 'wb')
    # pickle.dump(ret, file_write_list)
    #
    # test = Rectangle(size=(2, 3, 4), triangular=True)

    # filename = 'bunny.obj'
    # bunny = Rectangle.load_from_obj(filename)
    # bunny.color = (.9, .2, .7)
    # bunny.resize(scale=50)
    # bunny.move_to_origin()
    #
    # from time import time
    # now = time()
    # print(overlap(bunny,test))
    # print('tempo: ', str(time() - now))
    #
    # ret = [bunny, test]

    # for new_id_pol in ret:
    #     new_id_pol.dilate(1.5)

    ret = generate(50)
    # print('generated!')

    num = 0
    for i in ret:
        i.triangularize_faces()
        # i.round_vertices(decimals=6)
        x = is_convex(i)
        if not x:
            num += 1
            # print(i.id_pol)

    print(num)

    from polyutils import PolyViewer3D
    from polyutils import get_max_z, Rectangle

    ret.sort(key=lambda p: get_max_z(p))
    PolyViewer3D.easy_plot(ret, animate=True)

    #
    # container.append(get_obj_z(ret))
    # v = PolyViewer3D(lim=container, edges=False, alpha=1)
    # v.polygons = ret
    #
    # v.container = container
    # v.plot_container_auto(container_opacity=.1)
    #
    # v.add_axes(label='complex_mode')
    # v.plot_objects(animate=True, delay=5000)
    # v.show()


if __name__ == '__main__':
    main()
