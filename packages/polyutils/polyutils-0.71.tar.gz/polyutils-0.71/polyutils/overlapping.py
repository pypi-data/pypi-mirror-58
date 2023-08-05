from itertools import combinations as combine
import numpy as np

DECIMALS = 5


def get_planes_and_vertex_of_pol(pol):
    """
    It is obvious
    :param pol: an object like Polygon
    :return: returns the list of planes and the list of vertex of a polygon
    """
    vertex_pol = [*zip(*pol.vertex)]
    planes = []

    for f in pol.faces:
        faces_planes = []
        for v in f[0:3]:  # Only the three first vertex are necessary
            faces_planes.append(vertex_pol[v])

        # Create all the planes of a polygon
        plane = plane_equation(faces_planes[0], faces_planes[1], faces_planes[2])
        planes.append(plane)

    return planes, vertex_pol


def plane_separating_set(plane, points1, points2):
    """
    Give a plane and two sets of points, this function checks if the plane separates the two sets
    :param plane: array defining the plane equation
    :param points1: a set of 3D points
    :param points2: a set of 3D points
    :return: True if given plane separates the tho sets, False if does not.
    """

    side_a = all_points_same_side(plane, points1)
    side_b = all_points_same_side(plane, points2)

    # print('Sides: ',side_a, side_b)

    if side_a is False or side_b is False:
        return False
    if side_a == -1 * side_b:
        return True
    return False


def is_convex(pol):
    plane, points = get_planes_and_vertex_of_pol(pol)

    for pl in plane:
        if not all_points_same_side(pl, points):
            print(pol.id_pol)
            return False

    return True


def all_points_same_side(plane, points, admit_zero=True):
    """
    if all points are on the same side of a plane, it returns the side (1 or -1), else
    returns False
    :param plane: array defining the plane equation
    :param points: a set of 3D points
    :param admit_zero: if point intersection is not allowed
    :return: 1, -1 or False
    """

    results = []
    for p in points:
        s = point_plane_side(plane, p)
        results.append(s)

    results = set(results)

    if admit_zero:
        results.discard(0)

    if len(results) == 1:
        return list(results)[0]
    return False


def point_plane_side(plane, point):
    """
    Return the side of a plane where the point is located
    :param plane: plane: array defining the plane equation
    :param point: a 3D point
    :return: -1 or 1 if is located in any side, or 0 if it is on plane
    """

    # NumPy is so slow!!!
    # v = np.dot(point, plane[0:3]) + plane[3]
    # v = np.round(v, decimals=DECIMALS)

    v = point[0] * plane[0] + point[1] * plane[1] + point[2] * plane[2] + plane[3]

    if abs(v) < 0.00001:
        v = 0

    v = np.sign(v)

    return v


def plane_equation(a, b, c):
    """
    This function calculates an equation given three points
    :param a: a 3D point
    :param b: a 3D point
    :param c: a 3D point
    :return: an array [a b c d] thar represents the plane equation formula
    ax + by + cz + d = 0
    """
    ab = [b[0] - a[0], b[1] - a[1], b[2] - a[2]]
    ac = [c[0] - a[0], c[1] - a[1], c[2] - a[2]]

    # NumPy is so slow!!!
    # cv = np.cross(ab, ac)
    # d = np.dot(cv, a)
    # cv = np.append(cv, -d)

    cv = [ab[1] * ac[2] - ab[2] * ac[1],
          ab[2] * ac[0] - ab[0] * ac[2],
          ab[0] * ac[1] - ab[1] * ac[0]]

    d = cv[0] * a[0] + cv[1] * a[1] + cv[2] * a[2]

    cv.append(-d)

    return cv


def overlap_list(polygons):
    """
    Return those polygons whose are overlapping.
    :param polygons: list of polygons
    :return: True and the pairs of overlapping polygons, or False.
    """
    pairs = list(combine(polygons, 2))
    print('Overlapping pairs:     ', len(pairs))
    bad_polygons = []

    for pol in pairs:
        if overlap(pol[0], pol[1]) is True:
            bad_polygons.append(pol[0])
            bad_polygons.append(pol[1])

    if len(bad_polygons) == 0:
        return False, None
    return True, bad_polygons


def overlap(pol1, pol2):
    """
    A geometry based function that verifies if two polygons overlaps or not.
    :param pol1: Polygon 1
    :param pol2: Polygon 2
    :return: True if the polygons overlap, False if does not.
    """
    planes1, v1 = get_planes_and_vertex_of_pol(pol1)
    planes2, v2 = get_planes_and_vertex_of_pol(pol2)

    for pl in planes1:
        if plane_separating_set(pl, v1, v2) is True:
            return False

    for pl in planes2:
        if plane_separating_set(pl, v1, v2) is True:
            return False

    return True


def main():
    from polyutils import Rectangle as r
    from polyviewer import PolyViewer1 as p
    a = r([1, 2, 3], 1)
    b = r([.5, .5, .5], 1)
    b.change_vertex([1, 2, 3])

    print(b.vertex)

    v = p(lim=[5, 5, 5])
    v.objects.extend([a, b])
    v.animate()
    v.show()

    print(overlap(a, b))


if __name__ == "__main__":
    main()
