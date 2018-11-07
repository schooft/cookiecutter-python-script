"""
    A skeleton python script
"""
import sys
import argparse


def greeting(name, lang='en'):
    if lang == "en":
        return "Hello, {}!".format(name)
    elif lang == "de":
        return "Hallo, {}!".format(name)
    else:
        raise ValueError("Unknown language: {}".format(lang))


def parse_args(argv):
    parser = argparse.ArgumentParser(description='Personal greeter.')
    parser.add_argument('name', type=str, help='your name')
    parser.add_argument('--language', '-l', type=str, default='en',
                        help='the language')

    return parser.parse_args(argv)


def main(argv=sys.argv[1:]):
    args = parse_args(argv)
    print(greeting(args.name, args.language))
    return 0


if __name__ == "__main__":
    sys.exit(main())
