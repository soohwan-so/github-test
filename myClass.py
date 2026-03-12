class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def write_file(self, content):
        try:
            with open(self.file_path, 'w') as file:
                file.write(content)
            return "File written successfully."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def append_file(self, content):
        try:
            with open(self.file_path, 'a') as file:
                file.write(content)
            return "Content appended successfully."
        except Exception as e:
            return f"An error occurred: {str(e)}"
        
    def delete_file(self):
        import os
        try:
            os.remove(self.file_path)
            return "File deleted successfully."
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return f"An error occurred: {str(e)}"
        