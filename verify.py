import json

# Load original data
with open("original.json") as f:
    original = json.load(f)

# Load new data
with open("data.json") as f:
    new = json.load(f)

# Calculate average typing speed
orig_avg = sum(original) / len(original)
new_avg = sum(new) / len(new)

print("Original Avg:", orig_avg)
print("New Avg:", new_avg)

# Compare
if abs(orig_avg - new_avg) < 0.05:
    print("User Verified ✅")
else:
    print("Intruder Detected ❌")
