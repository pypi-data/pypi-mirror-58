#!/usr/bin/env python
"""
Module load handler for execution via:

python -m prawn
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys

import click

from .stream import process_stream

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

__version__ = "0.1"


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.version_option(version=__version__)
@click.pass_context
def main(ctxt):
    """
    Main click group handler
    """
    if ctxt.invoked_subcommand is None:
        run_invocation()


@main.command()
def invoke():
    """
    Primary command handler
    """
    run_invocation()


def run_invocation():
    """
    Execute the invocation
    """
    process_stream(sys.stdin, sys.stdout)


def get_basedir():
    """
    Locate the current directory of this file
    """
    return os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
# vim: set ft=python:
