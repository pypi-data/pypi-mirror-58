"""Console script for confluent_kafka_connect_cli."""
import confluent_kafka_connect_cli.call as call
import click
import json

@click.group()
@click.option("--host", help="The kafka connector host.", default="localhost")
@click.option("--port", help="The kafka connector port.", default="8083")
@click.pass_context
def connector(ctx, host, port):
    ctx.obj['baseurl'] = 'http://{host}:{port}'.format(host=host, port=port)


@connector.command()
@click.pass_context
def status(ctx):
    print(json.dumps(call.status(ctx.obj['baseurl']), indent=4))


@connector.command()
@click.pass_context
def config(ctx):
    print(json.dumps(call.config(ctx.obj['baseurl']), indent=4))


@connector.command()
@click.option("--config", help="The kafka connector config file.")
@click.pass_context
def create(ctx, config):
    print(json.dumps(call.create(ctx.obj['baseurl'], config), indent=4))


@connector.command()
@click.pass_context
def delete(ctx):
    print(json.dumps(call.delete(ctx.obj['baseurl']), indent=4))


@connector.command()
@click.pass_context
def restart(ctx):
    print(json.dumps(call.restart(ctx.obj['baseurl']), indent=4))


@connector.command()
@click.pass_context
def restart_tasks(ctx):
    print(json.dumps(call.restart_tasks(ctx.obj['baseurl']), indent=4))


@connector.command()
@click.pass_context
def pause(ctx):
    print(json.dumps(call.pause(ctx.obj['baseurl']), indent=4))


@connector.command()
@click.pass_context
def resume(ctx):
    print(json.dumps(call.resume(ctx.obj['baseurl']), indent=4))


def main():
    return connector(obj={})


if __name__ == '__main__':
    connector(obj={})
