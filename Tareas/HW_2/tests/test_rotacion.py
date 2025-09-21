import numpy as np
import repo.rotacion as student_code

from pytest_check import check


# Function names for rotations along each axis
func = {'x':student_code.rot_x,
        'y':student_code.rot_y,
        'z':student_code.rot_z,
        'rot': student_code.rotar
       }

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
    # Consider theta in degrees too
    theta2 = theta * 180 / np.pi
    # Consider rotation in clockwise sense
    theta3 = -theta
    # Consider rotation in clockwise sense in degrees
    theta4 = -theta * 180 / np.pi
    rot_func = func[axis]
    for point, point_rotated in zip(points, rotated_points):
        point_check = rot_func(*point, theta)
        point_check2 = rot_func(*point, theta2)
        point_check3 = rot_func(*point, theta3)
        point_check4 = rot_func(*point, theta4)
        with check:
            assert isinstance(point_check, np.ndarray), (
                f"wrong type:{type(point_check)}"
            )

        point_check = np.array(point_check)
        point_check2 = np.array(point_check2)
        point_check3 = np.array(point_check3)
        point_check4 = np.array(point_check4)
        assert check_dimension(point_check)

        assert np.all(
            np.abs(point_check - point_rotated) < error
        ) or np.all(
            np.abs(point_check2 - point_rotated) < error
        ) or np.all(
            np.abs(point_check3 - point_rotated) < error
        ) or np.all(
            np.abs(point_check4 - point_rotated) < error
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

def test_rotar():
    axes = ['x', 'y', 'z']
    for axis in axes:
        points, theta, rotated_points, error = get_data(axis)
        # Consider theta in degrees too
        theta2 = theta * 180 / np.pi
        # Consider rotation in clockwise sense
        theta3 = -theta
        # Consider rotation in clockwise sense in degrees
        theta4 = -theta * 180 / np.pi
        for point, point_rotated in zip(points, rotated_points):
            with check:
                point_check = func['rot'](*point, theta, axis)
                point_check = np.array(point_check)
                point_check2 = func['rot'](*point, theta2, axis)
                point_check2 = np.array(point_check2)
                point_check3 = func['rot'](*point, theta3, axis)
                point_check3 = np.array(point_check3)
                point_check4 = func['rot'](*point, theta4, axis)
                point_check4 = np.array(point_check4)
                assert np.all(
                    np.abs(point_check - point_rotated) < error
                ) or np.all(
                    np.abs(point_check2 - point_rotated) < error
                ) or np.all(
                    np.abs(point_check3 - point_rotated) < error
                ) or np.all(
                    np.abs(point_check4 - point_rotated) < error
                )
