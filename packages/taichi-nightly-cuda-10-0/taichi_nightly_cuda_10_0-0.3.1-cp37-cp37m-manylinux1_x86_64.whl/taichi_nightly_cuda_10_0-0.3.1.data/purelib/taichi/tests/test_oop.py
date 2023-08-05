import taichi as ti


@ti.host_arch
def test_oop():

  class Array2D:

    def __init__(self, n, m, increment):
      self.n = n
      self.m = m
      self.val = ti.var(ti.f32)
      self.total = ti.var(ti.f32)
      self.increment = increment

    def place(self, root):
      root.dense(ti.ij, (self.n, self.m)).place(self.val)
      root.place(self.total)

    @ti.classkernel
    def inc(self):
      for i, j in self.val:
        ti.atomic_add(self.val[i, j], self.increment)

    @ti.classkernel
    def inc2(self, increment: ti.i32):
      for i, j in self.val:
        ti.atomic_add(self.val[i, j], increment)

    @ti.classkernel
    def reduce(self):
      for i, j in self.val:
        ti.atomic_add(self.total, self.val[i, j] * 4)

  arr = Array2D(128, 128, 3)

  double_total = ti.var(ti.f32)

  @ti.layout
  def place():
    ti.root.place(
        arr)  # Place an object. Make sure you defined place for that obj
    ti.root.place(double_total)
    ti.root.lazy_grad()

  arr.inc()
  arr.inc(
      __gradient=True
  )  # instead of arr.inc.grad due to python method bounding... Or just use ti.Tape
  assert arr.val[3, 4] == 3
  arr.inc2(4)
  assert arr.val[3, 4] == 7

  with ti.Tape(loss=arr.total):
    arr.reduce()

  for i in range(arr.n):
    for j in range(arr.m):
      assert arr.val.grad[i, j] == 4

  @ti.kernel
  def double():
    double_total[None] = 2 * arr.total

  with ti.Tape(loss=double_total):
    arr.reduce()
    double()

  for i in range(arr.n):
    for j in range(arr.m):
      assert arr.val.grad[i, j] == 8
