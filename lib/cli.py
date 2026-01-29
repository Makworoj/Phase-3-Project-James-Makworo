import click
from sqlalchemy import func

from db.session import session
from db.models import Member, Skill, Job


# ---------------- CLICK COMMANDS (LOGIC LAYER) ----------------

@click.group()
def cli():
    """SkillTrack CLI"""
    pass


@cli.command()
@click.argument("name")
@click.argument("location")
def add_member(name, location):
    member = Member(name=name, location=location)
    session.add(member)
    session.commit()
    print(f"✅ Member '{name}' added successfully.")
    print(f"👉 Member ID: {member.id}")


@cli.command()
def list_members():
    members = session.query(Member).all()
    if not members:
        print("No members found.")
        return

    for member in members:
        print(f"{member.id} | {member.name} | {member.location}")


@cli.command()
@click.argument("member_id", type=int)
@click.argument("skill_name")
def add_skill(member_id, skill_name):
    member = session.get(Member, member_id)
    if not member:
        print("❌ Error: Member not found.")
        return

    skill = Skill(name=skill_name, member=member)
    session.add(skill)
    session.commit()
    print(f"✅ Skill '{skill_name}' added to {member.name}.")


@cli.command()
@click.argument("member_id", type=int)
def list_skills(member_id):
    member = session.get(Member, member_id)

    if not member:
        print("❌ Error: Member not found.")
        return

    if not member.skills:
        print(f"{member.name} has no skills recorded.")
        return

    print(f"Skills for {member.name}:")
    for skill in member.skills:
        print(f"- {skill.name}")


@cli.command()
@click.argument("member_id", type=int)
@click.argument("description")
@click.argument("amount", type=float)
def add_job(member_id, description, amount):
    member = session.get(Member, member_id)
    if not member:
        print("❌ Error: Member not found.")
        return

    job = Job(description=description, amount=amount, member=member)
    session.add(job)
    session.commit()
    print(f"💰 Job '{description}' recorded for {member.name}: KES {amount}")


@cli.command()
def earnings():
    results = (
        session.query(
            Member.name,
            func.sum(Job.amount)
        )
        .join(Job)
        .group_by(Member.id)
        .all()
    )

    if not results:
        print("No earnings recorded yet.")
        return

    for name, total in results:
        print(f"{name}: KES {total}")


# ---------------- MENU + LOOP (INTERACTION LAYER) ----------------

def menu():
    while True:
        print("\n===== SkillTrack CLI =====")
        print("1. Add Member")
        print("2. List Members")
        print("3. Add Skill")
        print("4. Add Job")
        print("5. View Earnings")
        print("6. View Member Skills")
        print("0. Exit")

        choice = input("Select an option: ").strip()

        # ---------- ADD MEMBER ----------
        if choice == "1":
            name = input("Enter member name: ").strip()
            location = input("Enter member location: ").strip()

            if not name.isalpha():
                print("❌ Error: Name must contain letters only.")
                continue

            if not location.isalpha():
                print("❌ Error: Location must contain letters only.")
                continue

            add_member.callback(name, location)

        # ---------- LIST MEMBERS ----------
        elif choice == "2":
            list_members.callback()

        # ---------- ADD SKILL ----------
        elif choice == "3":
            try:
                member_id = int(input("Enter member ID: "))
            except ValueError:
                print("❌ Error: Member ID must be a number.")
                continue

            skill_name = input("Enter skill name: ").strip()

            if not skill_name.isalpha():
                print("❌ Error: Skill name must contain letters only.")
                continue

            add_skill.callback(member_id, skill_name)

        # ---------- ADD JOB ----------
        elif choice == "4":
            try:
                member_id = int(input("Enter member ID: "))
            except ValueError:
                print("❌ Error: Member ID must be a number.")
                continue

            description = input("Enter job description: ").strip()
            if not description:
                print("❌ Error: Job description cannot be empty.")
                continue

            try:
                amount = float(input("Enter amount earned: "))
            except ValueError:
                print("❌ Error: Amount must be a number.")
                continue

            if amount <= 0:
                print("❌ Error: Amount must be greater than zero.")
                continue

            add_job.callback(member_id, description, amount)

        # ---------- EARNINGS ----------
        elif choice == "5":
            earnings.callback()

        # ---------- LIST SKILLS ----------
        elif choice == "6":
            try:
                member_id = int(input("Enter member ID: "))
            except ValueError:
                print("❌ Error: Member ID must be a number.")
                continue

            list_skills.callback(member_id)

        # ---------- EXIT ----------
        elif choice == "0":
            print("👋 Exiting SkillTrack. Goodbye!")
            break

        # ---------- INVALID OPTION ----------
        else:
            print("❌ Error: Invalid option. Please select a valid menu number.")


# ---------------- ENTRY POINT ----------------

if __name__ == "__main__":
    menu()
