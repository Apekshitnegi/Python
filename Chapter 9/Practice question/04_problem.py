word = "Dockey" 

with open(rf"C:\Users\Apekshit negi\OneDrive\Documents\Desktop\Python\Chapter 9\Practice question\text.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "####")

with open(rf"C:\Users\Apekshit negi\OneDrive\Documents\Desktop\Python\Chapter 9\Practice question\text.txt", "w") as f:
    f.write(contentNew)