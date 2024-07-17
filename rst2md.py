import pypandoc


def rst2md(input_file, output_file):
    output = pypandoc.convert_file(input_file, "md", format="rst")
    with open(output_file, "w") as f:
        f.write(output)


if __name__ == "__main__":
    input_file = input("Path to README.rst: ")
    output_file = input("Path to README.md: ")
    rst2md(input_file=input_file, output_file=output_file)
