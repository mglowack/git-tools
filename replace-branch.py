from git import Repo
import sys

repoPath = sys.argv[1]
repoBranchName = sys.argv[2]
repoRemoteName = sys.argv[3] if len(sys.argv) > 3 else 'origin'

repo = Repo(repoPath)
git = repo.git

print git.status()
print git.fetch('-v', repoRemoteName)
print git.checkout(repoBranchName)
print git.reset('--hard', '{0}/{1}'.format(repoRemoteName, repoBranchName))
