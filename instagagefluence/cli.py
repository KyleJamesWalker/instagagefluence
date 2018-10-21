import argparse
import yamlsettings


def main():
    parser = argparse.ArgumentParser(
        description=" Instagram Engagement Influencer Bot",
    )
    parser.add_argument(
        "config",
        help="Configuration",
        nargs='?',
        default="igf.yaml",
    )
    args = parser.parse_args()

    settings = yamlsettings.load('igf://{}'.format(args.config))
    print(settings)
