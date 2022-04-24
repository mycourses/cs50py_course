# CS50 Python 2022
# Problem Set 0 - Making Faces
# v1.0


def convert(user_input):
    converted = user_input.replace(":)", "🙂").replace(":(", "🙁")
    return converted


def main():
    user_prompt = "Go on, give us a smile! "
    response = input(user_prompt)
    print(convert(response))


main()

