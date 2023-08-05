from polyutils.abstract_polygon import AbstractPolygon
import numpy as np

# Faces is the same for all rectangles ;)
faces = [[1, 3, 2, 0],
         [1, 5, 7, 3],
         [1, 0, 4, 5],
         [2, 6, 4, 0],
         [2, 3, 7, 6],
         [4, 6, 7, 5]]

# Angle for rotation
angle = np.pi / 2


class Rectangle(AbstractPolygon):

    def __init__(self, size, id_pol=0, color=np.random.rand(3), triangular=False):
        """
        Class constructor
        Create a rectangle with given size
        :param size: triple representing the size (length, width, height)
        :param color: triple that represents a color (RGB), random if not specified
        """

        vertex = [(0.0, size[0], 0.0, size[0], 0.0, size[0], 0.0, size[0]),
                  (0.0, 0.0, size[1], size[1], 0.0, 0.0, size[1], size[1]),
                  (0.0, 0.0, 0.0, 0.0, size[2], size[2], size[2], size[2])]

        volume = size[0] * size[1] * size[2]

        super().__init__(vertex=vertex,
                         faces=faces,
                         volume=volume,
                         id_pol=id_pol,
                         color=color,
                         triangular=triangular,
                         )

    def dilate(self, rate=.1):
        old_vertex = self.vertex
        new_vertex = []
        for vertice in old_vertex:
            new_vertice = list(vertice)
            k = []
            for i in new_vertice:
                if i <= 0.0:
                    i -= rate
                    k.append(i)
                else:
                    i += rate
                    k.append(i)
            new_vertex.append(tuple(k))

        self.vertex = new_vertex

    def rotate_rectangle(self, direction=0):
        """
        Rotate a rectangle orthogonally, i.e., there are 6 possible rotations
        :param direction: the number of the rotation (type=0: no rotation)
        :return: None
        """

        if direction == 1:  # Type 1 - (a,c,b)
            Rectangle.rotate(self, angle, 0, 0)

        elif direction == 2:  # Type 2 - (b,a,c)
            Rectangle.rotate(self, 0, 0, angle)

        elif direction == 3:  # Type 3 - (b,c,a)
            Rectangle.rotate(self, angle, 0, angle)

        elif direction == 4:  # Type 4 - (c,a,b)
            Rectangle.rotate(self, 0, angle, angle)

        elif direction == 5:  # Type 5 - (c,b,a)
            Rectangle.rotate(self, angle, angle, angle)

        # else:  # Type 0 - no rotation (a,b,c)
        #     None
        #     Rectangle.rotate(self, 0, 0, 0)

        Rectangle.move_to_origin(self)


# Example
def main():
    from polyviewer import PolyViewer2 as p
    from polyutils.placement_rules import bottom_front_left, bottom_front_left_2, get_obj_z
    from copy import deepcopy
    from polyutils.overlapping import overlap_list, is_convex

    # Create colorful rectangles
    ret = [Rectangle(size=np.random.randint(1, 14, 3), id_pol=k, color=np.random.rand(3), triangular=True) for k in
           range(50)]

    container = [50, 50, 50]  # Container to put the rectangles

    # Place them in a fool way
    ret = bottom_front_left_2(ret, container, rotation=True)

    for r in ret:
        print(is_convex(r))

    # Check if there are any overlapping between the rectangles
    print(overlap_list(ret))

    v = p(lim=container, edges=False)
    container[2] = get_obj_z(ret)
    v.container = container
    v.objects = ret
    v.plot_container_auto(container_opacity=.1, dilate=.1)

    v.add_axes()
    v.animate(animate=False)
    v.show()


if __name__ == '__main__':
    main()
