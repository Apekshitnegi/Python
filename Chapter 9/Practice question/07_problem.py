with  open(rf"C:\Users\Apekshit negi\OneDrive\Documents\Desktop\Python\Chapter 9\Practice question\log.txt", "r") as f:
    lines = f.readlines()

lineno = 1

for line in lines:
    if("python" in line):
        print(f"yes python present in lineno: {lineno}")
        break
    lineno += 1

else:
    ("no python present") 