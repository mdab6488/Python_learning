def hello(name, lang):
    greetings = {
        "en": "Hello",
        "es": "Hola",
        "fr": "Bonjour",
        "de": "Hallo",
        "it": "Ciao",
        "pt": "Olá",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personal greeting.")

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person to greet.",
    )

    parser.add_argument(
        "-l",
        "--lang",
        metavar="language",
        required=True,
        choices=["en", "es", "fr", "de", "it", "pt"],
        default="en",
        help="The language of the greeting (default: 'en').",
    )

    args = parser.parse_args()

    hello(args.name, args.lang)
