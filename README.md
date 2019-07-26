# Snowflake Account Migration Script
This script can be used to help in migrating Snowflake Users/Roles/Grants from one Snowflake account to another. The script will print out SQL commands that can be used in another Snowflake account to re-create users, roles and grants (work in progress).

## Usage:
1. Clone the repo: `git clone https://github.com/filanthropic/snowflake-migrate-users.git && cd snowflake-migrate-users`
2. Create Python3 Virtual Env: `python3 -m venv .`
3. Activate virtual env: `source bin/activate`
4. Upgrade pip: `pip install --upgrade pip`
5. Install Snowflake Python Connector and other dependencies: `pip install -r requirements.txt`
6. Open `migrate_users_roles_grants.py` and provide your Snowflake source account name and credentials
7. Run: `python migrate_users_roles_grants.py`
