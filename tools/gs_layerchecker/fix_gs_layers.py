import click
import logging
import sys
from geoserver.catalog import Catalog

log = logging.getLogger(__name__)
stdout_hdlr = logging.StreamHandler(sys.stdout)
stdout_hdlr.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
stdout_hdlr.setLevel(logging.INFO)
log.addHandler(stdout_hdlr)
log.setLevel(logging.INFO)
cat = Catalog('https://geodata.alquds.info/geoserver/rest/', username='admin', password="<ENTER_PASSWORD_HERE>")


def fix_slds():
    """Process all layers in the catalog and make sure there are no null styles"""
    layers = cat.get_layers()
    for layer in layers:
        log.info("Processing layer "+layer.name)
        generic = cat.get_style('generic')
        if layer:
            log.debug("Adding style to  layer "+layer.name)

            if not layer.default_style:

                log.debug("setting genric default style: ")
                layer.default_style = generic
            styles = list(layer.styles)
            if styles:
                log.debug([style.name for style in styles])
                styles = [style if style is not None else generic for style in styles]

            else:
                styles = [generic]

            layer.styles = styles
            cat.save(layer)


@click.group()
@click.option('--debug', is_flag=True)
def cli(debug):
    if debug:
        stdout_hdlr.setLevel(logging.DEBUG)
        log.setLevel(logging.DEBUG)


@cli.command()
def fixer():
    fix_slds()


if __name__ == '__main__':
    cli()
