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
    f = re.sub(r"(Part|Verse) ([0-9])", r"(\1 \2)", f)
    f = re.sub(r"[0-9] of ([0-9])", r"(Part \1)", f)
    return f

# Rename episode
def rename(f, n):
    os.rename(f, n)
    os.chmod(n, 0644)
    if user == "root": os.chown(n, pwd.getpwnam("root").pw_uid, grp.getgrnam("plex").gr_gid)

# == Main ============================================================================================================ #

part_delim = " "
season_dir = "./"

for f in sorted(os.listdir(season_dir)):
    title_parts = f[:-4].split(part_delim)
    episode_num = title_parts[1][3:].strip()
    new_ep_name = title_parts[0].strip() + " S01E" + episode_num + ".mkv"
    rename(f.strip(), new_ep_name)
