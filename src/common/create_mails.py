import logging

logging.getLogger().setLevel(logging.DEBUG)

from . import config


def _create_mails(argA, argB):
    return {
        "argA": argA,
        "argB": argB,
    }


def main():
    import argparse

    script_parser = argparse.ArgumentParser(
        prog="create_mails",
        description="create_mails script",
    )

    script_parser.add_argument(
        "-a",
        "--argA",
        action="store",
        metavar="arg1",
        help="create_mails argA",
        required=True,
    )

    script_parser.add_argument(
        "-b",
        "--argB",
        action="store",
        metavar="color",
        help="create_mails color",
        required=True,
    )

    result = _create_mails(**vars(script_parser.parse_args()))

    # Example how to access config toml file
    logging.debug(config)

    # Using **vars() to convert Namespace to dict
    logging.debug(result)

    return result


if __name__ == "__main__":
    main()
