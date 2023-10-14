def linearsearchproduct(productlist,targetproduct):
  indices=[]
  for index, product in enumerate(productlist):
      if product==targetproduct:
        indices.append(index) 
        return indices
products=["bangles","chain","earing"]
target="bangles"
target="saree"
result=linearsearchproduct(products,target)
print(result)