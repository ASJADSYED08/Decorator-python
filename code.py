def dec1(func1):
    def nowexec():
        print("NOW EXECUTING")
        func1()
        print("executed")
    return nowexec
@dec1
def who():
    print("ASJAD")
# who=dec1(who)
who()            