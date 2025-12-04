import random

import dagster as dg
from dagster import RetryPolicy, op

MAX_RETRIES = 1
MAX_ATTEMPTS = 1 + MAX_RETRIES  # initial attempt + retries


@dg.op(
    retry_policy=dg.RetryPolicy(
        max_retries=MAX_RETRIES,
        delay=1,  # 1-second wait between retries
    )
)
def hello_op(context: dg.OpExecutionContext):
    num_attempt = context.retry_number + 1  # 0 = first try, 1 = first retry, ...
    print(
        f"====> hello_op: running... (attempt={num_attempt} / MAX_ATTEMPTS={MAX_ATTEMPTS})"
    )

    # Randomly fail 50% of the time
    if random.random() < 0.5:
        print("====> hello_op: simulated failure")
        raise Exception("====> Random failure for retry test")

    print("====> hello_op: success")


@dg.job
def hello_job():
    hello_op()
