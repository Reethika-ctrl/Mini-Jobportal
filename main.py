from recruiter import recruiter_register, recruiter_login, recruiter_menu
from jobseeker import jobseeker_register, jobseeker_login, jobseeker_menu

# ------------------------------------------------------
# MAIN MENU — ENTRY POINT OF THE WHOLE PROGRAM
# ------------------------------------------------------
def main_menu():
    """
    Shows the first menu when the program starts.
    Lets user choose registration, login, or exit.
    """
    while True:
        print("\n=== Mini Job Portal ===")
        print("1. Register as Recruiter")
        print("2. Register as Job Seeker")
        print("3. Login as Recruiter")
        print("4. Login as Job Seeker")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            recruiter_register()

        elif choice == "2":
            jobseeker_register()

        elif choice == "3":
            recruiter_id = recruiter_login()
            if recruiter_id:
                recruiter_menu(recruiter_id)  # redirect to recruiter menu

        elif choice == "4":
            seeker_id = jobseeker_login()
            if seeker_id:
                jobseeker_menu(seeker_id)    # redirect to job seeker menu

        elif choice == "5":
            print("Exiting Mini Job Portal. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main_menu()
