def is_triangle(a,b,c):
  return (a+b > c) * (b+c > a) * (a+c > b)