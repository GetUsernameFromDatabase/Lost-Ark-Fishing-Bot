class Counter:
    def __init__(self, initialValue: int = 0, maxValue: int = 0):
        self.__initalValue = initialValue

        self.count = initialValue
        self.maxValue = maxValue

    def increase(self, amount: int = 1):
        """
        Increases count by the given amount (default: 1)

        Returns:
            bool: True if count is above or equal to the max value
        """
        self.count += amount
        return self.isAboveEqualToMax()

    def decrease(self, amount: int = 1):
        """
        Decreases count by the given amount (default: 1)

        Returns:
            bool: True if count is above or equal to the max value
        """
        self.count -= amount
        return self.isAboveEqualToMax()

    def isAboveEqualToMax(self):
        return self.count >= self.maxValue

    def reset(self):
        self.count = self.__initalValue
