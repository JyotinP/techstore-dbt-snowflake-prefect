from prefect import task, flow
from prefect.filesystems import GitHub
from prefect_dbt.cli.commands import trigger_dbt_cli_command
from prefect_dbt.cli.configs import SnowflakeTargetConfigs
import os
import shutil

# Load Blocks
snowflake_target_configs = SnowflakeTargetConfigs.load("snowflake-dbt-configs")
github_block = GitHub.load("dbt-github-repo")

# Add Steps
# Note: dbt triggers cannot be a @task, must be a @flow (sub-flow)

# clone the github repo into a temp directory
@task
def clone_dbt_repo():    
    shutil.rmtree("dbt_temp/", ignore_errors=True)
    github_block.get_directory(local_path="dbt_temp/")
    os.chdir("dbt_temp")

# run dbt command to build marts in prod
@flow
def run_dbt_build():
    try:
        trigger_dbt_cli_command("dbt build -s marts.* --target prod")
    except Exception as e:
        print(repr(e))

# delete the repo
@task
def delete_dbt_repo():
    os.chdir("..")
    shutil.rmtree("dbt_temp/", ignore_errors=True)

# Set Execution Order
@flow
def dbt_deploy_wrapper():
    clone_dbt_repo()
    run_dbt_build()
    delete_dbt_repo()

# Set the start function
if __name__ == "__main__":
    dbt_deploy_wrapper()