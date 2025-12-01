import re
import urllib.request

class MyFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def read(self):
        if self.mode != "read":
            print("File is not open for reading")
            return ""

        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File {self.filename} not found")
            return ""
        except Exception as e:
            print(f"Error in reading: {e}")
            return ""

    def write(self, text):
        if self.mode not in ["write", "append"]:
            print("File is not open for writing")
            return

        try:
            if self.mode == "write":
                with open(self.filename, 'w', encoding='utf-8') as file:
                    file.write(text)
            else:
                with open(self.filename, 'a', encoding='utf-8') as file:
                    file.write(text)
            print("File written")
        except Exception as e:
            print(f"Error in writing: {e}")

    def read_url(self):
        if self.mode != "url":
            print("This is not URL mode")
            return ""

        try:
            with urllib.request.urlopen(self.filename) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            print(f"Error in reading URL: {e}")
            return ""

    def count_urls(self):
        if self.mode != "url":
            print("This is not URL mode")
            return 0

        html_content = self.read_url()
        urls = re.findall(r'href=[\'"]?([^\'" >]+)', html_content)
        return len(urls)

    def write_url(self, output_filename):
        if self.mode != "url":
            print("This is not URL mode")
            return

        content = self.read_url()
        if content:
            try:
                with open(output_filename, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"URL content is saved in {output_filename}")
            except Exception as e:
                print(f"Error in saving: {e}")


if __name__ == "__main__":

    #Чтение
    file = MyFile("text.txt", "read")
    text = file.read()
    print(text)

    #Запись
    file = MyFile("text.txt", "write")
    file.write("Hello World")

    #Добавление
    file = MyFile("text.txt", "append")
    file.write("another text")

    #URL
    file = MyFile("https://example.url.com", "url")
    text = file.read_url()
    print(text)

    #Подсчет URL
    count = file.count_urls()
    print(f"Found {count} URLs")

    #Сохранение содержимого URL в файл
    file.write_url("text.txt")