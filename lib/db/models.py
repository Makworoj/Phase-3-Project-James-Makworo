from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .session import Base, engine

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)

    skills = relationship("Skill", back_populates="member", cascade="all, delete")
    jobs = relationship("Job", back_populates="member", cascade="all, delete")

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    member_id = Column(Integer, ForeignKey("members.id"))

    member = relationship("Member", back_populates="skills")

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    amount = Column(Float, nullable=False)
    member_id = Column(Integer, ForeignKey("members.id"))

    member = relationship("Member", back_populates="jobs")

Base.metadata.create_all(engine)
