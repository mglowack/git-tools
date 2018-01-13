import argparse
import sys
import subprocess
import os

def cmd(params):
    print subprocess.check_output(params)

parser = argparse.ArgumentParser(description='Tool for syncing branches across a workspace.')
parser.add_argument('-w', '--workspace', metavar='path', default='.')
parser.add_argument('-r', '--remote', metavar='name', default='origin')
parser.add_argument('repos', nargs='+')

args = parser.parse_args(sys.argv[1:])
print args

for repo in args.repos:
    parts = repo.split('/')
    repoName = parts[0]
    branchName = parts[1]

    repoPath = os.path.join(args.workspace, repoName)

    print 'syncing repo \'{0}\' with branch \'{1}\' from remote \'{2}\''.format(repoName, branchName, args.remote)
    cmd(['python', 'replace-branch.py', '-r', args.remote, repoPath, branchName])

