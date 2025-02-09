Part 1 - Steps to use the DS5111 Repository:
1. Run "sudo apt update" on your virtual machine
2. Generate a new SSH key using these instructions under the "Generating a new SSH key" section: (resource) https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
3. Add the public side of the new SSH key to your github account by following these steps: (resource) https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
4. Set up SSH access in the virtual machine by following the steps in the "00_00_setup_script_for_git_github.md" file.
5. Set up your global git credentials using the teminal on your virtual machine by following the steps in the "00_01_setup_git_global_creds.sh" file. For the "USER", substitute your own email used with your github account. For the "NAME", substitute your own github username. After running "git config --global --list" the second time, you should see your username and email.
6. Clone this repo to the virtual machine by running the following command in your terminal: "git clone git@github.com:tjh0302/SP25_DS5111_-dcc7qe-.git". Then run the command "ls" and you should see the repo name.
7. Run the "init.sh" script in this repo. This completes the base steps for setting up your virtual machine.

Part 2 - Steps to add additional tools.
1. To install the chrome headless browser, run the command "bash install_chrome_headless.sh" in the terminal, which will execute the bash file.
2. Run "wget https://example.com" in the terminal to test that the browser works. Then run "cat index.html" which should output the html code for the website.
3. A file titled requirements.txt exists in the repo which lists the dependencies for the project.
4. Run the command "make update" in your terminal to run the makefile. This makefile uses the requirements.txt file.
5. Test the headless browser by running "make ygainers.csv" in the terminal.
6. Structure of the repo:
