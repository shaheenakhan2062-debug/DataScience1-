print('Welcome from user1')
print('Welcome from vivek')
print('Welcome from bibek')

These are the exact steps and commands I used to clear the push issue:
1.	Checked the repo remote and branch
2.	git remote -v
3.	git branch --show-current
4.	Cleared the cached GitHub credentials so Git would stop using the old account/session
5.	"protocol=https`nhost=github.com`n" | git credential-manager erase
6.	Tested push permission without changing anything on the branch feature1
7.	git push --dry-run origin feature1
8.	Performed the real push
9.	git push -u origin feature1

The most common and safest way to collaborate on a GitHub project is to use branches + pull requests (PRs). This allows your friend to make changes without directly modifying your main branch, and gives you a chance to review everything before merging.
________________________________________
Option 1: Add Your Friend as a Collaborator (Recommended for Private Repositories)
Step 1: Invite Your Friend
1.	Open your repository on GitHub.
2.	Click Settings.
3.	In the left sidebar, click Collaborators (or Collaborators and teams).
4.	Click Add people.
5.	Enter your friend's GitHub username or email.
6.	Send the invitation.
7.	Your friend must accept the invitation.
After accepting, your friend can clone, create branches, push code, and create pull requests.
________________________________________
Step 2: Your Friend Clones the Repository
Your friend runs:
git clone https://github.com/yourusername/project.git
cd project
This downloads the repository to their computer.
________________________________________
Step 3: Your Friend Creates a New Branch
Your friend should never work directly on main.
Create a feature branch:
git checkout -b add-login-feature
Example branch names:
fix-navbar
update-readme
add-authentication
bugfix-payment
This isolates their work from the production code.
________________________________________
Step 4: Make Changes
Your friend edits files as needed.
Check modified files:
git status
________________________________________
Step 5: Commit Changes
Stage files:
git add .
Create a commit:
git commit -m "Add login page and validation"
A commit is a snapshot of the changes.
________________________________________
Step 6: Push Branch to GitHub
git push origin add-login-feature
This uploads the branch to GitHub.
________________________________________
Step 7: Create a Pull Request
On GitHub:
1.	Open the repository.
2.	GitHub will usually show a Compare & Pull Request button.
3.	Click it.
4.	Add:
o	Title
o	Description
o	Screenshots (if applicable)
5.	Click Create Pull Request.
Now the changes are waiting for your review.
________________________________________
How You Review Your Friend's Changes
Method 1: Through GitHub Website
Open the Pull Request.
You will see tabs such as:
•	Conversation
•	Commits
•	Files Changed
Click Files Changed.
GitHub highlights:
- old code
+ new code
Red = removed
Green = added
You can:
•	Review line by line
•	Add comments
•	Request changes
•	Approve the PR
This is usually the easiest method.
________________________________________
Method 2: Review Locally on Your Computer
Fetch all branches:
git fetch
View remote branches:
git branch -r
Checkout your friend's branch:
git checkout add-login-feature
Compare with main:
git diff main
Or:
git diff main..add-login-feature
See exactly what changed.
________________________________________
How to See Commit History
View commits:
git log --oneline
Example:
c52ab34 Add login validation
8af3d12 Create login page
See detailed changes in a commit:
git show c52ab34
________________________________________
How to Test Before Merging
Before merging:
1.	Pull your friend's branch.
2.	Run the application.
3.	Run automated tests.
4.	Verify functionality.
Example:
npm test
or
pytest
or
mvn test
depending on the project.
________________________________________
How to Merge the Pull Request
On GitHub
After reviewing:
1.	Open the PR.
2.	Click Merge Pull Request.
3.	Click Confirm Merge.
GitHub merges the branch into main.
________________________________________
Locally Using Git
Switch to main:
git checkout main
Get latest changes:
git pull origin main
Merge branch:
git merge add-login-feature
Push updated main:
git push origin main
________________________________________
How to Handle Merge Conflicts
Sometimes both of you modify the same lines.
Git may report:
CONFLICT (content): Merge conflict
Open the file and you'll see:
<<<<<<< HEAD
Your code
=======
Friend's code
>>>>>>> add-login-feature
Edit the file to keep the correct version:
Combined final code
Then:
git add .
git commit -m "Resolve merge conflict"
________________________________________
Best Practice Workflow for Teams
A typical workflow is:
main
 │
 ├── friend-feature-1
 ├── friend-feature-2
 └── your-feature
Process:
1.	Keep main stable.
2.	Every feature gets its own branch.
3.	Create Pull Requests.
4.	Review changes.
5.	Run tests.
6.	Merge into main.
7.	Delete old branches.
________________________________________
Alternative: Friend Forks the Repository
If you don't want to give direct repository access:
1.	Your friend clicks Fork on GitHub.
2.	GitHub creates a copy in their account.
3.	They work on their fork.
4.	They create a Pull Request back to your repository.
This is the workflow used by most open-source projects.
________________________________________
Recommended Setup
For learning, personal projects, and small teams:
1. Add friend as collaborator
2. Friend creates feature branch
3. Friend pushes branch
4. Friend opens Pull Request
5. You review Files Changed
6. Run tests
7. Merge Pull Request into main
8. Delete branch
This approach protects the main branch while giving you full visibility and control over every change your friend makes.


The command:
git checkout -b add-login-feature
actually performs two actions at once:
1.	Creates a new branch named add-login-feature
2.	Switches (checks out) to that branch immediately
It's equivalent to:
git branch add-login-feature
git checkout add-login-feature
or in newer Git versions:
git switch -c add-login-feature
________________________________________
Understanding Branches First
Think of a Git branch as a separate line of development.
Suppose your repository currently looks like this:
main
  |
  A --- B --- C
You are currently on the main branch at commit C.
Now you run:
git checkout -b add-login-feature
Git creates a new branch pointing to the same commit:
main
  |
  A --- B --- C
              ^
              |
     add-login-feature
And Git moves you onto the new branch.
________________________________________
What Does checkout Mean?
The word checkout means:
"Switch my working directory and HEAD to another branch or commit."
For example:
git checkout main
moves you back to the main branch.
________________________________________
What Does -b Mean?
The -b option means:
"Create a new branch before switching."
Without -b:
git checkout add-login-feature
Git expects the branch already exists.
If it doesn't exist, you'll get an error like:
error: pathspec 'add-login-feature' did not match any file(s) known to git
Using -b tells Git to create it first.
________________________________________
Example Step-by-Step
Assume your repository contains:
main
  |
  A --- B --- C
Current branch:
git branch
Output:
* main
Create a feature branch:
git checkout -b add-login-feature
Output:
Switched to a new branch 'add-login-feature'
Now:
git branch
Output:
* add-login-feature
  main
The * indicates your current branch.
________________________________________
What Happens After You Make Changes?
Suppose you edit files and commit:
git add .
git commit -m "Add login page"
Git creates a new commit:
main
  |
  A --- B --- C

add-login-feature
  |
  A --- B --- C --- D
Notice:
•	main still points to C
•	add-login-feature points to D
Your work is isolated from main.
________________________________________
Why Is This Useful?
Imagine you accidentally break something while developing.
Because you're working in a separate branch:
main (safe)
add-login-feature (experimental)
The production-ready code remains untouched.
This is why teams rarely develop directly on main.
________________________________________
Viewing Your Current Branch
Check where you are:
git branch
Example:
* add-login-feature
  main
or
git status
Output:
On branch add-login-feature
________________________________________
Pushing the New Branch to GitHub
Creating the branch locally does not automatically create it on GitHub.
You must push it:
git push origin add-login-feature
Now GitHub will also have:
main
add-login-feature
________________________________________
What Does origin Mean?
When you clone a repository:
git clone https://github.com/user/project.git
Git automatically creates a remote called:
origin
You can view remotes:
git remote -v
Example:
origin https://github.com/user/project.git
So:
git push origin add-login-feature
means:
Push my local branch add-login-feature to the remote repository named origin.
________________________________________
How to Return to Main
At any time:
git checkout main
or
git switch main
Now you're back on the main branch.
________________________________________
Visual Example
Before creating a branch:
main
 |
 A --- B --- C
Run:
git checkout -b add-login-feature
After creating branch:
main
 |
 A --- B --- C
               \
                add-login-feature
After making two commits:
main
 |
 A --- B --- C

add-login-feature
 |
 A --- B --- C --- D --- E
After merging:
main
 |
 A --- B --- C --- D --- E
The feature becomes part of main.
________________________________________
Modern Alternative
Newer Git versions recommend:
git switch -c add-login-feature
instead of:
git checkout -b add-login-feature
because switch is dedicated to branch operations and is easier to understand.
Both commands achieve the same result:
git checkout -b add-login-feature
and
git switch -c add-login-feature
→ create a new branch and immediately move you to it.

