# Change git history with force pushing

We can technically change the history of a git repo using soft resetting and then force push the new history.

## The steps:
- Reset HEAD to previous commit, but keep all file changes:

    ```bash
    git reset --soft HEAD~1
    ```
    This:
    - Removes the last commit from history,
    - Keeps all the code in your working directory and staging area. Use `git reset HEAD` if you want to unstage the changes. 

    (Optional) Double-check your working tree:

    ```bash
    git status
    ```
    You'll see all your files listed as staged.

- Force-push the new history to GitHub:
    ```bash
    git push origin <branch-name> --force
    ```

## Warning: Force-pushing rewrites history
- Only do this if you're the sole contributor, or all collaborators are aware.

- NEVER rewrite public/shared history unless absolutely necessary.