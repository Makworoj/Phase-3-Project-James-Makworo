from helpers import (
    create_member,
    get_all_members,
    get_member_by_id,
    add_skill_to_member,
    add_job_to_member,
    get_earnings
)


# ---------- VALIDATION HELPER ----------
def letters_only(text):
    return text.replace(" ", "").isalpha()


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

            if not letters_only(name):
                print("❌ Error: Name must contain letters only.")
                continue

            if not letters_only(location):
                print("❌ Error: Location must contain letters only.")
                continue

            member = create_member(name, location)
            print(f"✅ Member created successfully. ID: {member.id}")

        # ---------- LIST MEMBERS ----------
        elif choice == "2":
            members = get_all_members()

            if not members:
                print("No members found.")
                continue

            for m in members:
                print(f"{m.id} | {m.name} | {m.location}")

        # ---------- ADD SKILL (WITH DUPLICATE CHECK) ----------
        elif choice == "3":
            try:
                member_id = int(input("Enter member ID: "))
            except ValueError:
                print("❌ Error: Member ID must be a number.")
                continue

            skill_name = input("Enter skill name: ").strip()

            if not letters_only(skill_name):
                print("❌ Error: Skill name must contain letters only.")
                continue

            result = add_skill_to_member(member_id, skill_name)

            if result == "member_not_found":
                print("❌ Error: Member not found.")
                continue

            if result == "duplicate":
                print("⚠️ Skill already listed for this member.")
                continue

            print(f"✅ Skill '{skill_name}' added successfully.")

        # ---------- ADD JOB ----------
        elif choice == "4":
            try:
                member_id = int(input("Enter member ID: "))
            except ValueError:
                print("❌ Error: Member ID must be a number.")
                continue

            description = input("Enter job description: ").strip()

            if not letters_only(description):
                print("❌ Error: Job description must contain letters only.")
                continue

            try:
                amount = float(input("Enter amount earned: "))
            except ValueError:
                print("❌ Error: Amount must be a number.")
                continue

            if amount <= 0:
                print("❌ Error: Amount must be greater than zero.")
                continue

            job = add_job_to_member(member_id, description, amount)

            if not job:
                print("❌ Error: Member not found.")
                continue

            print(f"💰 Job recorded successfully. Amount: KES {amount}")

        # ---------- VIEW EARNINGS ----------
        elif choice == "5":
            earnings = get_earnings()

            if not earnings:
                print("No earnings recorded yet.")
                continue

            for name, total in earnings:
                print(f"{name}: KES {total}")

        # ---------- VIEW MEMBER SKILLS ----------
        elif choice == "6":
            try:
                member_id = int(input("Enter member ID: "))
            except ValueError:
                print("❌ Error: Member ID must be a number.")
                continue

            member = get_member_by_id(member_id)

            if not member:
                print("❌ Error: Member not found.")
                continue

            print(f"\nMember: {member.id} | {member.name}")

            if not member.skills:
                print("No skills recorded for this member.")
                continue

            print("Skills:")
            for s in member.skills:
                print(f"{s.id} | {s.name}")

        # ---------- EXIT ----------
        elif choice == "0":
            print("👋 Exiting SkillTrack. Goodbye!")
            break

        # ---------- INVALID OPTION ----------
        else:
            print("❌ Error: Invalid option. Please select a valid menu number.")


if __name__ == "__main__":
    menu()
