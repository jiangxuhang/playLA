from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == "__main__":
    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    print(T.dot(p))