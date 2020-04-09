def my_decorator(func):
    def wrapper():
        print("Add something before the function is called.")
        func()
        print("Add something after the function is called.")
    return wrapper

@my_decorator
def my_func():
    print("Running function being wrapped")

def main():
    my_func()

if __name__ == '__main__':
    main()
