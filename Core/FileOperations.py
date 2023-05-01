import os


class FileOperations:

    def find_file_under_folder_with_extension(self, folder_path, extension):
        result_files = []

        for root, dirs, files in os.walk(f"{folder_path}"):
            for file in files:
                if file.endswith(f'{extension}'):
                    result_files.append(os.path.join(root, file))

        if result_files:
            return result_files
