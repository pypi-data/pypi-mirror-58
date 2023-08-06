import re

import click

from seki.commands.shared import commit_changes, prepare_project
from seki.conf import DRONE_PATH


@click.command("template", short_help="Generate drone from template.")
@click.argument("file", type=click.Path(exists=True))
@click.option("--cron", help="Cron expression.")
def _template(file, cron):
    prepare_project(cron)

    params = get_template_params(file)

    replacements = get_params_values(params)

    process_template(file, DRONE_PATH, replacements)

    commit_changes()


def get_template_params(template_path):
    with open(template_path, "r") as template_file:
        first_line = template_file.readline()

        if "# PARAMETERS:" in first_line:
            first_line = first_line.replace("# PARAMETERS:", "")
            return [param.strip() for param in first_line.split(",")]
        else:
            return []


def get_params_values(params):
    replacements = {}

    for param in params:
        key = "$$" + param.upper()
        replacements[key] = input(f"Value for '{param}': ")

    return replacements


def do_replacements_on(text, replacements):
    pattern = re.compile("|".join(re.escape(k) for k in replacements))

    return pattern.sub(lambda match: replacements[match.group(0)], text)


def process_template(template_path, output_path, replacements):
    click.echo(f"Generating 'drone.yml' from '{template_path}'...")

    with open(template_path, "r") as template_file, open(output_path, "w") as output_file:
        for line in template_file:
            if replacements:
                line = do_replacements_on(line, replacements)
            output_file.write(line)
