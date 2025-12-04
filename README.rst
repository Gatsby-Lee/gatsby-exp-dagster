Gatsby EXP Dagster
==================

How to setup and Run Hello-World
--------------------------------

.. code-block:: bash

    ## install uv if not available
    brew install uv

    ## Clone repo
    git clone https://github.com/Gatsby-Lee/gatsby-exp-dagster.git

    ## Intstall dependecies
    uv sync

    ## Enable venv
    source .venv/bin/activate

    ## Run locally - CLI approach
    dagster job execute -f experiments/hello_world/defs.py -j hello_job
    # the run_config will help supress the Dagster Event logs
    dagster job execute -f experiments/exp_retry_policy/defs.py -j hello_job -c run_config.yaml


What I did to initialize this Project on my mac
------------------------------------------------

.. code-block:: bash

    ## this will create pyproject.toml
    brew install uv

    ## add dependencies
    # .venv will be created automatically if not exists.
    uv add dagster
    uv add dagster-webserver
