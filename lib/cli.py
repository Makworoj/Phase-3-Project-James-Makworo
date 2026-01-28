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
@cli.command()
def list_members():
    """List all community members"""
    members = session.query(Member).all()

    if not members:
        click.echo("No members found.")
        return

    for member in members:
        click.echo(f"{member.id} | {member.name} | {member.location}")




if __name__ == "__main__":
    cli()
