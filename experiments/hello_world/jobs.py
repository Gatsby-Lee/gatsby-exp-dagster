import dagster as dg


@dg.op
def hello_op():
    print("====> PRINT:: hello world")


@dg.job
def hello_job():
    hello_op()
