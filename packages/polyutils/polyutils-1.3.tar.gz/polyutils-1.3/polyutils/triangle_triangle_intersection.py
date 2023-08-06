# Used
def plot(polygons=(), points=()):
    color = [
        (.1, .4, .9),
        (.1, .9, .4),
        (.4, .1, .9),
        (.4, .9, .1),
        (.9, .1, .4),
        (.9, .4, .1),
    ]
    triangles = [(0, 1, 2)]
    scale = .25
    opacity = 1

    from mayavi import mlab
    f = mlab.figure(size=[1000, 700], bgcolor=(.1, .1, .1))
    f.scene.disable_render = False

    # Plot points and labels
    for p in points:
        if p is not None:
            mlab.points3d(p[0], p[1], p[2], scale_factor=scale, figure=f)
            mlab.text3d(p[0], p[1], p[2], text=str(p), scale=scale * 1.2)

    # Plot triangles
    for k, p in enumerate(polygons):
        if p is not None:
            # Plotters separate the x's, y's and z's in three different arrays
            p = [*zip(*p)]
            mlab.triangular_mesh(
                p[0], p[1], p[2], triangles, figure=f, color=color[k % 6],
                opacity=opacity
            )

    mlab.orientation_axes(figure=f)

    mlab.show()


# Used indirectly
def signed_distance_array(t, p):
    d = []
    for v in t:
        k = v[0] * p[0] + v[1] * p[1] + v[2] * p[2] + p[3]
        d.append(k)

    return d


# Used indirectly
def matmul(v1, v2):
    m = [v1[1] * v2[2] - v1[2] * v2[1],
         v1[2] * v2[0] - v1[0] * v2[2],
         v1[0] * v2[1] - v1[1] * v2[0]]

    return m


# Used
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


# Used indirectly
def sign(n):
    if n >= 0:
        return 1
    elif n < 0:
        return -1

    return None


# Used indirectly
def signed_array(array):
    result = []
    for a in array:
        result.append(sign(a))

    return result


def same_sign(array):
    result = signed_array(array)
    result = set(result)

    if len(result) == 1:
        return True

    return False


# Used indirectly
def triangle_area(triangle):
    # Too hard to think about at 4am
    # Source: https://math.stackexchange.com/a/2169905

    p1, p2, p3 = triangle[0], triangle[1], triangle[2]

    x1, y1, z1 = p1[0], p1[1], p1[2]
    x2, y2, z2 = p2[0], p2[1], p2[2]
    x3, y3, z3 = p3[0], p3[1], p3[2]

    a = (x2 * y1) - (x3 * y1) - (x1 * y2) + (x3 * y2) + (x1 * y3) - (x2 * y3)
    b = (x2 * z1) - (x3 * z1) - (x1 * z2) + (x3 * z2) + (x1 * z3) - (x2 * z3)
    c = (y2 * z1) - (y3 * z1) - (y1 * z2) + (y3 * z2) + (y1 * z3) - (y2 * z3)

    # d = (a + b + c) ** .5
    d = ((a ** 2) + (b ** 2) + (c ** 2)) ** .5

    area = d / 2

    return area


# Used
def is_point_inside_triangle(point, triangle):
    total_area = triangle_area(triangle)

    a, b, c = triangle[0], triangle[1], triangle[2]

    t1 = triangle_area((a, b, point))
    t2 = triangle_area((a, c, point))
    t3 = triangle_area((b, c, point))

    decomposed_area = t1 + t2 + t3

    # print('[{}]   {} = ( {} + {} + {} )'.format(total_area, decomposed_area, t1, t2, t3))

    if abs(total_area - decomposed_area) < 0.00005:
        # The point belongs to the triangle
        return True

    return False


# Used
def intersection_line_plane(points, plane):
    p0, p1 = points[0], points[1]

    line = (p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2])

    # p0 * plane equation
    a = plane[0] * p0[0] + plane[1] * p0[1] + plane[2] * p0[2]

    # line * plane equation
    b = plane[0] * line[0] + plane[1] * line[1] + plane[2] * line[2]

    c = a + plane[3]
    t = -c / b

    point = (p0[0] + line[0] * t, p0[1] + line[1] * t, p0[2] + line[2] * t)

    return point


def get_intersection_points(triangle, plane):
    # Get intersection points between a triangle and a plane
    # If there are any intersection, we need to find the
    # two points that intersect a plane
    # Note that only two lines intersects this plane.
    # The third one results in a division by zero.

    pairs = [
        (triangle[0], triangle[1]),
        (triangle[0], triangle[2]),
        (triangle[1], triangle[2])
    ]

    points = []
    for pair in pairs:
        try:
            p = intersection_line_plane(pair, plane)
            points.append(p)
        except:
            pass

    # These points represents the line that is the intersection
    # between the two planes described by the triangles
    return points


def triangles_intersection(triangle_1, triangle_2, get_points=False):
    plane_triangle_1 = plane_equation(triangle_1)
    plane_triangle_2 = plane_equation(triangle_2)

    # This case verifies if the triangles are parallel
    ssd_t1_p2 = same_sign(
        signed_distance_array(triangle_1, plane_triangle_2)
    )
    ssd_t2_p1 = same_sign(
        signed_distance_array(triangle_2, plane_triangle_1)
    )
    if ssd_t1_p2 and ssd_t2_p1 is True:
        # Every plane separates the points
        if get_points:
            return []
        return False

    # This case is sufficient all of the other commutative cases
    # If there is only one intersection point, then we have a semi intersection case
    points = get_intersection_points(triangle_2, plane_triangle_1)
    intersect_points = []
    for p in points:
        if is_point_inside_triangle(p, triangle_1):
            intersect_points.append(p)

    # This case verifies if the one above fails
    if len(intersect_points) is 0:
        # Sadly this gives a recursion error, I'll fix one day...
        # intersect_points = triangles_intersection(triangle_2, triangle_1, get_points=get_points)
        points = get_intersection_points(triangle_1, plane_triangle_2)
        intersect_points = []
        for p in points:
            if is_point_inside_triangle(p, triangle_2):
                intersect_points.append(p)

    # This verifies edge intersection that is allowed
    if len(intersect_points) == 2:
        if (intersect_points[0] in triangle_1
                or intersect_points[1] in triangle_1
                or intersect_points[0] in triangle_2
                or intersect_points[1] in triangle_2):
            if get_points:
                return intersect_points
            return False

    # This verifies if the intersection is one point
    if len(intersect_points) == 2 and intersect_points[0] == intersect_points[1]:
        # Point intersection is allowed
        if get_points:
            return [intersect_points[0]]
        return False

    if get_points:
        return intersect_points
    return True


def main():
    # No intersect test (equal triangles) - commutative
    # T1 = [(0, 0, 0), (0, 10, 0), (10, 10, 0)]
    # T2 = [(0, 0, 0), (0, 10, 0), (10, 10, 0)]

    # No intersect test (parallel) - commutative
    # T1 = [(0, 0, 0), (0, 10, 0), (10, 10, 0)]
    # T2 = [(0,0, 5), (0, 10, 5), (10,10, 5)]

    # No intersect test (not parallel) - commutative
    # T1 = [(0, 0, 0), (0, 10, 0), (10, 10, 0)]
    # T2 = [(0, 0, 5), (0, 10, 1), (10, 10, 5)]

    # No intersect test (point intersection) - commutative
    # T1 = [(0, 0, 5), (0, 10, 0), (10, 10, 0)]
    # T2 = [(0, 0, 5), (0, 10, 5), (10, 10, 5)]

    # No intersect test (line intersection) - commutative
    # T1 = [(0, 0, 5), (0, 10, 5), (10, 10, 0)]
    # T2 = [(0, 0, 5), (0, 10, 5), (10, 10, 5)]

    # Intersect test (semi intersection) - commutative
    # T1 = [(0, 0, 0), (0, 10, 0), (10, 10, 0)]
    # T2 = [(2, 2, 5), (0, 10, -5), (11, 11, 5)]

    # Intersect test - sadly, not commutative
    T1 = [(0, 0, 0), (0, 10, 0), (10, 10, 0)]
    T2 = [(2, 2, 5), (0, 10, -5), (8, 8, 5)]

    # T1 blue, T2 green
    polygons = [T1, T2]
    points_to_plot = []
    for p in polygons:
        for i in p:
            points_to_plot.append(i)

    x = triangles_intersection(T1, T2, get_points=False)
    print(x)

    # points_to_plot.extend(x)

    # plot(polygons=polygons, points=points_to_plot)


if __name__ == "__main__":
    main()
