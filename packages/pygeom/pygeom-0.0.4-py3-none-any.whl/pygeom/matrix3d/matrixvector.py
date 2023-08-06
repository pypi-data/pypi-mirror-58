from pygeom.geom3d import Vector
from numpy.matlib import matrix, zeros, multiply

class MatrixVector(object):
    """Vector Class"""
    x = None
    y = None
    z = None
    def __init__(self, x: matrix, y: matrix, z: matrix):
        self.x = x
        self.y = y
        self.z = z
    def to_unit(self):
        """Returns the unit matrixvector of this matrixvector"""
        mag = self.return_magnitude()
        x = zeros(self.shape)
        y = zeros(self.shape)
        z = zeros(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if mag[i, j] != 0:
                    x[i, j] = self.x[i, j]/mag[i, j]
                    y[i, j] = self.y[i, j]/mag[i, j]
                    z[i, j] = self.z[i, j]/mag[i, j]
        return MatrixVector(x, y, z)
    def return_magnitude(self):
        """Returns the magnitude matrix of this matrixvector"""
        mag = zeros(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                mag[i, j] += self.x[i, j]**2
                mag[i, j] += self.y[i, j]**2
                mag[i, j] += self.z[i, j]**2
                mag[i, j] = mag[i, j]**0.5
        return mag
    def __getitem__(self, key):
        x = self.x[key]
        y = self.y[key]
        z = self.z[key]
        if isinstance(x, matrix):
            return MatrixVector(x, y, z)
        elif isinstance(x, float):
            return Vector(x, y, z)
        else:
            print('Did nothing!')
    def __setitem__(self, key, value):
        if isinstance(value, Vector) and isinstance(key, tuple):
            if len(key) == 2:
                if isinstance(key[0], int) and isinstance(key[1], int):
                    self.x[key] = value.x
                    self.y[key] = value.y
                    self.z[key] = value.z
        elif isinstance(value, MatrixVector) and isinstance(key, tuple):
            if len(key) == 2:
                self.x[key] = value.x
                self.y[key] = value.y
                self.z[key] = value.z
    @property
    def shape(self):
        return self.x.shape
    def transpose(self):
        x = self.x.transpose()
        y = self.y.transpose()
        z = self.z.transpose()
        return MatrixVector(x, y, z)
    def sumall(self):
        x, y, z = 0.0, 0.0, 0.0
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                x += self.x[i, j]
                y += self.y[i, j]
                z += self.z[i, j]
        return Vector(x, y, z)
    def tolist(self):
        lst = []
        for i in range(self.shape[0]):
            lst.append([])
            for j in range(self.shape[1]):
                x = self.x[i, j]
                y = self.y[i, j]
                z = self.z[i, j]
                lst[-1].append(Vector(x, y, z))
        return lst
    def copy(self):
        x = self.x.copy()
        y = self.y.copy()
        z = self.z.copy()
        return MatrixVector(x, y, z)
    # def __rmul__(self, obj):
    #     if isinstance(obj, (Vector, MatrixVector)):
    #         return obj.x*self.x+obj.y*self.y+obj.z*self.z
    #     else:
    #         x = obj*self.x
    #         y = obj*self.y
    #         z = obj*self.z
    #         return MatrixVector(x, y, z)
    def __mul__(self, obj):
        if isinstance(obj, (Vector, MatrixVector)):
            return self.x*obj.x+self.y*obj.y+self.z*obj.z
        else:
            x = self.x*obj
            y = self.y*obj
            z = self.z*obj
            return MatrixVector(x, y, z)
    def __rmul__(self, obj):
        return self.__mul__(obj)
    # def __matmul__(self, obj):
    #     if isinstance(obj, matrix):
    #         x = self.x@obj
    #         y = self.y@obj
    #         z = self.z@obj
    #         return MatrixVector(x, y, z)
    # def __rmatmul__(self, obj):
    #     return self.__matmul__(obj)
    def __truediv__(self, obj):
        if isinstance(obj, (int, float, complex)):
            x = self.x/obj
            y = self.y/obj
            z = self.z/obj
            return MatrixVector(x, y, z)
    def __pow__(self, obj):
        if isinstance(obj, Vector):
            x = self.y*obj.z-self.z*obj.y
            y = self.z*obj.x-self.x*obj.z
            z = self.x*obj.y-self.y*obj.x
            return MatrixVector(x, y, z)
        elif isinstance(obj, MatrixVector):
            x = self.y*obj.z-self.z*obj.y
            y = self.z*obj.x-self.x*obj.z
            z = self.x*obj.y-self.y*obj.x
            return MatrixVector(x, y, z)
    def __add__(self, obj):
        if isinstance(obj, MatrixVector):
            x = self.x+obj.x
            y = self.y+obj.y
            z = self.z+obj.z
            return MatrixVector(x, y, z)
    def __radd__(self, obj):
        if obj is None:
            return self
        else:
            return self.__add__(obj)
    def __sub__(self, obj):
        if isinstance(obj, MatrixVector):
            x = self.x-obj.x
            y = self.y-obj.y
            z = self.z-obj.z
            return MatrixVector(x, y, z)
    def __pos__(self):
        return MatrixVector(self.x, self.y, self.z)
    def __neg__(self):
        return MatrixVector(-self.x, -self.y, -self.z)
    def __repr__(self):
        return '<MatrixVector: {:}, {:}, {:}>'.format(self.x, self.y, self.z)
    def __str__(self):
        return 'x:\n{:}\ny:\n{:}\nz:\n{:}'.format(self.x, self.y, self.z)
    def __format__(self, format_spec):
        frmstr = 'x:\n{:'+format_spec+'}\ny:\n{:'+format_spec+'}\nz:\n{:'+format_spec+'}'
        return frmstr.format(self.x, self.y, self.z)

def zero_matrix_vector(shape: tuple):
    x = zeros(shape)
    y = zeros(shape)
    z = zeros(shape)
    return MatrixVector(x, y, z)

def solve_matrix_vector(a: matrix, b: MatrixVector):
    from numpy.linalg import solve
    newb = zeros((b.shape[0], b.shape[1]*3))
    for i in range(b.shape[1]):
        newb[:, 3*i+0] = b[:, i].x
        newb[:, 3*i+1] = b[:, i].y
        newb[:, 3*i+2] = b[:, i].z
    newc = solve(a, newb)
    c = zero_matrix_vector(b.shape)
    for i in range(b.shape[1]):
        c[:, i] = MatrixVector(newc[:, 3*i+0], newc[:, 3*i+1], newc[:, 3*i+2])
    return c

def elementwise_multiply(a: matrix, b: MatrixVector) -> MatrixVector:
    if a.shape[0] == b.shape[0] and a.shape[0] == b.shape[0]:
        x = multiply(a, b.x)
        y = multiply(a, b.y)
        z = multiply(a, b.z)
        return MatrixVector(x, y, z)
        # c = zero_matrix_vector(a.shape)
        # for i in range(a.shape[0]):
        #     for j in range(a.shape[1]):
        #         c[i, j] = a[i, j]*b[i, j]
        # return c

def elementwise_dot_product(a: MatrixVector, b: MatrixVector):
    if a.shape[0] == b.shape[0] and a.shape[0] == b.shape[0]:
        c = multiply(a.x, b.x) + multiply(a.y, b.y) + multiply(a.z, b.z)
        return c

def elementwise_cross_product(a: MatrixVector, b: MatrixVector):
    if a.shape[0] == b.shape[0] and a.shape[0] == b.shape[0]:
        x = multiply(a.y, b.z)-multiply(a.z, b.y)
        y = multiply(a.z, b.x)-multiply(a.x, b.z)
        z = multiply(a.x, b.y)-multiply(a.y, b.x)
        return MatrixVector(x, y, z)
        # c = zero_matrix_vector(a.shape)
        # for i in range(a.shape[0]):
        #     for j in range(a.shape[1]):
        #         c[i, j] = a[i, j]**b[i, j]
        # return c
