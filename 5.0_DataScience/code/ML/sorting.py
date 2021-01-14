x = [4,1,2,3]
y = sorted(x)
x.sort()

x = sorted([-4,1,-2,3], key=abs, reverse=True)

wc = sorted(word_counts.items(),key=lambda (word, count): count,reverse=True)


