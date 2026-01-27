import click
from db.session import session
from db.models import Member

@click.group()
def cli():
    """SkillTrack CLI"""
    pass


@cli.command()
@click.argument("name")
@click.argument("location")
def add_member(name, location):
    """Add a community member"""
    member = Member(name=name, location=location)
    session.add(member)
    session.commit()
    click.echo(f"✅ Member '{name}' added successfully.")


if __name__ == "__main__":
    cli()
