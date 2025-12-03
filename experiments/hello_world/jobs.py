import dagster as dg


@dg.op
def hello_op():
    print("hello world")


@dg.job
def hello_job():
    hello_op()
