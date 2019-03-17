import numpy as np


class Perceptron:
    def __init__(self, weights, bias):
        self.w = np.array(weights)
        self.b = bias
        self.i = len(weights)  # input amount

    def calc(self, inputs):
        if len(inputs) != self.i:
            raise Exception("Invalid input size")

        r = np.dot(np.array(inputs), self.w)
        s = np.sum(r) + self.b
        return True if s > 0 else False


def test(p, title):
    print(title)
    print(f"[0, 0] {p.calc([0, 0])}")
    print(f"[0, 1] {p.calc([0, 1])}")
    print(f"[1, 0] {p.calc([1, 0])}")
    print(f"[1, 1] {p.calc([1, 1])}")


def main():
    AND = Perceptron((1, 1), -1.5)
    test(AND, "AND Gate")
    NAND = Perceptron((-2, -2), 3)
    test(NAND, "NAND Gate")
    OR = Perceptron((1, 1), -0.5)
    test(OR, "OR Gate")
    NOR = Perceptron((-1, -1), 0.5)
    test(NOR, "NOR Gate")
    NOT = Perceptron((-1, ), 0.5)
    print("NOT Gate")
    print(f"[0] {NOT.calc((0,))}")
    print(f"[1] {NOT.calc((1,))}")


if __name__ == '__main__':
    main()
