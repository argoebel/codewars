def find_short(s):
  return min(list(map(len, s.split(' '))))

  def find_short(s):
    return min(len(x) for x in s.split())