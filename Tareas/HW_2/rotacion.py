import numpy as np

def create_point(x, y, z):
    return np.array([x, y, z], dtype=float)

def rot_x(x, y, z, theta):
    '''
    Descripcion

    Parameters:
        param_name (data_type): brief description
        param_name (data_type): brief description

    Returns:
        data_type: brief description
    '''
    point = create_point(x, y, z)
    rotar_x = np.array(
                       [[1, 0, 0],
                       [0, np.cos(theta), -np.sin(theta)],
                       [0, np.sin(theta), np.cos(theta)]],
                       dtype = float
    )
    return np.matmul(rotar_x, point)

def rot_y(x, y, z, theta):
    '''
    Descripcion

    Parameters:
        param_name (data_type): brief description
        param_name (data_type): brief description

    Returns:
        data_type: brief description
    '''
    point = create_point(x, y, z)
    rotar_y = np.array(
                       [[np.cos(theta), 0, np.sin(theta)],
                       [0, 1, 0],
                       [-np.sin(theta), 0, np.cos(theta)]],
                       dtype = float
    )
    return np.matmul(rotar_y, point)

def rot_z(x, y, z, theta):
    '''
    Descripcion

    Parameters:
        param_name (data_type): brief description
        param_name (data_type): brief description

    Returns:
        data_type: brief description
    '''
    point = create_point(x, y, z)
    rotar_z = np.array(
                       [[np.cos(theta), -np.sin(theta), 0],
                       [np.sin(theta), np.cos(theta), 0],
                       [0, 0, 1]],
                       dtype = float
    )
    return np.matmul(rotar_z, point)


def rotar(x, y, z, theta, axis):
    '''
    Descripcion

    Parameters:
        param_name (data_type): brief description
        param_name (data_type): brief description
        param_name (data_type): brief description
        param_name (data_type): brief description
        axis (string): eje de rotacion; puede tomar valor 'x', 'y' o 'z'.

    Returns:
        data_type: brief description
    '''
    axis = axis.lower()
    if(axis=='x'):
        return rot_x(x, y, z, theta)
    elif(axis=='y'):
        return rot_y(x, y, z, theta)
    elif(axis=='z'):
        return rot_z(x, y, z, theta)
    else:
        raise Exception('wrong axis; choose "x", "y", or "z"')

