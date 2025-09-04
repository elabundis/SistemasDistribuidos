import numpy as np

def area_circulo(radio:float) -> float:
    """
    Calcula el area de un círculo utlizando su radio.

    Parameters:
        radio (float): radio del circulo.

    Returns:
        float: el area del circulo
    """
    area = np.pi * radio**2
    return area

