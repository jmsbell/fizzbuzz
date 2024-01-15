"""
Prints the Fizz Buzz sequence up to a given number.
"""

def main():
    """
    Ask user for last number
    Count from 1 to last number.
    Answer with "fizz" if divisible by 3, "buzz" if divisible by 5, "fizzbuzz" if divisible by 3 and 5
    """
    last_number = int(input("Number to count to: "))
    fizzcount = 0
    buzzcount = 0 
    fizzbuzzcount = 0

    for i in range(1, last_number +1):
        fizz = (i % 3 == 0) and (i!=0)
        buzz = (i % 5 == 0) and (i!=0)
        fizzbuzz = (i % 15 == 0) and (i!=0)
        if fizzbuzz:
            print("Fizzbuzz")
            #add to fizzbuzz total
            fizzbuzzcount = fizzbuzzcount +1
        elif fizz:
            print("Fizz")
            #add to fizz total
            fizzcount = fizzcount +1
        elif buzz:
            print("Buzz")
            # add to buzz total
            buzzcount = buzzcount +1
        else:
            print(i)

    print("")
    print('Num fizzed: ' + str(fizzcount))
    print('Num buzzed: ' + str(buzzcount))
    print('Num fizzbuzzed: '+ str(fizzbuzzcount))

    

 
if __name__ == '__main__':
    main()