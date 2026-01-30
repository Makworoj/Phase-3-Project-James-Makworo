SKILLTRACK CLI

PROJECT DESCRIPTION
SkillTrack CLI is a menu-driven command-line application designed to help communities
track members, their skills, completed jobs, and total earnings.

The project addresses a common challenge where individuals possess income-generating
skills but lack a structured way to document and manage them.

The application allows users to:
- Register community members
- Assign skills to members
- Prevent duplicate skills for the same member
- Record completed jobs and earnings
- View total earnings per member
- View a member and all their associated skills


PROBLEM STATEMENT
In many communities, especially in informal and rural settings, people possess practical
skills such as repair services, technical work, or manual labor. However, these skills
and earnings are rarely documented.

SkillTrack CLI provides a simple, offline-friendly solution using a local database
to store and manage this information efficiently.


FEATURES
- Menu-driven CLI with continuous user interaction
- Input validation with clear error messages
- SQLite database persistence using SQLAlchemy ORM
- One-to-many relationships between members, skills, and jobs
- Prevention of duplicate skills per member
- Clear display of related data (members and their skills)


TECHNOLOGIES USED
- Python 3
- SQLAlchemy ORM
- SQLite
- Virtual Environment (venv)


PROJECT STRUCTURE

skilltrack/
│
├── lib/
│   ├── cli.py          Menu-driven CLI and user interaction
│   ├── helpers.py      Business logic and database operations
│   └── db/
│       ├── __init__.py Empty (marks package)
│       ├── models.py  ORM models (Member, Skill, Job)
│       └── session.py Database engine and session
│
├── skilltrack.db       SQLite database (ignored in git)
├── README.txt
├── .gitignore
└── venv/


DATA MODELS

Member
Represents a community member.
- id
- name
- location
- relationships: skills, jobs

Skill
Represents a skill owned by a member.
- id
- name
- member_id

Job
Represents a completed job and payment.
- id
- description
- amount
- member_id


HOW TO RUN THE APPLICATION

1. Activate Virtual Environment
   source venv/bin/activate

2. Install Dependencies
   pip install sqlalchemy

3. Run the CLI
   python lib/cli.py


MENU OPTIONS

1. Add Member
2. List Members
3. Add Skill
4. Add Job
5. View Earnings
6. View Member Skills
0. Exit


EXAMPLE USAGE

Add a Member
Enter member name: James Makworo
Enter member location: Nairobi

Add a Skill
Enter member ID: 1
Enter skill name: Engineer

If the skill already exists:
Skill already listed for this member.

View Member Skills
Member: 1 | James Makworo
Skills:
1 | Engineer
2 | Technician

Record a Job
Enter member ID: 1
Enter job description: Fire Suppression
Enter amount earned: 1500

View Earnings
James Makworo: KES 1500


INPUT VALIDATION
- Member IDs must be numeric
- Names, locations, skills, and job descriptions allow letters and spaces only
- Duplicate skills for the same member are prevented
- Negative or non-numeric job amounts are rejected


DESIGN PRINCIPLES
- Separation of concerns:
  * cli.py handles user interaction
  * helpers.py handles business logic
  * models handle data persistence
- Modular and readable code
- Clear error handling and user feedback


FUTURE ENHANCEMENTS
- Track unpaid vs paid jobs
- Delete or update members, skills, and jobs
- Skill-based job filtering
- Export earnings reports
- Web or mobile interface


CONCLUSION
SkillTrack CLI demonstrates effective use of Python, SQLAlchemy ORM, and menu-driven
CLI design to solve a real-world problem.

The project follows best practices in structure, validation, and separation of concerns,
making it easy to extend and maintain.
