from git import Repo
import argparse
import sys

parser = argparse.ArgumentParser(description='Git tools for pushing WIP changes to remote')
parser.add_argument('--path', metavar='repo-path', default='.')
parser.add_argument('-r', '--remote', metavar='name', default='origin')
parser.add_argument('--review', dest='review', default=False, action='store_true')
parser.add_argument('-n', '--no-push', dest='push', default=True, action='store_false')

args = parser.parse_args(sys.argv[1:])
print(args)

repo = Repo(args.path)
msg = repo.head.reference.commit.message.strip()
git = repo.git
branch = repo.active_branch.name
remoteBranch = branch + '-review' if args.review else branch

print(git.status())
print(git.add('.'))

if args.review:
    print('amending previous commit')
    print(git.commit('--amend', '--no-edit'))
else:
    if msg == "WIP":
        print('amending WIP commit')
        print(git.commit('--amend', '--no-edit'))
    else:
        print('creating WIP commit')
        print(git.commit('-m', 'WIP'))

print('pushing to remote \'{0}\', branch \'{1}\''.format(args.remote, remoteBranch))
if args.push:
    print(git.push(args.remote, '{0}:{1}'.format(branch, remoteBranch), '--force'))
