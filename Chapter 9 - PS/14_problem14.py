# with open("log.txt") as f:
    # lines = f.readlines()
# lineNo = 1
# for line in lines:
#     if("Python" in line):
#         print(f"Word found. Line no: {lineNo}")
#         break
#     lineNo += 1
# else:
#     print("Word not found")

def check_for_line():
    lineNo = 1
    with open("log.txt") as f:
        lines = f.readlines()
    
    for line in lines:
        if("Python" in line):
            print(f"Word found. Line no: {lineNo}")
            break
        lineNo += 1
    else:
        print("Word not found")

check_for_line()