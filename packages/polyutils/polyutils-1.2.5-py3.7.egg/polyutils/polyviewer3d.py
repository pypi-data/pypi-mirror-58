from mayavi import mlab

FG_COLOR = (1, 1, 1)
BG_COLOR = (.1, .1, .1)


class PolyViewer3D:

    def __init__(
            self, lim=(10, 10, 10), alpha=1,
            title='Mayavi Visualizer', edges=False):

        self.__fig = mlab.figure(
            figure=title,
            bgcolor=BG_COLOR,
            fgcolor=FG_COLOR,
            size=(800, 700),
        )

        self.__container = lim

        self.__alpha = alpha
        self.__edges = edges

        self.__best_fit = [0, 0, 0]

        self.__polygons = []
        self.__objects = []

        self.__axes = None
        self.__orientation_axes = None

        self.__delay = 100
        self.anim = (mlab.animate(delay=self.__delay, ui=True, ))(self.anim)

    def plot_container(
            self, container=None, color=(.9, .9, .9),
            container_opacity=.1, dilate=.1):

        if container is None:
            container = self.__container

        from polyutils.rectangle import Rectangle
        c = Rectangle(size=container, triangular=True)

        if dilate is not None:
            c.old_dilate(rate=dilate)

        self.add_cell(
            obj=c,
            color=color,
            opacity=container_opacity
        )
        return c

    def plot_container_auto(
            self, color=(.9, .9, .9),
            container_opacity=.1, dilate=.1):

        self.update_best_fit()

        self.__container = self.__best_fit

        c = self.plot_container(
            container=self.__container, color=color,
            container_opacity=container_opacity,
            dilate=dilate
        )
        return c

    def update_best_fit(self):

        from polyutils.placement_rules import get_obj_x, get_obj_y, get_obj_z

        x = get_obj_x(self.__polygons)
        y = get_obj_y(self.__polygons)
        z = get_obj_z(self.__polygons)

        n_digits = 0
        x = round(x, ndigits=n_digits)
        y = round(y, ndigits=n_digits)
        z = round(z, ndigits=n_digits)

        self.__best_fit = [x, y, z]

    def add_axes(self, label='simple'):

        if label is 'complex_mode':
            x_label = 'x=' + str(self.__container[0])
            y_label = 'y=' + str(self.__container[1])
            z_label = 'z=' + str(self.__container[2])
        else:
            x_label = 'x'
            y_label = 'y'
            z_label = 'z'

        ranges = [
            0, self.__container[0],
            0, self.__container[1],
            0, self.__container[2]
        ]

        self.__axes = mlab.axes(
            xlabel=x_label,
            ylabel=y_label,
            zlabel=z_label,
            ranges=ranges,
            nb_labels=0,
            figure=self.__fig
        )

        self.__orientation_axes = mlab.orientation_axes(figure=self.__fig)

    def add_objects(self, objs):

        for i in objs:
            self.add_cell(i, color=i.color, opacity=self.__alpha)

    def add_cell(self, obj, color=None, opacity=.8):

        x = obj.vertex[0]
        y = obj.vertex[1]
        z = obj.vertex[2]
        faces = obj.faces

        c = color

        if color is None:
            c = obj.color

        representation = 'surface'

        o = mlab.triangular_mesh(
            x, y, z, faces,
            color=c,
            opacity=opacity,
            representation=representation,
            resolution=80000,
            figure=self.__fig,
        )

        self.__objects.append(o)

        if self.__edges is True:
            mlab.outline(figure=self.__fig, )

        # self.__polygons.append(o)

    def anim(self):

        for i in self.__polygons:
            self.add_cell(i, color=i.color, opacity=self.__alpha)
            yield

    def plot_objects(self, animate=False, delay=500):

        self.__delay = delay

        if not animate:
            for i in self.__polygons:
                self.add_cell(obj=i, opacity=self.__alpha)
            return

        self.anim()

        return

    @staticmethod
    def show():
        mlab.show()

    @property
    def polygons(self):
        return self.__polygons

    @polygons.setter
    def polygons(self, new_pols):
        self.__polygons = new_pols

    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, new_container):
        self.__container = new_container

    @property
    def objects(self):
        return self.__objects

    @staticmethod
    def easy_plot(polygons, animate=False, container=None):

        v = PolyViewer3D(lim=container, edges=False, alpha=1)
        v.polygons = polygons

        if container is None:
            v.plot_container_auto(container_opacity=.1)

        else:
            v.container = container
            v.plot_container()

        v.add_axes(label='complex_mode')
        v.plot_objects(animate=animate, delay=5000)
        v.show()


def main():
    from polyutils.rectangle import Rectangle
    from polyutils.placement_rules import bottom_front_left_2, get_obj_z
    import numpy as np

    container_base = [20, 25]

    num_pols = 60
    ret = [Rectangle(size=np.random.randint(1, 10, 3),
                     color=np.random.rand(3),
                     id_pol=i,
                     triangular=True) for i in range(num_pols)
           ]

    ret = bottom_front_left_2(ret, container_base, rotation=True)

    container_base.append(get_obj_z(ret))

    # Create the visualizer
    visualizer = PolyViewer3D(alpha=1, edges=False)

    # Add the polygons list to the visualizer
    visualizer.polygons = ret

    # Set the container
    visualizer.container = container_base

    # Plot the given container
    visualizer.plot_container()

    # If you want the best container,
    # you can use this instead of plot_container()
    # visualizer.plot_container_auto(container_opacity=.1)

    # Optional: show axes
    visualizer.add_axes(label='complex_mode')

    # Add objects to the scene
    visualizer.plot_objects(animate=True, delay=10)

    # Finally show the scene
    visualizer.show()

    # Or more easy:
    # Just pass the polygons and the container (this is optional)
    # PolyViewer3D.easy_plot(ret, animate=True, container=(50, 50, 50))


if __name__ == "__main__":
    main()
