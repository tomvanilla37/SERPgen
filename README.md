# setup
clone git files
```bash
mkdir ~/code/tomvanilla37
cd  ~/code/tomvanilla37
git clone git@github.com:tomvanilla37/SERPgen.git
cd SERPgen
mkdir raw_data
```

create a virtual env for the project:
```bash
pyenv virtualenv SERPgen
pyenv local SERPgen
pip install --upgrade pip
pip install -r https://gist.githubusercontent.com/krokrob/53ab953bbec16c96b9938fcaebf2b199/raw/9035bbf12922840905ef1fbbabc459dc565b79a3/minimal_requirements.txt
pip list
pip install -r requirements.txt
```

install the package
```bash
pip install -e .
```

remember that use the following command to update the master branch every morning.
```bash
pip pull
```

# Working inside a branch
make a branch
```bash
git branch BRANCH_NAME
```

switch to branch
```bash
git checkout BRANCH_NAME
```

after modifying your files, push them to the branch on github
```bash
git add FILES
git commit -m 'SOME_MASSAGE'
git push origin BRANCH_NAME
```

When you finish the code in your branch request to merge with master branch
```bash
git merge master
```

now you can switch to master branch again. (It seems out main branch name is not master!!!)
```bash
git checkout main
```

# old ...
# Data analysis
- Document here the project: SERPgen
- Description: Project Description
- Data Source:
- Type of analysis:

Please document the project the better you can.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for SERPgen in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/SERPgen`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "SERPgen"
git remote add origin git@github.com:{group}/SERPgen.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
SERPgen-run
```

# Install

Go to `https://github.com/{group}/SERPgen` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/SERPgen.git
cd SERPgen
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
SERPgen-run
```

some changes
