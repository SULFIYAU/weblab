print("rectangle")
print("..........")
l=int(input("enter the legth of rectangle:"))
b=int(input("enter the breadth of rectangle:"))
area=lambda l,b:l*b
print("area of rectangle:",area (l,b))
perimeter=lambda l,b:2*(l+b)
print("area of perimeter:",perimeter(l,b))
print("square")
print("..........")
a=int(input("enter the side of the square:"))
area=lambda a:a*a
print("area:",area(a))
perimeter=lambda a:4*a
print("perimeter:",perimeter(a))


