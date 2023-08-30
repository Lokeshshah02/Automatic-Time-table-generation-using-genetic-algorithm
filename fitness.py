BITCOUNT = 10


def fitness(member):
  if member < 0 or member >= 1:
    return -1
  elif member >= 0 and member < 2:
    return 60.0
  elif member >= 2 and member < 3:
    return member + 30.0
  elif member >= 3 and member < 4:
    return 120.0
  elif member >= 4 and member < 5:
    return -0.83333 * member + 220
  elif member >= 5 and member < 6:
    return 1.75 * member - 322.5
  elif member >= 6 and member < 7:
    return 150.0
  elif member >= 7 and member < 8:
    return 2.0 * member - 450
  elif member >= 8 and member < 9:
    return -1.8 * member + 918
  else:
    return 0

if __name__ == "__main__":
  for i in range(0, 1024):
    print (i, fitness(i))
