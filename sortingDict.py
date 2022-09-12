xs = {'a':4,'c':2,'b':3,'d':1}

sorted(xs.items())

#sorting dictionary with value
sorted(xs.items(),key =lambda x: x[1])

#sorting with value in reverse
sorted(xs.items(),key = lambda x:x[1], reverse = True)

#sorting dictionary with key
sorted(xs.items(),key =lambda x: x[0])

#sorting with value in reverse
sorted(xs.items(),key = lambda x:x[0], reverse = True)
