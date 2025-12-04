from dagster import Definitions

from experiments.exp_retry_policy.jobs import hello_job

defs = Definitions(
    jobs=[hello_job],
)
