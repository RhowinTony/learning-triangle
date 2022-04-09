"""
input = 1235
output = abce

"""

def barcode(number):
    alpha_code = "-abcdefgij"
    r_val = ""   
    for i in number.strip():
        r_val = r_val+alpha_code[int(i)]
    return r_val

    
def main():
    try:
        number = abs(int(input("Enter the barcode ")))
    except ValueError:
        print("invalid input - Please enter a numerical code")
    else:
        output = barcode(f"{number}")
        print(f"The alpha code of {number} is {output}")
    finally:
        print("--*--"*12)
main()







