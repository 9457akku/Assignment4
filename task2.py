output_file = "output.txt"

data = input("Enter text to write to the file: ")

with open(output_file,"at") as fh:
    fh.writelines(data)
    print(f"Data successfully written to {output_file}.")

add_text = input("Enter additional text to append: ")
with open(output_file,"at") as fh:
    fh.writelines(add_text)
    print(f"Data successfully appended.")

with open(output_file,"rt") as fh:
    content = fh.readlines()
    print(f"Final content of {output_file}:")
    for text in content:
        print(f"{text}\n")