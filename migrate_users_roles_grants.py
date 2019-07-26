#!/usr/bin/env python
import snowflake.connector

# Gets the version
ctx = snowflake.connector.connect(
    user='<YOUR_SNOWFLAKE_USERNAME>',
    password='<YOUR_SNOWFLAKE_PASSWORD>',
    account='<YOUR_SNOWFLAKE_ACCOUNT_NAME>'
    )
cs = ctx.cursor()
try:
    #print("starting to execute query")
    #1: get users
    cs.execute("use role ACCOUNTADMIN")
    cs.execute("show users")
    #print("query returned")
    print(','.join([col[0] for col in cs.description]))
    users = cs.fetchall()
    for user in users:
        #create user user1 password='abc123' default_role = myrole must_change_password = true;
        print("------------------------------")
        print("--creating user: {0}".format(user[0]))
        print("------------------------------")
        print("create user if not exists {0} password='abc123' default_role = {1} must_change_password = true;".format(user[0], user[15]))
        cs.execute("show grants to user {0}".format(user[0]))
        #created_on,role,granted_to,grantee_name,granted_by
        grants = cs.fetchall()
        for grant in grants:
            print("grant role {0} to {1} {2};".format(grant[1], grant[2], grant[3]))


    #2: get roles
    cs.execute("use role ACCOUNTADMIN")
    cs.execute("show roles")
    #print(','.join([col[0] for col in cs.description]))
    roles = cs.fetchall()
    for role in roles:
        print("------------------------------")
        print("--creating role: {0}".format(role[1]))
        print("------------------------------")
        print("create role if not exists {0};".format(role[1]))

        #3: get grants
        #cs.execute("show grants of role DBA_CITIBIKE")
        # created_on,privilege,granted_on,name,granted_to,grantee_name,grant_option,granted_by
        cs.execute("show grants to role {0}".format(role[1]))
        #print(','.join([col[0] for col in cs.description]))
        grants = cs.fetchall()
        for grant in grants:
            if grant[5] != "PUBLIC":
                if grant[2] == "ROLE" and grant[4] == "ROLE":
                    print("grant role {0} to role {1};".format(grant[3], grant[5]))
                else:
                    print("grant {0} on {1} {2} to {3} {4};".format(grant[1], grant[2], grant[3], grant[4], grant[5]))
except Exception as e:
    print("Error occured: ", str(e))
finally:

    cs.close()
ctx.close()
