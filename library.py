import argparse, configparser, grp, pwd, hashlib, os, re, sys, zlib
from datetime import datetime
from fnmatch import fnmatch
from math import ceil

argparser = argparse.ArgumentParser(description = "Command-line parser")
argsubparser = argparser.add_argument(title = "Command", dest = "command")
argsubparser.required = True


def cmd_add(args):
    print(f"This is the arg: {args}")

def cmd_cat_file(args):
    print(f"This is the arg: {args}")

def cmd_check_ignore(args):
    print(f"This is the arg: {args}")

def cmd_checkout(args):
    print(f"This is the arg: {args}")

def cmd_commit(args):
    print(f"This is the arg: {args}")

def cmd_hash_object(args):
    print(f"This is the arg: {args}")

def cmd_init(args):
    print(f"This is the arg: {args}")

def cmd_log(args):
    print(f"This is the arg: {args}")

def cmd_ls_files(args):
    print(f"This is the arg: {args}")

def cmd_ls_tree(args):
    print(f"This is the arg: {args}")

def cmd_rev_parse(args):
    print(f"This is the arg: {args}")

def cmd_rm(args):
    print(f"This is the arg: {args}")

def cmd_show_ref(args):
    print(f"This is the arg: {args}")

def cmd_status(args):
    print(f"This is the arg: {args}")

def cmd_tag(args):
    print(f"This is the arg: {args}")


def main(argv = sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case "add" : cmd_add(args)
        case "cat-file" : cmd_cat_file(args)
        case "check-ignore" : cmd_check_ignore(args)
        case "checkout" : cmd_checkout(args)
        case "commit" : cmd_commit(args)
        case "hash-object" : cmd_hash_object(args)
        case "init" : cmd_init(args)
        case "log" : cmd_log(args)
        case "ls-files" : cmd_ls_files(args)
        case "ls-tree" : cmd_ls_tree(args)
        case "rev-parse" : cmd_rev_parse(args)
        case "rm" : cmd_rm(args)
        case "show-ref" : cmd_show_ref(args)
        case "status" : cmd_status(args)
        case "tag" : cmd_tag(args)
        case _ : print("Invalid command")

