def orth_triangle(cath1 = 0, hyp = 0, cath2 = 0)->"float":
# Finds the third side of a triangle
    if cath1 > hyp or cath2 > hyp:
        print(None)
    elif cath1 == 0:
        cath1 = (hyp**2 - cath2**2)**(0.5)
        print(cath1)
    elif cath2 == 0:
        cath2 = (hyp**2 - cath1**2)**(0.5)
        print(cath2)
    elif hyp == 0:
        hyp = (cath1**2 + cath2**2)**(0.5)
        print(hyp)
  
orth_triangle(hyp = 15, cath1 = 7)
