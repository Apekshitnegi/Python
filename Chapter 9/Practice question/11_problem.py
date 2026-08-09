with open(rf"C:\Users\Apekshit negi\OneDrive\Documents\Desktop\Python\Chapter 9\Practice question\old.txt") as f:
    content = f.read()

with open(rf"C:\Users\Apekshit negi\OneDrive\Documents\Desktop\Python\Chapter 9\Practice question\gold.txt", "w") as f:
    f.write(content)