def safe_print_list(my_list=[], x=0):
  count = 0
  try:
      for i in range(x):
          print(my_list[i], end="")
          count += 1
  except IndexError:
      pass
  print()
  return count
nbp=safe_print_list([2,4,6,33,4],3)
print("nb_print: {:d}".format(nbp))