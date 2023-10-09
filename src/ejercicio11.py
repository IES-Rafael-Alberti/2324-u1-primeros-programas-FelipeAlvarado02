

def sumaDeSusAnteriores(num:int):
    num = (num*(num+1))//2
    return str(num)

if __name__ == "__main__":

    print(sumaDeSusAnteriores(int(input("Introduce el número:\n"))))