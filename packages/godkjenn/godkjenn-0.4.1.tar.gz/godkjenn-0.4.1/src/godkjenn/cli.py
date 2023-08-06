import logging
import sys
from pathlib import Path

import click
from exit_codes import ExitCode

import godkjenn.config
import godkjenn.plugins
from godkjenn.version import __version__

log = logging.getLogger(__name__)


@click.group()
@click.option('--config', help='Config file to load', type=Path)
@click.option('--root-dir', help='Root directory', type=Path)
@click.option('--verbosity',
              default='WARNING',
              help="The logging level to use.",
              type=click.Choice([name
                                 for lvl, name in sorted(logging._levelToName.items())
                                 if lvl > 0],
                                case_sensitive=True))
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx, config, root_dir, verbosity):
    """Command-line interface for godkjenn.
    """
    logging_level = getattr(logging, verbosity)
    logging.basicConfig(level=logging_level)

    if config is not None:
        config = godkjenn.config.load_config(config)
    else:
        config = godkjenn.config.default_config(root_dir)

    ctx.obj = {'config': config}


@cli.command()
@click.argument('test_id')
@click.pass_obj
def accept(ctx_obj, test_id):
    """Accept the current received data for a test.
    """
    vault = godkjenn.plugins.get_vault(ctx_obj['config'])

    try:
        vault.accept(test_id)
    except KeyError:
        log.error('No received data for {}'.format(test_id))
        return ExitCode.DATA_ERR

    return ExitCode.OK


@cli.command()
@click.pass_obj
def accept_all(ctx_obj):
    """Accept all received data for a configuration/root directory.
    """
    vault = godkjenn.plugins.get_vault(ctx_obj['config'])

    for test_id in vault.ids():
        try:
            vault.accept(test_id)
        except KeyError:
            # This just means there isn't any received data for the ID, just accepted.
            pass

    return ExitCode.OK


@cli.command()
@click.argument('test_id')
@click.argument('data_source', type=click.File(mode='rb'))
@click.pass_obj
def receive(ctx_obj, test_id, data_source):
    """Receive new data for a test.
    """
    vault = godkjenn.plugins.get_vault(ctx_obj['config'])

    data = data_source.read()
    vault.receive(test_id, data)

    return ExitCode.OK


def main(argv=None, standalone_mode=True):
    return cli(argv, standalone_mode=standalone_mode)


if __name__ == '__main__':
    sys.exit(main())
