class Env:
    def __init__(self):
        self.x_range = 51  # size of background
        self.y_range = 31
        self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                        (1, 0), (1, -1), (0, -1), (-1, -1)]
        self.obs = self.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    def obs_map(self):
        """
        Initialize obstacles' positions
        :return: map of obstacles
        """

        x = self.x_range
        y = self.y_range
        obs = set()

        for i in range(x):
            obs.add((i, 0))
        for i in range(x):
            obs.add((i, y - 1))

        for i in range(y):
            obs.add((0, i))
        for i in range(y):
            obs.add((x - 1, i))

        # Environment 1

        """
        for i in range(10, 21):
            obs.add((i, 15))

        for i in range(15):
            obs.add((20, i))

        for i in range(15, 30):
            obs.add((30, i))
        
        for i in range(16):
            obs.add((40, i))
        """

        # Environment 2

        """
        for i in range(10,25):
            obs.add((10,i))

        for i in range(10,37):
            obs.add((i,25))

        for i in range(10,40):
            obs.add((i,10))

        for i in range(10,25):
            obs.add((40,i))
        """   

        # Environment 3

        
        for i in range(10):
            obs.add((i+5,i))
            obs.add((i,i+5))

        for i in range(15,20):
            obs.add((25-i,i))
            obs.add((35-i,i))

        for i in range(5,10):
            obs.add((40-i,i))
            obs.add((50-i,i))

        for i in range(20,26):
            obs.add((60-i,i))
            obs.add((70-i,i))
            obs.add((70-i-5,i+5))

        for i in range(10,20):
            obs.add((20+i,i))
            obs.add((30+i,i))

        for i in range(20,25):
            obs.add((i-15,i))
            obs.add((i-5,i))
            obs.add((i-15+5,i+5))

        for i in range(10,15):
            obs.add((i+5,i))

        for i in range(20,35):
            obs.add((i,25))  
              

        return obs