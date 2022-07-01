# SERPgen - an NLP-based search results text generator
This project uses natural language processing to generate SEQ (Search Engine Query) content from keywords.

The cost of writing Search Engine Result Page descriptions (title and snippet) is high for business owners. Such descriptions enable products and services to appear in searches and to generate leads.
Because of the tedious process of creating individual descriptions for each product, Search Engine Optimization professionals can focus more on other important tasks.


Using trained NLP models that are fed search results for similar products, SERPgenTM automatically generates search engine result title and description based on keywords such as company name + product name + attributes.

<img src="UI/serpgen_g.png" width="500"/>

For more information please check the following presentation. <br />
*[An NLP-based search results text generator](https://docs.google.com/presentation/d/1Vy21neAeTntBbcdmtyPCD2LMBnt8zpptBZHT6jL59mw/edit?usp=sharing)*



## Model:
SERPgen is based on T5 model.

You can access the online site by clicking the following link

https://serpv1.herokuapp.com/

# Deploy the entire user interface on your own
To deploy the model, we need two different steps.
1) Upload the api (docker file) on GCP to use the prediction of model
2) Upload the UI to Heroku of GCP to use the api.


## How to deploy the API on Google Cloud
First, log in to Google Cloud
```bash
gcloud auth login
gcloud auth list
```

Then export the image by replacing the project id and docker image name. And build the image

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

After a successful depoyment, save the generated link of your API website.
Replace the link of api in the function *key_to_text* in the file *UI/serp_backend.py*

## How to deploy the UI to Heroku and GCP
### How to deply the UI to Heroku
To depoly the UI on the heroku, create a user name on heroku website and using the following command login into it.
```bash
heroku login
```

use the following command to create the project and push it to heroku, after modifying *UI_NAME*.
```bash
export UI_NAME=serpv2
echo $UI_NAME
heroku create ${UI_NAME}

git push heroku main:main
heroku ps:scale web=1
```

### How to deply the UI to GCP
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
