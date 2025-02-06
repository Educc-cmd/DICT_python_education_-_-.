class MarkdownFormatter:
    def __init__(self):
        self.output_text = ""
        self.available_formatters = {
            "plain", "bold", "italic", "header", "link",
            "inline-code", "ordered-list", "unordered-list", "new-line"
        }

    def print_help(self):
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")

    def get_header(self):
        while True:
            try:
                level = int(input("Level: "))
                if 1 <= level <= 6:
                    break
                print("The level should be within the range of 1 to 6.")
            except ValueError:
                print("The level should be a number.")
        text = input("Text: ")
        return f"{'#' * level} {text}\n"

    def get_list(self, ordered):
        while True:
            try:
                num_rows = int(input("Number of rows: "))
                if num_rows > 0:
                    break
                print("The number of rows should be greater than zero.")
            except ValueError:
                print("The number of rows should be a number.")
        
        list_items = []
        for i in range(num_rows):
            row_text = input(f"Row #{i + 1}: ")
            list_items.append(f"{i + 1}. {row_text}" if ordered else f"* {row_text}")
        
        return "\n" + "\n".join(list_items) + "\n\n"

    def format_text(self, formatter, text=None):
        if formatter == "plain":
            return text
        if formatter == "bold":
            return f"**{text}**"
        if formatter == "italic":
            return f"*{text}*"
        if formatter == "inline-code":
            return f"`{text}`"
        if formatter == "header":
            return self.get_header()
        if formatter == "link":
            label = input("Label: ")
            url = input("URL: ")
            return f"[{label}]({url})"
        if formatter == "new-line":
            return "\n\n"
        if formatter in ["ordered-list", "unordered-list"]:
            return self.get_list(formatter == "ordered-list")
        return ""

    def run(self):
        while True:
            user_input = input("Choose a formatter: ")
            if user_input == "!help":
                self.print_help()
            elif user_input == "!done":
                with open("output.md", "w", encoding="utf-8") as file:
                    file.write(self.output_text.strip())
                print(self.output_text)
                break
            elif user_input in self.available_formatters:
                if user_input in ["new-line", "ordered-list", "unordered-list", "header", "link"]:
                    self.output_text += self.format_text(user_input)
                else:
                    text = input("Text: ")
                    self.output_text += self.format_text(user_input, text) + " "
                print(self.output_text.strip())
            else:
                print("Unknown formatting type or command")


if __name__ == "__main__":
    MarkdownFormatter().run()
