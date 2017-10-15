from math import sqrt


def get_roots(a, b, c):
    """Returns roots of quadratic equation a*x^2 + b*x + c = 0.

    Returns 2 roots if discriminant > 0, 1 root if discriminant == 0,
    and no roots if discriminant is negative.

    Arguments:
        a (float): a-coefficient of quadratic equation.
        b (float): b-coefficient of quadratic equation.
        c (float): c-coefficient of quadratic equation.

    Returns:
        root1 (float): the first root of quadratic equation.
        root2 (float): the second root of quadratic equation.
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2
