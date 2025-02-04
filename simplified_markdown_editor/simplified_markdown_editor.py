def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")


def format_text(formatter, text=None):
    if formatter == "plain":
        return text
    elif formatter == "bold":
        return f"**{text}**"
    elif formatter == "italic":
        return f"*{text}*"
    elif formatter == "inline-code":
        return f"`{text}`"
    elif formatter == "header":
        level = int(input("Level: "))
        if 1 <= level <= 6:
            text = input("Text: ")
            return f"{'#' * level} {text}\n"
        else:
            print("The level should be within the range of 1 to 6.")
            return ""
    elif formatter == "link":
        label = input("Label: ")
        url = input("URL: ")
        return f"[{label}]({url})"
    elif formatter == "new-line":
        return "\n"
    elif formatter in ["ordered-list", "unordered-list"]:
        num_rows = int(input("Number of rows: "))
        if num_rows <= 0:
            print("The number of rows should be greater than zero.")
            return ""
        list_items = []
        for i in range(1, num_rows + 1):
            item = input(f"Row #{i}: ")
            prefix = f"{i}. " if formatter == "ordered-list" else "* "
            list_items.append(f"{prefix}{item}")
        return "\n".join(list_items) + "\n"
    return ""


available_formatters = {
    "plain", "bold", "italic", "header", "link",
    "inline-code", "ordered-list", "unordered-list", "new-line"
}

output_text = ""

while True:
    user_input = input("Choose a formatter: ")

    if user_input == "!help":
        print_help()
    elif user_input == "!done":
        with open("output.md", "w", encoding="utf-8") as file:
            file.write(output_text.strip())
        print(output_text)
        break
    elif user_input in available_formatters:
        if user_input in ["new-line", "ordered-list", "unordered-list"]:
            output_text += format_text(user_input)
        else:
            text = input("Text: ")
            output_text += format_text(user_input, text) + " "
        print(output_text.strip())
    else:
        print("Unknown formatting type or command")
