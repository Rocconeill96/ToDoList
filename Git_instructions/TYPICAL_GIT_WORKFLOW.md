# 1. Set Up (once/repository)

`git clone <repository_url>` - clones a repository to local machine 
or 
`git init` - initialises a repository in the current directory 

N.B. `git clone` is typically easier and less problematic. In other words, creat a repository in Github first THEN clone it

# 2. Create or Switch to a Branch

`git checkout -b feature-branch` - Create and switch to a new branch 

`git checkout feature-branch` - Switch to an existing branch

# 3. Make changes and stage them

`git status` - See which files are modified or untracked

`git add .` - Stage ALL changes

# 4. Commit changes

`git commit -m <"commit description">` - concise description of the commit

# 5. Keep your Branch updated (before pushing)

`git fetch origin` - Get latest changes from the remote

`git pull origin main` - Merge latest main branch into your branch

`git rebase origin/main` - Rebase your branch on top of main (RECOMMENDED: Cleaner history)

# 6. Push changes 

`git push origin feature-branch` - Push your branch to the remote

# 7. Open a Pull Request (on Github/Gitlab/Bitbucket)

* Open a PR/MR from `feature-branch` -> `main` (or `develop`)
* Get it reviewed and approved (in commercial environments) 

# 8. Merge and Clean up

`git checkout main/master`

`git pull origin main/master` - Make sure main is up to date

`git merge feature-branch` - Merge your feature into main/master

`git push origin main/master` - Push updated main to remote

`git branch -d feature-branch` - Delete the local branch

`git push origin --delete feature-branch` - Delete the remote branch

# 9. Occasional Maintenance

`git stash` - Temporarily store changes without committing

`git stash pop` - Reapply stashed changes

`git log --oneline --graph` - View a concise commit history

`git reset --hard HEAD~1` - Undo last commit (DANGER: destructive!!)