import os

def concatenate_files_with_extension(directory, extension, output_file):
    with open(output_file, 'w') as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as infile:
                        content = infile.read()
                        # Write the file name before the content
                        outfile.write(f"--- Start of {file} ---\\n")
                        outfile.write(content + "\\n")
                        outfile.write(f"--- End of {file} ---\\n\\n")

# Example usage
directory = 'your/path'
extension = '.extension'
output_file = 'path/to/file.txt'

concatenate_files_with_extension(directory, extension, output_file)
