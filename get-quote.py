import random

def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  length = len(quotes) - 1
  randomQuote = random.randint(0, length)
  print(quotes[randomQuote])

if __name__== "__main__":
  primary()
