"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter

class Test(unittest.TestCase):
   def setUP(self):
      self.instance = Counter()
      
   def test_both_have_the_same_count(self):
      a = Counter()
      a.increment()
      a.increment()
      b = Counter()
      b.increment()
      self.assertEqual(a.count, b.count)
   
   def test_both_instance_are_the_same(self):
      a = Counter()
      b = Counter()
      b.increment()
      self.assertIs(a, b)
   
   def test_check_memory_address(self):
      a = Counter()
      b = Counter()
      self.assertEqual(id(a), id(b))
      
   def test_counter_initiate_with_count_is_zero(self):
      a = Counter()
      self.assertEqual(0, a.count)
      
   def test_counter_counting_properly(self):
      a = Counter()
      a.increment()
      a.increment()
      self.assertEqual(2, a.count)
            
      
if __name__ == "__main__":
   unittest.main()
      

