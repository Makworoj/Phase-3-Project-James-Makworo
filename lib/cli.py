import click
from db.session import session
from db.models import Member, Skill, Job


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
    click.echo(f"👉 Your Member ID is: {member.id}")
    click.echo(f'👉 Add a skill using: add-skill {member.id} "<skill name>"')


@cli.command()
def list_members():
    """List all community members"""
    members = session.query(Member).all()

    if not members:
        click.echo("No members found.")
        return

    for member in members:
        click.echo(f"{member.id} | {member.name} | {member.location}")


@cli.command()
@click.argument("member_id", type=int)
@click.argument("skill_name")
def add_skill(member_id, skill_name):
    """Add a skill to a community member"""
    member = session.get(Member, member_id)

    if not member:
        click.echo("❌ Member not found.")
        return

    skill = Skill(name=skill_name, member=member)
    session.add(skill)
    session.commit()

    click.echo(f"✅ Skill '{skill_name}' added to {member.name}.")


@cli.command()
@click.argument("member_id", type=int)
@click.argument("description")
@click.argument("amount", type=float)
def add_job(member_id, description, amount):
    """Record a completed job and payment"""
    member = session.get(Member, member_id)

    if not member:
        click.echo("❌ Member not found.")
        return

    job = Job(description=description, amount=amount, member=member)
    session.add(job)
    session.commit()

    click.echo(f"💰 Job '{description}' recorded for {member.name}: KES {amount}")


if __name__ == "__main__":
    cli()
