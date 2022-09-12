'''
usage of get() method for looking for looking up a key while providing a fallback value.
'''
name_for_userid = {
  382: 'Alice',
  950: 'Bob',
  590: 'Dilbert',
}
def greeting(userid):
  try:
    return 'Hi {}!'.format(name_for_userid[userid])
  except KeyError:
    return 'Hi, Key not found.'
  
'''
more cleaner code
'''
def pythonicGreeting(userid):
  return 'Hi {}!'.format(name_for_userid.get(userid,', key not found'))
