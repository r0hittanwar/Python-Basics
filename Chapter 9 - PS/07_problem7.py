with open("log.txt", "r") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if("Python" in line):
        print(f"Yes Python is present.\nLine no: {lineNo}")
        break
    lineNo += 1

else:
    print("No Python is not present")
