def announce(f):
    def wapper():
        print("About to run the function...........")
        f()
        print("Done with the function!")
    return wapper

@announce
def hello():
    print("Hello, world!")

hello()