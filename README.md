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

remember that use the following command to update the main branch every morning.
```bash
pip pull origin main
```
if you use the above command where you are in your selected branch, all data from remote main branch will merge into your selected branch.
In case of any conflicts, you see some conflicts massages.


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
git merge main
```

now you can switch to master branch again. (It seems our main branch name is not master!!!)
```bash
git checkout main
```

# How to deploy the api to google cloud
For the first access login to google cloud
```bash
gcloud auth login
gcloud auth list
```

First replace the project id and docker image name and export it. And build the image

```bash
export PROJECT_ID=wagon-bootcamp-351218
echo $PROJECT_ID
gcloud config set project $PROJECT_ID

export DOCKER_IMAGE_NAME=api-serpgen-v1
echo $DOCKER_IMAGE_NAME

docker build -t eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME .
```

After a successful built you can push and deploy the image
```bash
docker push eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME
gcloud run deploy --image eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME \
  --platform managed --region europe-west1 \
  --memory 8000M --cpu 2 --allow-unauthenticated
```

Save the generated url  in a safe place.

# How to deploy the UI to Heroku and GCP
## How to deply the UI to Heroku
To depoly the UI on the heroku, create a user name on heroku website and using the following command login into it.
```bash
heroku login
```

use the following command to create the project and push it to heroku, after modifying *UI_NAME*.
```bash
export UI_NAME=serpv2
echo $UI_NAME
heroku create ${APP_NAME}

git push heroku main:main
heroku ps:scale web=1
```

After a successful depoyment, save the generated line of your UI website.

## How to deply the UI to GCP
To depoly the UI on the GCP, create a user name on GCP and using the following command login into it.
```bash
gcloud auth list
gcloud auth login

gcloud auth configure-docker
```

To use gcp for deploying the UI, we need a Docker container.
In the follwoing command, moddify the *PROJECT_ID* and *DOCKER_IMAGE_NAME*. Then using the *Dockerfile_ui*, build the docker container.

```bash
export PROJECT_ID=wagon-bootcamp-351218
echo $PROJECT_ID
gcloud config set project $PROJECT_ID

export DOCKER_IMAGE_NAME=api-serpgen-ui
echo $DOCKER_IMAGE_NAME

docker build  -f Dockerfile_ui -t eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME .
```

After a successful building, you are able to push and deploy the container to GCP.
```bash
docker push eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME
gcloud run deploy --image eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME \
   --platform managed --region europe-west1 \
   --memory 700M --allow-unauthenticated
```

After a successful depoyment, save the generated line of your UI website.
