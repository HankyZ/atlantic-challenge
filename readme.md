## How to run
1. install docker
1. open terminal and cd to the project root folder
1. run the command `docker-compose run web python manage.py migrate && docker-compose up`

## Able to complete
1. create record with non-existing customer Id, subscription Id and gift Id
1. dockerization

## Unable to complete
1. update record with existing customer Id, subscription Id or gift Id
1. tests
1. irregularity detection and alerting