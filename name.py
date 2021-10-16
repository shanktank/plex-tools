#!/usr/bin/python

import sys, os, re, pwd, grp, subprocess

# == Get current UID ================================================================================================= #

user = pwd.getpwuid(os.getuid()).pw_name

# == Functions ======================================================================================================= #

# Collapse contiguous spaces
def ws(f):
    return re.sub(" +", " ", f)

# Fix capitalization of S##E##
def cap(f):
    if re.search(r"s([0-9]{2,3})e([0-9]{2,3})", f):
        rename(f, re.sub(r"s([0-9]{2,3})e([0-9]{2,3})", r"S\1E\2", f))

# Format episode titles divided into parts
def part(f):
    #return re.sub(r"(Part|Verse) ([0-9])", r"(\1 \2)", f)
    return re.sub(r"[0-9] of ([0-9])", r"(Part \1)", f)

# Rename episode
def rename(f, n):
    os.rename(f, n)
    os.chmod(n, 0644)
    if user == "root": os.chown(n, pwd.getpwnam("root").pw_uid, grp.getgrnam("plex").gr_gid)

# == Main ============================================================================================================ #

order = 1
special = 1
delim = ' '
showdir = "./"

for f in sorted(os.listdir(showdir)):
    title_parts = f[:-4].split(delim)
    episode_num = title_parts[1][3:].strip()
    new_ep_name = title_parts[0].strip() + " S01E" + episode_num + ".mkv"
    rename(f.strip(), new_ep_name)

#    p = f.split(delim)
#    #n = "Dragon Ball Z - E%s.mkv" % p[4]
#    if re.search(r" \([0-9]{4}\)", f):
#        n = re.sub(r" \([0-9]{4}\)", "", f)
#        n = re.sub(r" [0-9]+p", "", n)
#        rename(f.strip(), n.strip())

#    ep = re.search(r"Episode [0-9]{1,2}", f)
#    sp = re.search(r"Episode [0-9]{1,2}\.[0-9]", f)
#    pt = re.search(r"Part [0-9]", f)
#    if ep or sp:
#        if pt:
#            n = "Dragon Ball Z Abridged: %s [%s] - S01E%s.mp4" % (ep.group(0), pt.group(0), "{:02}".format(order))
#        elif sp:
#            n = "Dragon Ball Z Abridged: Special %s - S01E%s.mp4" % (special, "{:02}".format(order))
#            special += 1
#        else:
#            n = "Dragon Ball Z Abridged: %s - S01E%s.mp4" % (ep.group(0), "{:02}".format(order))
#        order += 1
#        rename(f.strip(), n)
#        #print(n)
