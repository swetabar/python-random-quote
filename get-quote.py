import random
def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rand = random.randint(0, last)
  print(quotes[rand])

if __name__== "__main__":
  primary()
