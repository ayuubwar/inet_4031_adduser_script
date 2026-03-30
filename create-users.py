#!/usr/bin/python3

# INET4031
# Your Name
# Date Created: March 29, 2026
# Date Last Modified: March 29, 2026

# os allows us to run operating system commands like adduser
# re allows us to use regular expressions to search for patterns in strings
# sys allows us to read from standard input (stdin)
import os
import re
import sys

def main():

    # Read each line from standard input one at a time
    for line in sys.stdin:

        # Check if the line starts with # which means it should be skipped
        match = re.match("^#",line)

        # Remove whitespace and split the line into fields using colon as delimiter
        fields = line.strip().split(':')

        # If the line starts with # OR does not have exactly 5 fields, skip it
        # This handles both commented out lines and malformed/incomplete lines
        if match or len(fields) != 5:
            continue

        # Extract username, password, and full name from the fields
        # gecos is the full name field stored in /etc/passwd
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Split the groups field by comma to get individual group names
        groups = fields[4].split(',')

        print("==> Creating account for %s..." % (username))

        # Build the adduser command with the username and full name
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        print(cmd)
        os.system(cmd)

        print("==> Setting the password for %s..." % (username))

        # Build the command to set the user's password using passwd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        print(cmd)
        os.system(cmd)

        # Loop through each group and add the user if group is not '-'
        for group in groups:
            # A '-' in the groups field means no groups should be assigned
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
