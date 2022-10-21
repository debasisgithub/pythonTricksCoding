my_items = ['a','b','c']
for item in my_items:
  print(item)
  
#what if you need an item index for example.
#It is possible to write loops that keep a running index while avoiding the range(len(..)) pattern.
# The enumerate() built-in helps you make those kinds of loops nice and pythonic:

for i,item in enumerate(my_items):
  print('{}:{}'.format(i,item))