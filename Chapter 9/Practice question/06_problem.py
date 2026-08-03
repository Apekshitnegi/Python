with  open(rf"C:\Users\Apekshit negi\OneDrive\Documents\Desktop\Python\Chapter 9\Practice question\log.txt", "r") as f:
    content = f.read()

if("python" in content):
    print("yes python is present")
else :
    print("no python present")