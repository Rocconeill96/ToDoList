# 1. Basic set-up and information 


`git init` - Initialise a new Git repository in the current directory.

`git clone <repo-url>` - Clone a remote repository to your local machine.

`git status` - Show the current status (staged, unstaged, untracked files).

`git config --global user.name "Your Name"` - Set your global Git username.

`git config --global user.email "you@example.com"` - Set your global git email.  

# 2. Tracking Changes

`git add <file>` - Stage a specific file for commit.

`git add .` - Stage all changes in the current directory.

`git reset <file>` - Unstage a file (but keep changes)

`git restore <file>` - Discard changes in a file (revert to last commit)

`git rm <file>` - Remove a tracked file (WARNING: This command will also remove the file from the directory)

`git rm --cached <file>` - Remove a file from tracking but keep it locally

# 3. Commtting 

`git commit -m "message"` - Commit staged changes with a message

`git commit -am "message"` - Stage and commit modified files (not new ones)

`git log` - View commit history

`git show <commit-hash>` - Show details of a specific commit

# 4. Branching + Merging

`git branch` - List branches 

`git branch <name>` - Create a new branch

`git checkout <branch>` - Switch to another branch

`git switch <branch>` - (modern alternative to checkout for swtiching)

`git merge <branch>` - Merge a branch into the current one

`git rebase <branch>` - Reapply commits from your branch on top of another 

# 5. Remote Repositories

`git remote -v` - List remotes

`git remote add origin <url>` - Add a remote repository

`git fetch` - Download changes from remote (but don't merge)

`git pull` - Fetch and merge changes from remote

`git push` - Push your local commits to remote

`git push -u origin <branch>` - Push a new branch and set upstream tracking

# 6. Undoing and fixing

`git reset --hard <commit>` - Reset to a specific commit (destroy changes!!)

`git reset --soft <commit>` - Reset but keep changes staged

`git revert <commit>` - Create a new commit

`git stash` - Temporarily save changes without committing

`git stash pop` - Reapply stashed changes

# 7. Cleaning up

`git clean -fd` - Remove untracked files and directories

`git clean -fdx` - Remove ignored and untracked files
