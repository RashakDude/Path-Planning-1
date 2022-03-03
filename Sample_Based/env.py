class Env:
    def __init__(self):
        self.x_range = (0, 50)
        self.y_range = (0, 30)
        self.obs_boundary = self.obs_boundary()
        self.obs_circle = self.obs_circle()
        self.obs_rectangle = self.obs_rectangle()

    @staticmethod
    def obs_boundary():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30]
        ]
        return obs_boundary

    @staticmethod
    def obs_rectangle():

        # Environment 1

        obs_rectangle = [
            [20, 0, 1, 15, 0],
            [10, 15, 11, 1, 0],
            [30, 15, 1, 15, 0],
            [40, 0, 1, 16, 0]
        ]

        # Environment 2
        """
        obs_rectangle = [
            [10, 10, 30, 1, 0],
            [10, 10, 1, 15, 0],
            [10, 25, 25, 1, 0],
            [40, 10, 1, 15, 0]
        ]
        """
        return obs_rectangle

    @staticmethod
    def obs_circle():
        obs_cir = []
        return obs_cir
    
