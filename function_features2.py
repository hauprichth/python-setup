def arb_args(*args):
  for x in args:
    print(x)

arb_args(1,2,3,4,5,6,7,8,9)

def inner_func(x,y):
  def inner_1():
    return x+y
  def inner_2():
    return x-y
  print(inner_1()+inner_2())

inner_func(12,6)


def lunch_lady(name, lunch="Mystery Meat"):
  print(name, lunch)

lunch_lady("Joe", "PB&J")
lunch_lady("Jane")

def sum_n_product(x,y):
  return x+y,x*y

print(sum_n_product(2,3))

alias_arb_args = arb_args


def arb_mean(*args):
  total = 0
  for x in args:
    total += x
  print(x/len(args))

def arb_longest_string(*args):
  long = 0
  longest = ""
  for x in args:
    if len(x) > long:
      long = len(x)
      longest = x
  return longest