# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
# step 3: Use a loop to add two more members
for i in range(2):  # We want to add two members
    if i == 0:
        beatles.append("Stu Sutcliffe")
    elif i == 1:
        beatles.append("Pete Best")
print("Step 3:", beatles)

# step 4
del beatles[4]
del beatles[3]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
