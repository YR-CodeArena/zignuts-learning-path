
try:
    with ( 
        
        open('text1.txt', 'r') as f,
        
        
        open('text2.txt', 'w') as g,
        open('text3.txt', 'a') as h
    ):
        data = f.read()
        g.write(data)
        h.write("Log: File 1's content copied to file 2.")
except:
    print("First make the text file called: text1.txt")

