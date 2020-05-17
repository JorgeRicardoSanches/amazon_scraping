i = 0
def callback(index):
  print("kgs")
  index += 1
  callback(index)

callback(i)
