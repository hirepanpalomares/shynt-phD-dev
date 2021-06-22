


class Region:

    def __init__(self):
        pass


class SurfaceSide(Region):

    def __init__(self, surface, side):
        self.surface = surface
        self.side = side

        print(surface)
        print(side)


