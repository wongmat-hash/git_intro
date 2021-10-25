import unittest
from task import mystery_func2
class TestCase(unittest.TestCase):
  def test1(self):
    a = 2
    self.assertGreater(mystery_func2(a),0)

  def test2(self):
    a = 1
    self.assertEqual(mystery_func2(a),100)

if __name__ == '__main__':
  unittest.main(verbosity=2)




# This function is contrived and serves no purpose
def mystery_func2(a):
  b = 0
  if a>1 or a==0:
    b = 10
  return 100/b
