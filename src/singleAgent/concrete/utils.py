# -*- coding: utf-8 -*-

def getFileName(R,S,T,P):
    return "ConcreteSubstraction_%.0f%.0f%.0f%.0f.xlsx" %(R,S,T,P)

def main():
    print(getFileName(-1,-3,0,-2))
  
if __name__== "__main__":
    main()

