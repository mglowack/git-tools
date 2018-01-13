from git import Repo
import argparse
import sys

parser = argparse.ArgumentParser(description='Git tools for pushing WIP changes to remote')
parser.add_argument('-r', '--remote', metavar='name', default='origin')
parser.add_argument('-n', '--no-push', dest='push', default='true', action='store_false')

args = parser.parse_args(sys.argv[1:])
print args

repo = Repo('.')
msg = repo.head.reference.commit.message.strip()
git = repo.git

print git.status()
print git.add('.')

if msg == "WIP":
    print 'amending WIP commit'
    print git.commit('--amend', '--no-edit')
else:
    print 'creating WIP commit'
    print git.commit('-m', 'WIP')

if args.push:
    print 'pushing to remote \'{0}\''.format(args.remote)
    git.push(args.remote, '--force')
