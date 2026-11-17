def main():
    # Remove pass with your answer.
    while True:
        try:
            x = int(input("Type an integer:"))
        except ValueError:
            print("Please enter an interger")    
    print("is not divisible by 10 or divisible by 3")
    print("is divisible by 10 and not divisible by 3")


if __name__ == "__main__":
    # execute only if run as a script
    main()
