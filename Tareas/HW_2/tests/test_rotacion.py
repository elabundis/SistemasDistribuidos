import numpy as np
import repo.rotacion as student_code

from pytest_check import check


# Function names for rotations along each axis
func = {'x':student_code.rot_x,
        'y':student_code.rot_y,
        'z':student_code.rot_z}

def get_data(axis):
    point1 = np.array([1, 0, 0])  # i
    point2 = np.array([0, 1, 0])  # j
    point3 = np.array([0, 0, 1])  # k
    points = np.array([point1, point2, point3])

    theta = np.pi/2

    error = 1e-6
    if(axis=='x'):
        rotated_points = np.array([point1, point3, -point2])
    elif(axis=='y'):
        rotated_points = np.array([-point3, point2, point1])
    elif(axis=='z'):
        rotated_points = np.array([point2, -point1, point3])
    else:
        raise Exception("wrong axis")

    return (points, theta, rotated_points, error)

def check_type(point):
    return isinstance(point, np.ndarray)

def check_dimension(point):
    return  len(point.shape) == 1

def check_rotation(axis):
    points, theta, rotated_points, error = get_data(axis)
    rot_func = func[axis]
    for point, point_rotated in zip(points, rotated_points):
        point_check = rot_func(*point, theta)
        with check:
            assert isinstance(point_check, np.ndarray), f"wrong type:{type(point_check)}"

        point_check = np.array(point_check)
        assert check_dimension(point_check)

        point_check = np.array(point_check)
        assert np.all(
            np.abs(point_check - point_rotated) < error
        )

def test_rot_x():
    # Rotate i, j, and k around x axis
    check_rotation('x')

def test_rot_y():
    # Rotate i, j, and k around y axis
    check_rotation('y')

def test_rot_z():
    # Rotate i, j, and k around z axis
    check_rotation('z')

