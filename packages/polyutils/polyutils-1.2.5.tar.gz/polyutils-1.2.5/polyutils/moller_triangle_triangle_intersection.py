def matmul(v1, v2):
    m = [v1[1] * v2[2] - v1[2] * v2[1],
         v1[2] * v2[0] - v1[0] * v2[2],
         v1[0] * v2[1] - v1[1] * v2[0]]

    return m


def plane_equation(t):
    v0 = t[0]
    v1 = t[1]
    v2 = t[2]

    v1_v0 = [v1[0] - v0[0], v1[1] - v0[1], v1[2] - v0[2]]
    v2_v0 = [v2[0] - v0[0], v2[1] - v0[1], v2[2] - v0[2]]

    n = matmul(v1_v0, v2_v0)

    d = -(n[0] * v0[0] + n[1] * v0[1] + n[2] * v0[2])

    n.append(d)

    return n


def get_n(t):
    m = plane_equation(t)
    n = m[:3]
    return n


def signed_distance(t, p):
    print(t)
    print(p)

    d = []
    for v in t:
        k = v[0] * p[0] + v[1] * p[1] + v[2] * p[2] + p[3]
        d.append(k)

    return d


def plot(t1, t2):
    triangles = [(0, 1, 2)]
    color = (.9, .1, .4)
    color2 = (.1, .4, .9)

    from mayavi import mlab
    f = mlab.figure(size=[900, 600], bgcolor=(.1, .1, .1))

    mlab.points3d(t1[0], t1[1], t1[2], scale_factor=10, figure=f)
    mlab.points3d(t2[0], t2[1], t2[2], scale_factor=10, figure=f)

    mlab.triangular_mesh(
        t1[0], t1[1], t1[2], triangles, figure=f, color=color
    )

    mlab.triangular_mesh(
        t2[0], t2[1], t2[2], triangles, figure=f, color=color2
    )
    mlab.orientation_axes(figure=f)

    mlab.show()


def intersection_line(t1, t2):
    n1 = get_n(t1)
    n2 = get_n(t2)

    d = matmul(n1, n2)

    # temporariamente
    return d


def print_line(a=(0, 0, 0), b=(1, 1, 1)):
    import mayavi.mlab as mlab

    black = (0, 0, 0)
    white = (1, 1, 1)

    mlab.figure(bgcolor=white)

    factor = 17487446

    mlab.points3d(a[0], a[1], a[2], scale_factor=factor, )
    mlab.points3d(b[0], b[1], b[2], scale_factor=factor, )
    mlab.plot3d(
        [a[0], b[1]], [a[1], b[1]], [a[2], b[2]],
        color=black, tube_radius=factor
    )

    mlab.show()


T1 = [(-21, -72, 63), (-78, 99, 40), (-19, -78, -83)]
T2 = [(96, 77, -51), (-95, -1, -16), (9, 5, -21)]

# plot(t1, t2)

# p1 = plane_equation(t1)
# p2 = plane_equation(t2)
# distances = signed_distance(t2, p1)
# print(distances)
#
# print(get_N(t1))

print(intersection_line(T1, T2))
