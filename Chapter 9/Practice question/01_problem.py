f = open(r"c:\Users\Apekshit negi\OneDrive\Documents\Desktop\Python\Chapter 9\Practice question\poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content")

f.close()