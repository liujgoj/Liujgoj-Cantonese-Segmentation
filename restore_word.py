with open("1.txt", "r", encoding="utf-8") as file1, open("2.txt", "w", encoding="utf-8") as file2:
    for line in file1:
        # Step 1: replace "hor' mxhoryiq" with "horyiq mxhoryiq"
        line = line.replace("hor' mxhoryiq", "horyiq mxhoryiq")
        
        # Step 2: replace "hor' mxhornangx" with "hornangx mxhornangx"
        line = line.replace("hor' mxhornangx", "hornangx mxhornangx")
        
        # Step 3: replace "'deih" with "keoiqdeih"
        line = line.replace("'deih", "keoiqdeih")
        
        # Write the modified line to file2
        file2.write(line)