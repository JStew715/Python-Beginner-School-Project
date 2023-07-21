def hello():
    name=str(input("enter your name : "))
    print("hello " + str(name))
    return
hello()

def statement():
    r=str(input("Enter a value: "))
    print("this program will calculate the area of a cube using the value provided: " + str(r))
    return
statement()

def areaofwholecube(r):
    sa=6*(r*r)
    print("surface area of the cube: " , sa)
areaofwholecube(4)

def areaofsidecube(r):
    sa=2*(2*r*r)
    print("surface area of side of the cube: " , sa)
areaofsidecube(1)


