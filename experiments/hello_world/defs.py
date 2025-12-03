import dagster as dg

from experiments.hello_world.jobs import hello_job

defs = dg.Definitions(jobs=[hello_job])

# ==
# dagster job execute -f experiments/hello_world/defs.py -j hello_job
