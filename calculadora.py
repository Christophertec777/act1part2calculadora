def division(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def main():
    print("División:", division(5, 3))

if _name_ == "_main_":
    main()
