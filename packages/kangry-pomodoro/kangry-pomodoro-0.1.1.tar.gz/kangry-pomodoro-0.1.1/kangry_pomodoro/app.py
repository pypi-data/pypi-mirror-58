#! /usr/bin/env python3

import click
from kangry_pomodoro.trayicon import launch_app


@click.group()
def main():
    """pomodoro cli"""
    pass


@main.command()
@click.option('--work_time', '-w', type=int, default=25, help='Working interval in minutes.')
@click.option('--short_break', '-s', default=5, help='Short break interval in minutes.')
@click.option('--long_break', '-l', default=30, help='Long break interval in minutes.')
def start(work_time, short_break, long_break):
    """
   Start the timer.
   """
    launch_app(work_time=work_time, short_break=short_break, long_break=long_break)


if __name__ == "__main__":
    main()
