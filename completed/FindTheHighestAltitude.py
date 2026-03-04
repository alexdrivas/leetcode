class Solution:
    def largestAltitude(self, gain: List[int]) -> int:


        """
        gain = [-5, 1, 5, 0, -7]
        Return max of altitude[]
        """

        altitude = [0]
        for i in range(len(gain)):
            new_altitude = gain[i] + altitude[i] 
            altitude.append(new_altitude)
        return max(altitude)

        