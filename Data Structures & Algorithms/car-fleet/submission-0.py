
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),key=lambda car :car[0],reverse = True)
        fleet = 0
        slow_eta_ahead = 0.0
        for pos,spd in cars:
            eta = (target-pos)/spd
            if eta > slow_eta_ahead:
                fleet += 1
                slow_eta_ahead = eta
        return fleet