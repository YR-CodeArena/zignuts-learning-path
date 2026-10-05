with open("table_of_2_to_20.txt", "w") as f:
    for i in range(2, 21):
        for n in range(1, 11):
            fu = ""
            st = ""
            r = n * i
            fu = f"{i} x {n} = {r}"
            st += fu    
            f.write(st + "\n")
        f.write("\n")