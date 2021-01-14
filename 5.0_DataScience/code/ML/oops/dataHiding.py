class dataHiding:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1

    print(self.__secretCount)


counter = dataHiding()
counter.count()

print(counter.__secretCount)  # error

# print(counter._dataHiding__secretCount)
