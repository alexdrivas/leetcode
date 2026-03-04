class RecentCounter(object):

    def __init__(self):
        self.counter = 0
        self.recent_t = []
        
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        self.recent_t.append(t)
        self.counter+=1
        
        while t - self.recent_t[0] > 3000:
            value = self.recent_t.pop(0)
            self.counter-=1
        
        return self.counter