language: generic

env:
  - DOCKER_COMPOSE_VERSION=1.16.1

before_install:
  - sudo rm /usr/local/bin/docker-compose
  - curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > docker-compose
  - chmod +x docker-compose
  - sudo mv docker-compose /usr/local/bin
  - docker-compose up -d db
  - docker-compose build

before_script:
  - echo "Waiting for postgres.."; sleep 2;
  - docker-compose ps

script:
  - docker-compose run website ./manage.py test
