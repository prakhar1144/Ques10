### Git commands learnt during Ques10 Internship
Command | Use | Extra
|----|----|----|
git init | Initiate VCS in local repo |
git clone url | Get an existing repo |
git status | To get the current status of repo i.e. what is staged, what is commited|
git add file_name | Stage the file for commit | git add is a multipurpose command — you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved
git commit -m "message" | Snapshot at that stage |
git push origin branch_name | Push the commit to the mentioned branch at origin |
git stash | Save at that stage |
git pull origin branch_name | update your local repo with remote | git fetch + git merge
git fetch && git checkout testing ||
git diff | changes not yet staged | shows the exact lines
git diff --staged | changes staged not yet commited |
git branch branch_name | create a branch |
git checkout branch_name | Change / switch branch | Either commit your code, or stash them before switching branch 
#### Extras
* files are in four states : untracked, unmodified, modified, staged [Details here](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
