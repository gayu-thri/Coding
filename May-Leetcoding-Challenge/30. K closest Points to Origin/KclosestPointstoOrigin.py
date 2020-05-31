class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        #origin = [0,0]
        
        distance = [(math.sqrt(point[0]**2 + point[1]**2),point) for point in points]
        return [point for dist,point in sorted(distance)[:K]]