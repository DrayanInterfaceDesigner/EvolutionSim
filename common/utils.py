def lerp(a, b, t):
    return (1 - t) * a + t * b


def intersection(a, b, c, d) :
    T_TOP = (d.x - c.x) * (a.y - c.y) - (d.y - c.y) * (a.x - c.x)
    U_TOP = (c.y - a.y) * (a.x - b.x) - (c.x - a.x) * (a.y - b.y)
    BOTTOM = (d.y - c.y) * (b.x - a.x) - (d.x - c.x) * (b.y - a.y)

    if (BOTTOM != 0) :
        T = T_TOP / BOTTOM
        U = U_TOP / BOTTOM

        if (T >= 0 and T <= 1 and U >= 0 and U <= 1):
            return {"x": lerp(a.x, b.x, T),
                    "y": lerp(a.y, b.y, T), 
                    "offset": T}

    return None