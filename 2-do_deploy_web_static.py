#!/usr/bin/python3
"""Distribute an archive to web servers using Fabric."""

from fabric.api import env, put, run
from os.path import exists, splitext

env.hosts = ['18.235.255.120', '52.201.157.77']  # server IPs
env.user = 'ubuntu'  # SSH username
env.key_filename = '/root/my_ssh_private_key'


def do_deploy(archive_path):
    """Distribute an archive to web servers.

    Args:
        archive_path (str): The path to the archive to distribute.

    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    if not exists(archive_path):
        return False

    filename = archive_path.split('/')[-1]
    name = splitext(filename)[0]
    remote_path = '/tmp/{}'.format(filename)

    # Upload the archive to the /tmp/ directory of the web servers
    put(archive_path, remote_path)

    # Uncompress the archive to the specified folder
    run('sudo mkdir -p /data/web_static/releases/{}/'.format(name))
    run('sudo tar -xzf {} -C /data/web_static/releases/{}/'
        .format(remote_path, name))

    # Delete the archive from the web servers
    run('sudo rm {}'.format(remote_path))

    # Remove the symbolic link /data/web_static/current
    run('sudo rm -rf /data/web_static/current')

    # Create a new symbolic link to the new version
    run('sudo ln -s /data/web_static/releases/{}/ /data/web_static/current'
        .format(name))

    return True
