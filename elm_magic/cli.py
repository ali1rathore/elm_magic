# -*- coding: utf-8 -*-

"""Console script for elm_magic."""

import click
import subprocess
import os

def run_shell(cmd):
    return subprocess.check_output(cmd,shell=True)

@click.group()
def main(args=None):
    """Console script for elm_magic."""

@main.command()
@click.option('--target', type=click.Path(exists=True)
             ,default="/usr/local",show_default=True
             ,help="Location where npm and node will be installed (<target>/bin/npm and <target>/bin/node)")
def install(target):
    """Install nodejs and elm-lang compiler dependancies.
       The <target>/bin directory should already be in your PATH
    """
    if not os.path.isdir(target):
        click.echo("Install target directory {} does not appear to be a directory".format(target))
        click.echo("  Please create it or use a different install directory")
        return

    click.echo("Installing npm and node at {}".format(target)) 
    run_shell("wget -qO- https://nodejs.org/dist/v4.4.4/node-v4.4.4-linux-x64.tar.xz | tar xJv -C {target} --strip-components=1".format(target=target))
    click.echo("Installing elm-lang")
    run_shell("npm install -g elm")
    run_shell("npm install -g elm-static-html")

@main.command()
def version():
    click.echo("ElmMagic version 0.1")

if __name__ == "__main__":
    main()
