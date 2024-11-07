

class Stability:
    def __init__(self, stabilityValue: float = 50.0) -> None:
        self.stabilityValue: float = stabilityValue
        self.baseStability: float = 50.0
        self.stabilizationCoefficient: float = 0.05

    def increaseStability(self, points: float) -> None:
        self.stabilityValue = round(min(100, self.stabilityValue + points), 2)

    def decreaseStability(self, points: float) -> None:
        self.stabilityValue = round(max(0, self.stabilityValue - points), 2)

    def stabilizationOfStability(self) -> None:
        if self.stabilityValue > self.baseStability:
            step: float = self.stabilizationCoefficient * (self.stabilityValue - self.baseStability)
            self.decreaseStability(step)
        elif self.stabilityValue < self.baseStability:
            step: float = self.stabilizationCoefficient * (self.baseStability - self.stabilityValue)
            self.increaseStability(step)
        
        self.stabilityValue = round(max(0, min(100, self.stabilityValue)), 2)
