import math

def first():
  result = []
  angle  = 0
  incr   = 1.0/16
  while angle < 1 and incr > 0.0001:
    result = result + [{'angle':angle, "size":1-angle}]
    angle += incr
    incr  *= 0.949341 # approximate root of -x^32 + 16x - 15
  return result

def next(loop, approx = 8):
  compress = 0.5
  offset   = 0
  result   = []
  while approx > 0:
    for l in loop:
      angle = l['angle'] * compress + offset
      size  = l['size'] * (1-angle)
      if size > 0.001:
        result = result + [{'angle': angle, 'size': size}]
    offset   += compress
    compress *= 0.5
    approx   -= 1
  return result

def output(depth):
  level = first()
  for i in range(depth):
    for x in level:
      print "%.15f\t%.15f" % (x['angle'] * 2 * math.pi, x['size'])
    print "\n"
    level = next(level)
