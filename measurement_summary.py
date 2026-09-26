measurements = [18, 21, 24, 19]
review_threshold_text = "20"

# Convert the threshold text to an integer so it can be compared with numbers.
review_threshold = int(review_threshold_text)

# Running totals start at zero before the loop.
total = 0
review_count = 0

for measurement in measurements:
    total = total + measurement
    if measurement >= review_threshold:
        label = "review"
        review_count = review_count + 1
    else:
        label = "within range"
    print("Measurement:", measurement, label)

# Mean uses the actual list length, not a hard-coded 4.
count = len(measurements)
mean = total / count

print("Count:", count)
print("Total:", total)
print("Mean:", mean)
print("Review count:", review_count)