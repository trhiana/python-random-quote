import random

def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  length = len(quotes)
  randomIndex = random.randint(0, length-1)
  randomQuote = quotes[randomIndex].rstrip()
  print(randomQuote)

if __name__== "__main__":
  primary()
