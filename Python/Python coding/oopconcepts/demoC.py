from oopconcepts.demoA import A
from oopconcepts.demoB import B


class C(B, A):
    def __init__(self, n1, n2, msg):
        A.__init__(self, n1, n2)   # initialize A
        B.__init__(self, msg)      # initialize B

    def display(self):
        A.display(self)
        B.display(self)

    def final(self):
        print("Done")
