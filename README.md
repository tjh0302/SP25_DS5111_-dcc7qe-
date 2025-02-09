Steps to use the DS5111 Repository:
1. Run "sudo apt update" on your virtual machine
2. Generate a new SSH key using these instructions under the "Generating a new SSH key" section: (resource) https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
3. Add the public side of the new SSH key to your github account by following these steps: (resource) https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
4. Set up SSH access in the virtual machine by following the steps in the "00_00_setup_script_for_git_github.md" file.
5. Set up your global git credentials using the teminal on your virtual machine by following the steps in the "00_01_setup_git_global_creds.sh" file. For the "USER", substitute your own email used with your github account. For the "NAME", substitute your own github username. After running "git config --global --list" the second time, you should see your username and email.
6. Clone your repo to the virtual machine by running the following command in your terminal: "git clone <ssh repo link>". Then run the command "ls" and you should see your repo name.
