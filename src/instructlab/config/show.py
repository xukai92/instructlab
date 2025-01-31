# SPDX-License-Identifier: Apache-2.0
# Third Party
import click
import yaml

# First Party
from instructlab import utils


@click.command()
@click.pass_context
@utils.display_params
def show(
    ctx,
):
    """Displays the current config as YAML"""
    # TODO: make this use pretty colors like jq/yq
    try:
        config_yaml = yaml.load(
            ctx.obj.config.model_dump_json(), Loader=yaml.FullLoader
        )
    except yaml.YAMLError as e:
        click.secho(f"Error loading config as YAML: {e}", fg="red")
    click.echo(yaml.dump(config_yaml, indent=4))
