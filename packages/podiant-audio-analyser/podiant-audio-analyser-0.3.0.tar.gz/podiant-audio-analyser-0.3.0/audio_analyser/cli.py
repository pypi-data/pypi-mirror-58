from datetime import datetime
from . import analyse as run
from .exceptions import AnalysisError, ConfigurationError
from .reporting import ConsoleReporter
import click
import logging


context_settings = dict(
    ignore_unknown_options=True,
    allow_extra_args=True
)


def configure_logging():
    logger = logging.getLogger('audio_analyser')
    logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(levelname)s - %(message)s')
    console.setFormatter(formatter)

    logger.addHandler(console)


@click.group()
@click.pass_context
def main(ctx):
    """Audio analysis toolkit"""


@main.command(context_settings=context_settings)
@click.pass_context
@click.argument('input', type=str)
@click.option('--debug', '-d', type=bool, default=False, is_flag=True)
def analyse(ctx, input, debug=False):
    """Analyse audio file"""

    if debug:
        configure_logging()

    started = datetime.now()
    reporter = ConsoleReporter()

    try:
        run(input, reporter=reporter)
    except (AnalysisError, ConfigurationError) as ex:
        click.echo(str(ex), err=True)
        click.exit(1)
        return

    finished = datetime.now()
    delta = (finished - started).total_seconds()

    if debug:
        logger = logging.getLogger('audio_analyser')
        logger.debug(
            'Process took %s second%s' % (
                delta,
                delta != 1 and 's' or ''
            )
        )
