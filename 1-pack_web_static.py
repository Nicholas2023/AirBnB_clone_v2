#!/usr/bin/python3
"""
A fabric script that generates .tgz archive
"""

# Import necessary modules and decorators
from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once


@runs_once  # Ensure that the function runs only once
def do_pack():

    """
    Generates .tgz archive from the contents of web_static folder
    """
    # Create the "versions" directory if it doesn't exist
    local("mkdir -p versions")

    # Construct the archive filename based on the current timestamp
    path = ("versions/web_static_{}.tgz"

            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    """
    Run the 'tar' command to compress the "web_static" directory
    into the archive
    """
    result = local("tar -cvzf {} web_static"

                   .format(path))

    # Check if the 'tar' command execution failed
    if result.failed:
        return None  # Return None if there was an error
    return path  # Return the path to the generated archive if successful
