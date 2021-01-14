def createGen():
    mylist = range(5)
    for i in mylist:
        yield i * i
        mygenerator = createGen()
        print(mygenerator)
