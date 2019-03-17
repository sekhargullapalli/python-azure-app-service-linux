# Python Apps for Azure App Service

Python web applications (Django, Flask apps etc.,) can be deployed to Azure app service on Linux using the cloud shell in azure portal or using a custom docker image. The Python extension for APP service on Windows is deprecated in favor of this method and is not recommended by Microsoft.

The following instruction are run in the cloud shell in my azure portal. 

The supported versions of Python can be listed using 

`az webapp list-runtimes –linux | grep PYTHON` 

![](/siteimages/pythonversions.jpg)

In the first step, create a directory and clone the repository from github. In case of a private repository, the user will be prompted to provide the user name and password. If your repository is in a different azure ad tenant (for example on your organization Azure devops), It works by providing a blank user name and a personal access token of your repository as password. 

![](/siteimages/gitclone.jpg)

The web application can now be deployed using the following command:

`az webapp up --name <appname>  --location <location> --subscription <subscriptionname>  --sku B1`

The locations for your subscriptions can be obtained using

`az account list-locations`

Note that free and shared SKUs are not available for apps running on Linux. The minimalistic tier than would be B1, which I used here. On the date of publishing, the B1 instance in west Europe costs around USD 39/ Month. 

![](/siteimages/deployment.jpg)

With this the site is up and running. The resource group of the application can be changed from the dashboard.

![](/siteimages/siteup.jpg)

The python version for the current app can be obtained by using the command:

`az webapp config show --resource-group <resource_group_name> --name <app_name> --query linuxFxVersion`

![](/siteimages/pythonversionapp.jpg)

A specific Python version can be set for the app service using the command:

`az webapp config set --resource-group <group_name> --name <app_name> --linux-fx-version "PYTHON|3.7"`

By default, the apps on run using Gunicorn WSGI HTTP server and has out of box support for Django and Flask applications. The app service looks for wsgi.py file in order to identify the project as a Django app or for files application.py or app.py for identifying the project as a Flask application.
