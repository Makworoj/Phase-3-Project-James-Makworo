from sqlalchemy import func
from db.session import session
from db.models import Member, Skill, Job


# ---------------- MEMBER HELPERS ----------------

def create_member(name, location):
    member = Member(name=name, location=location)
    session.add(member)
    session.commit()
    return member


def get_all_members():
    return session.query(Member).all()


def get_member_by_id(member_id):
    return session.get(Member, member_id)


# ---------------- SKILL HELPERS ----------------

def add_skill_to_member(member_id, skill_name):
    member = get_member_by_id(member_id)
    if not member:
        return "member_not_found"

    # 🔒 CHECK FOR DUPLICATE SKILL (case-insensitive)
    for skill in member.skills:
        if skill.name.lower() == skill_name.lower():
            return "duplicate"

    skill = Skill(name=skill_name, member=member)
    session.add(skill)
    session.commit()
    return skill


# ---------------- JOB HELPERS ----------------

def add_job_to_member(member_id, description, amount):
    member = get_member_by_id(member_id)
    if not member:
        return None

    job = Job(description=description, amount=amount, member=member)
    session.add(job)
    session.commit()
    return job


def get_earnings():
    return (
        session.query(
            Member.name,
            func.sum(Job.amount)
        )
        .join(Job)
        .group_by(Member.id)
        .all()
    )
