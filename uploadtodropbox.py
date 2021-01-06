#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 19:00:47 2021

@author: sadist
"""

import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
import datetime

dt = datetime.datetime.today()
TOKEN = "<token>"
LOCALFILE ="<locationtouploadfrom.fileformat>"
# Don't forget to add the file extension at the end of BACKUPPATH.
BACKUPPATH = f"/<locationtoupload.fileformat>"


def backup(localFile, backupPath):
    with open(localFile, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        print("Uploading " + localFile + " to Dropbox as " + backupPath + "...")
        try:
            dbx.files_upload(f.read(), backupPath, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have
            # enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()


if __name__ == '__main__':
    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError:
        sys.exit("ERROR: Invalid access token; try re-generating an "
                 "access token from the app console on the web.")

    # Create a backup of the current settings file
    backup(LOCALFILE, BACKUPPATH)

    print("Done!")
