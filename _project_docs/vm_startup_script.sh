#! /bin/bash

# Install git & pip
sudo apt-get update -y
sudo apt-get install git -y
sudo apt install python3-pip -y

# Install dbt 
pip3 install dbt-snowflake

# Install Prefect Dependencies
pip3 install prefect
pip3 install prefect-shell
pip3 install prefect-dbt
pip3 install "prefect-dbt[cli]"
pip3 install prefect-github
pip3 install prefect-snowflake
pip3 install s3fs

# Set Environment Variables
export DBT_PROFILES_DIR=.
export DBT_USER= <DBT_USER>
export DBT_PASSWORD= <DBT_PASSWORD>


# Authenticate Prefect Cloud & Start Agent
prefect cloud login -k <auth_key>
prefect agent start -q 'ec2-prefect-vm'