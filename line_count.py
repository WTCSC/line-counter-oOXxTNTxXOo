def line_count():
  #F for file      L for lines 
  F = open('file.txt', 'r') #opens file.txt to be read
  L = F.readlines() 
  t = len(L) #t = lines count
  F.close #closes file 
  return t