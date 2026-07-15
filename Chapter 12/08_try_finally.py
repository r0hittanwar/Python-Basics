def main():
    try:
        a = int(input("Enter the number: "))
        print(a)
        return      # According to code, here function should return but finally will also be executed.  

    except Exception as e:
        print(e)
        return

    # finally:
    #     print("Hey, i am inside finally")

    print("Hey, i am inside finally")    #this statement will not run beacause of return

    

main()