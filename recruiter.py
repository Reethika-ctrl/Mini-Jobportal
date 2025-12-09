from db import get_connection

# ------------------------------------------------------
# RECRUITER REGISTRATION
# ------------------------------------------------------
def recruiter_register():
    """
    Registers a new recruiter and stores their details
    into the users table with role='recruiter'.
    """
    conn = get_connection()
    cur = conn.cursor()

    print("\n--- Recruiter Registration ---")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    try:
        sql = """
            INSERT INTO users (username, email, password, role)
            VALUES (%s, %s, %s, 'recruiter')
        """
        cur.execute(sql, (username, email, password))
        conn.commit()
        print("Recruiter registered successfully!\n")

    except Exception as err:
        print("\nERROR during recruiter registration:")
        print(err)

    finally:
        cur.close()
        conn.close()



# ------------------------------------------------------
# RECRUITER LOGIN
# ------------------------------------------------------
def recruiter_login():
    """
    Logs in recruiter by checking email + password.
    Returns recruiter_id if login succeeds.
    Returns None if login fails.
    """
    conn = get_connection()
    cur = conn.cursor()

    print("\n--- Recruiter Login ---")
    email = input("Enter email: ")
    password = input("Enter password: ")

    try:
        sql = """
            SELECT user_id, username
            FROM users
            WHERE email = %s AND password = %s AND role = 'recruiter'
        """
        cur.execute(sql, (email, password))
        row = cur.fetchone()

        if row:
            recruiter_id, username = row
            print(f"\nWelcome, {username} (Recruiter)!")
            return recruiter_id
        else:
            print("\nInvalid email/password or not a recruiter.")
            return None

    except Exception as err:
        print("\nERROR during recruiter login:")
        print(err)
        return None

    finally:
        cur.close()
        conn.close()



# ------------------------------------------------------
# POST A JOB
# ------------------------------------------------------
def post_job(recruiter_id):
    """
    Allows a recruiter to post a job.
    The job will be stored in the jobs table.
    """
    conn = get_connection()
    cur = conn.cursor()

    print("\n--- Post a Job ---")
    title = input("Enter job title: ")
    description = input("Enter job description: ")

    try:
        sql = """
            INSERT INTO jobs (recruiter_id, job_title, job_description)
            VALUES (%s, %s, %s)
        """
        cur.execute(sql, (recruiter_id, title, description))
        conn.commit()
        print("Job posted successfully!\n")

    except Exception as err:
        print("\nERROR while posting job:")
        print(err)

    finally:
        cur.close()
        conn.close()



# ------------------------------------------------------
# VIEW APPLICANTS
# ------------------------------------------------------
def view_applicants(recruiter_id):
    """
    Shows all applications for jobs created by this recruiter.
    Uses JOIN to fetch job title + seeker details.
    """
    conn = get_connection()
    cur = conn.cursor()

    print("\n--- View Applicants for Your Jobs ---")

    try:
        sql = """
            SELECT 
                a.application_id,
                j.job_title,
                u.username,
                u.email,
                a.status,
                a.application_date
            FROM applications a
            JOIN jobs j ON a.job_id = j.job_id
            JOIN users u ON a.seeker_id = u.user_id
            WHERE j.recruiter_id = %s
            ORDER BY a.application_date DESC
        """
        cur.execute(sql, (recruiter_id,))
        rows = cur.fetchall()

        if not rows:
            print("No applicants found yet.\n")
        else:
            for app_id, job_title, seeker_name, seeker_email, status, app_date in rows:
                print(f"\nApplication ID: {app_id}")
                print(f"Job Title    : {job_title}")
                print(f"Seeker Name  : {seeker_name}")
                print(f"Seeker Email : {seeker_email}")
                print(f"Status       : {status}")
                print(f"Applied On   : {app_date}")
            print()

    except Exception as err:
        print("\nERROR while fetching applicants:")
        print(err)

    finally:
        cur.close()
        conn.close()



# ------------------------------------------------------
# RECRUITER MENU
# ------------------------------------------------------
def recruiter_menu(recruiter_id):
    """
    After login, recruiter sees this menu.
    All recruiter features are inside this loop.
    """
    while True:
        print("\n--- Recruiter Menu ---")
        print("1. Post a Job")
        print("2. View Applicants")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            post_job(recruiter_id)
        elif choice == "2":
            view_applicants(recruiter_id)
        elif choice == "3":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Try again.")
