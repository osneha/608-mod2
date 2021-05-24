import statistics

values = [47, 95, 88, 73, 88, 84]

count = len(values)

print("Count = ", count)
print("Sum = ",sum(values))

mean = statistics.mean(values)
print("Mean = ", mean )

median = statistics.median(values)
print("Median = ", median )

mode = statistics.mode(values)
print("Mode = ", mode )

