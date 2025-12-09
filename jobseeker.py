from db import get_connection


# ------------------------------------------------------
# JOB SEEKER REGISTRATION
# ------------------------------------------------------
def jobseeker_register():
    """
    Registers a job seeker and stores role='job_seeker'.
    """
    conn = get_connection()
    cur = conn.cursor()

    print("\n--- Job Seeker Registration ---")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    try:
        sql = """
            INSERT INTO users (username, email, password, role)
            VALUES (%s, %s, %s, 'job_seeker')
        """
        cur.execute(sql, (username, email, password))
        conn.commit()
        print("Job seeker registered successfully!\n")

    except Exception as err:
        print("\nERROR during job seeker registration:")
        print(err)

    finally:
        cur.close()
        conn.close()



# ------------------------------------------------------
# JOB SEEKER LOGIN
# ------------------------------------------------------
def jobseeker_login():
    """
    Logs in a job seeker.
    Returns seeker_id if login succeeds.
    """
    conn = get_connection()
    cur = conn.cursor()

    print("\n--- Job Seeker Login ---")
    email = input("Enter email: ")
    password = input("Enter password: ")

    try:
        sql = """
            SELECT user_id, username
            FROM users
            WHERE email = %s AND password = %s AND role = 'job_seeker'
        """
        cur.execute(sql, (email, password))
        row = cur.fetchone()

        if row:
            seeker_id, username = row
            print(f"\nWelcome, {username} (Job Seeker)!")
            return seeker_id
        else:
            print("\nInvalid email/password or not a job seeker.")
            return None

    except Exception as err:
        print("\nERROR during job seeker login:")
        print(err)
        return None

    finally:
        cur.close()
        conn.close()



# ------------------------------------------------------
# VIEW JOBS
# ------------------------------------------------------
def view_jobs():
    """
    Shows all jobs from the jobs table.
    """
    conn = get_connection()
    cur = conn.cursor()

    print("\n--- Available Jobs ---")

    try:
        sql = """
            SELECT j.job_id, j.job_title, j.job_description, j.date_posted, u.username
            FROM jobs j
            JOIN users u ON j.recruiter_id = u.user_id
            ORDER BY j.date_posted DESC
        """
        cur.execute(sql)
        rows = cur.fetchall()

        if not rows:
            print("No jobs posted yet.\n")
        else:
            for job_id, title, desc, date_posted, recruiter_name in rows:
                print(f"\nJob ID       : {job_id}")
                print(f"Title        : {title}")
                print(f"Description  : {desc}")
                print(f"Posted By    : {recruiter_name}")
                print(f"Date Posted  : {date_posted}")
            print()

    except Exception as err:
        print("\nERROR while fetching jobs:")
        print(err)

    finally:
        cur.close()
        conn.close()



# ------------------------------------------------------
# APPLY FOR A JOB
# ------------------------------------------------------
def apply_for_job(seeker_id):
    """
    Allows job seeker to apply for a job.
    Inserts the application in the applications table.
    """
    view_jobs()  # Show all jobs first

    conn = get_connection()
    cur = conn.cursor()

    try:
        job_id = input("Enter the Job ID you want to apply for: ")

        # Check job exists
        cur.execute("SELECT job_id FROM jobs WHERE job_id = %s", (job_id,))
        if not cur.fetchone():
            print("Invalid Job ID. Try again.\n")
            return

        sql = """
            INSERT INTO applications (job_id, seeker_id, status)
            VALUES (%s, %s, 'applied')
        """
        cur.execute(sql, (job_id, seeker_id))
        conn.commit()
        print("Application submitted successfully!\n")

    except Exception as err:
        print("\nERROR while applying for job:")
        print(err)

    finally:
        cur.close()
        conn.close()



# ------------------------------------------------------
# JOB SEEKER MENU
# ------------------------------------------------------
def jobseeker_menu(seeker_id):
    """
    After login, job seeker sees this menu.
    """
    while True:
        print("\n--- Job Seeker Menu ---")
        print("1. View Jobs")
        print("2. Apply for a Job")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            view_jobs()
        elif choice == "2":
            apply_for_job(seeker_id)
        elif choice == "3":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Try again.")
