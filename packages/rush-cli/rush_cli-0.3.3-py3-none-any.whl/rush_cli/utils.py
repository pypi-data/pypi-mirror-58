import os
import subprocess
import sys

import click
import toml


def strip_spaces(st):
    return st.rstrip()


def split_lines(st):
    return st.split("\n")


def remove_comments(task_chunk: list) -> list:
    task_chunk = [task for task in task_chunk if not task.startswith("#")]
    return task_chunk


def find_shell_path(shell_name):
    """Finds out system's bash interpreter path"""

    if not os.name == "nt":
        cmd = ["which", "-a", shell_name]
    else:
        cmd = ["where", shell_name]

    try:
        c = subprocess.run(
            cmd, universal_newlines=True, check=True, capture_output=True
        )
        output = c.stdout.split("\n")
        output = [_ for _ in output if _]

        _shell_paths = [f"/bin/{shell_name}", f"/usr/bin/{shell_name}"]

        for path in output:
            if path == _shell_paths[0]:
                return path
            elif path == _shell_paths[1]:
                return path

    except subprocess.CalledProcessError:
        click.echo(
            click.style(
                "Error: Bash not found. Install Bash to use Rush.", fg="magenta"
            )
        )
        sys.exit(1)


def beautify_task_name(task_name):
    task_name = f"{task_name}:"
    underline_len = len(task_name) + 3
    underline = "=" * underline_len

    task_name = str(click.style(task_name, fg="yellow"))
    underline = str(click.style(underline, fg="green"))

    click.echo(task_name)
    click.echo(underline)


def beautify_skiptask_name(task_name):
    task_name = f"=> Ignoring task {task_name}"
    task_name = click.style(task_name, fg="blue")
    click.echo(task_name)
    click.echo("")


def beautify_cmd(cmd):
    if not cmd.startswith("#"):
        separator = "=>"
        cmd = str(click.style(cmd, fg="cyan"))
        separator = str(click.style(separator, fg="cyan"))
        click.echo(f"{separator} {cmd}")


def run_task(use_shell, command, interactive=True, catch_error=True):
    std_out = sys.stdout if interactive else subprocess.PIPE
    std_in = sys.stdin if interactive else subprocess.PIPE

    res = subprocess.run(
        [use_shell, "-c", command],
        stdout=std_out,
        stdin=std_in,
        stderr=std_out,
        universal_newlines=True,
        check=catch_error,
        capture_output=False,
    )
    click.echo("")


def check_version():
    file_path = "./pyproject.toml"
    try:
        with open(file_path) as file:
            toml_content = toml.load(file, _dict=dict)
            version = toml_content.get("tool").get("poetry").get("version")
        return version

    except FileNotFoundError:
        sys.exit(click.style("Error: pyproject.toml file not found.", fg="magenta"))
