with open(rf"C:\Users\Apekshit negi\OneDrive\Documents\Desktop\Python\Chapter 9\Practice question\this.txt", "r") as f:
    content = f.read()

with open(rf"C:\Users\Apekshit negi\OneDrive\Documents\Desktop\Python\Chapter 9\Practice question\this_copy.txt", "w") as f:
    f.write(content)