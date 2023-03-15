# default
print("{0}  {1}".format("Hello", "World!"))

# cformat
import cprint
print("@56056{0}@45031{1}".cformat("Hello ", " World!"))
print("@56056{}@45031{}".cformat("Hello ", " World!"))
print("@56056{}@45031[ World!]".cformat("Hello "))
print("@56056{0}@45031[ World!]".cformat("Hello "))

# iformat theme 1
cprint.custom_style = {1: 612, 2: 1224}
print("@1{0}@2{1}".iformat("Hello ", " World!"))
print("@1{0}@2[ World!]".iformat("Hello "))

# iformat theme 2
cprint.custom_style = {1: 5547, 2: 66795}
print("@1{0}@2{1}".iformat("Hello ", " World!"))
print("@1{0}@2[ World!]".iformat("Hello "))

# DATA
print(" NOW: @NOW @56056{0}@45031{1}".cformat("Hello ", " World!"))
print("DATE: @DATE @1{0}@2{1}".iformat("Hello ", " World!"))
print("TIME: @TIME @1{0}@2{1}".iformat("Hello ", " World!"))