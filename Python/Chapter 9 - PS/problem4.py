with open("donkey_file.txt", "r+") as f:
    con = f.read()
    if "donkey" in con:
        replaced_con = con.replace("donkey", "#####")
        f.seek(0)
        f.write(replaced_con)
        f.truncate()
    else:
        print("No donkey word found.")