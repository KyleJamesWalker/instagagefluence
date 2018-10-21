import argparse
import hashlib
import os
import pickle
import time
import yamlsettings

from InstagramAPI import InstagramAPI


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

    user_data_file = '{}{}.data'.format(
        settings.data_prefix,
        hashlib.md5(settings.username.encode('utf-8')).hexdigest()
    )

    if os.path.isfile(user_data_file):
        print("Using existing data")
        ig = pickle.load(open(user_data_file, 'rb'))
    else:
        print("Creating new login")
        ig = InstagramAPI(settings.username, settings.password)
        ig.login()

    # Make sure I don't hit the API to much
    time.sleep(2)

    ig.getProfileData()
    print(ig.LastJson)
    pickle.dump(ig, open(user_data_file, 'wb'))
