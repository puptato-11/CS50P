def main():
    text = input()
    convert(text)
def convert(str):
    emoji = str.replace(":)", "🙂").replace(":(","🙁")
    print(emoji)
main()
