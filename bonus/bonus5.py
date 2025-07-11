contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced", 
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    #../ means we go one level up in the directory. 
    #we go from bonus file to the root directory where the "files" is stored
    #good practice if you intend to write data into other files
    #thankfully its not needed due to vs code advancements 
    
    file = open(f"files/{filename}", "w")
    file.write(content)