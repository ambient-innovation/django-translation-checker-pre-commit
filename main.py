import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filenames", nargs="*")
    parser.add_argument("--noodle", nargs="*")
    args = parser.parse_args()

    print(args.noodle)


if __name__ == "__main__":
    main()
