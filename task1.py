filename = "sample.txt"
try:
    with open(filename, "rt") as fh:
        print("Reading file content:\n")
        lines = fh.readlines()
        index = 1
        for line in lines:
            print(f"Line {index}: {line}")
            index += 1

except FileNotFoundError:
    print(f"Error: The file {filename} was not found.")


