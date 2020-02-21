from affine import Affine

Affine.identity()
a = Affine(1.0, 0.0, 0.0, 0.0, 1.0, 0.0)
print(a)
print("transl: ")
print(a.translation(2.0, 3.0))
print("scale: ")
