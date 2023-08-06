#!/usr/bin/python

"""
ddx
"""
import os
import random
#import argparse
import subprocess

import click


@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
def new(name):
    """ Create project directory """
    BASE_DIR = os.path.join(os.getcwd(), name)
    subprocess.run(["git", "clone", "https://github.com/ChanMo/django_boilerplate.git", name])
    os.chdir(BASE_DIR)
    subprocess.run(["docker", "build", "--tag=django", "."])
    subprocess.run(["docker", "run", "--rm", "--mount", "type=bind,src={},target=/app".format(BASE_DIR), "django", "django-admin", "startproject", "api"])
    subprocess.run(["sudo", "chown", "chen:chen", ".", "-R"]) # need impro
    subprocess.run(["docker", "image", "rm", "django"])
    #subprocess.run(["cp", "local.example.py", "api/api/local.py"], cwd=name)
    subprocess.run(["cp", "local.sample.py", "api/api/local.py"])
    subprocess.run(["cp", "api-dockerfile", "api/Dockerfile"])
    subprocess.run(["cp", "requirements.txt", "api/requirements.txt"])

cli.add_command(new)

if __name__ == '__main__':
    cli()
