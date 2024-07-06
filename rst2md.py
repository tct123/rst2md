import pypandoc
from pypandoc.pandoc_download import download_pandoc

download_pandoc()
input_file = 'README.txt'
output_file = 'README.md'

output = pypandoc.convert_file(input_file, 'md', format='rst')
with open(output_file, 'w') as f:
    f.write(output)
