# Coding a simple password manager

## Learning goals

Through this assigment,  you will learn to write and test a tiny software program collaboratively as a group.

## Background 

Develop a Python-based password manager that allows users tostore and retrieve website login credentials. Additionally, implement a password strength checker to encourage users to create strong passwords.  If you time and motivation for more, also add a password generator feature that allows users to generate strong and random passwords when adding new entries to the password manager.  You are provided with a coding templete, which as ready-make functions for Ceaser cipher excryption and decryption.  Please note that the Caesar cipher encryption is only for educational purposes. Real-world password managers use strong encryption algorithms and secure storage methods.

## Prepatory actions

1. Create a new repository for your team based on this templete called "emptypwmanager". See instructions at [GitHub Docs: Creating a repository from a template] (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
Enable security vulnerabilities reporting for your repository. See instructions at [GitHub Docs: Configuring private vulnerability reporting for a repository] (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/configuring-private-vulnerability-reporting-for-a-repository)
2. Protect the main branch of your repository. Notice a blue warning message about an unprotected branch and follow a link to the branch protection settings. Under "Protect matching branches", select "Require a pull request before merging". Optionally, to require approval (by another group member) before a pull request can be merged, you can also select "Require approvals". See more instructions at [GitHub Docs: Managing a branch protection rule] https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule
3. Optionally, use GitHub issues to manage your work as a team and assign tasks to each group member.  For instructions, see [GitHub Docs: Quickstart for GitHub Issues]  https://docs.github.com/en/issues/tracking-your-work-with-issues/quickstart

## Workflow actions

1.  Implement a simple password manager on top of the ready templete (at main.py). Do NOT change names of functions, nor the provided user interface.
2.  You should implement the following functions: adding password, restrieving password, checking password strengh,  loading passwords from file and saving passwords to file. Optionionally,  add a random password generator.
3.  If yuo can, please use the ready-provided funtions to encrypt and decrypt the password instead of writing them to file with plain text (while noting this encryption methos is only for educational purposes and not strong enough for real password managers).
4.  Test your password manager either manually or by using a ready-made code for automated unit tests (at test.py), you can freely modify testing code as needed
5.  Make sure that all relevant code changes are merged into the main repository before submitting the assigment for review. See Canvas for instructions on how to submit.
