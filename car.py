class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.angle = 0

    def test1(self):
        return self.x + self.y


if __name__ == '__main__':
    car1 = Car(45, 50)
    assert car1.test1() == 95
