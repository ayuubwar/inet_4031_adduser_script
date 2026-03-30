# inet_4031_adduser_script
## Program Description
This script automates the process of adding multiple users and groups to a Linux system. Instead of manually running `adduser` and `passwd` commands for each user, this script reads from an input file and automatically runs those same commands for every user listed. This is especially useful when setting up many servers that need the same user accounts.

## Program Operation

### Input File Format
The input file is a colon-delimited file where each line represents one user with 5 fields:
- Field 1: username
- Field 2: password
- Field 3: last name
- Field 4: first name
- Field 5: group(s) — comma separated. Use `-` if no groups needed.

To skip a line, put a `#` at the beginning of the line.

### Command Execution
First make the script executable:
```
chmod +x create-users.py
```
Then run it:
```
sudo ./create-users.py < create-users.input
```

### Dry Run
