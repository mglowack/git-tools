from git import Repo
import sys
import argparse

parser = argparse.ArgumentParser(description='Git tools.')
parser.add_argument('-r', '--remote', metavar='name', default='origin')
parser.add_argument('repoPath')
parser.add_argument('branchName')

args = parser.parse_args(sys.argv[1:])
print args


repo = Repo(args.repoPath)
git = repo.git

print git.status()
print git.fetch('-v', args.remote)
print git.checkout(args.branchName)
print git.reset('--hard', '{0}/{1}'.format(args.remote, args.branchName))
