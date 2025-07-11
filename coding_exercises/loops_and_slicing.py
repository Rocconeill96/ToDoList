filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for filename in filenames:
    print(filename.split(".txt")[0])