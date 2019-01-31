def gcd(a, b):
  return a if b == 0 else gcd(b, a%b) 

def xgcd(a, b):
  x0, x1, y0, y1 = 0, 1, 1, 0
  while a != 0:
    q, b, a = b // a, a, b % a
    y0, y1 = y1, y0 - q * y1
    x0, x1 = x1, x0 - q * x1
  return b, x0, y0

def diophantine_values(r, g, a, b, x1, y1):
  return (x1-r*b/g,y1+r*a/g)

if __name__ == "__main__":
  print(gcd(24,16))
  print("Linear diophantine equation input form ax+by=c")
  a,b,c = [int(input(x+"=")) for x in "abc"]
  g, x, y = xgcd(a,b)
  if g % c != 0:
    print("There are no solutions")
  k = c / g
  x*=k
  y*=k
  print("Solution for r=0:")
  print(diophantine_values(0,g,a,b,x,y))
  while True:
    r=int(input("r="))
    print("Solution for r=" + str(r) + ":")
    print(diophantine_values(r,g,a,b,x,y))
