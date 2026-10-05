with open("donkey_file.txt", "r+") as f:
    con = f.read()
    cuss_words = ["donkey", "seal"]
    if any(word in con for word in cuss_words):
        replaced_con = con.replace("donkey", "#####").replace("seal", "####")
        f.seek(0)
        f.write(replaced_con)
        f.truncate()
    else:
        print("No donkey or seal word found.")