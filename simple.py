s1= "my name is pravin"
t1=s1.split()
print(t1)
result = ' '.join([word[::-1] for word in s1.split()])
print(result)