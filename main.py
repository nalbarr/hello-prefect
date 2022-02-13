from prefect import task, Flow, Parameter

@task(log_stdout=True)
def task1(name, x):
    print("task1: {0}, {1}".format(name, x))

def main():
    with Flow("flow 1") as flow:
        name = Parameter("name")
        x = Parameter("x")
        task1(name, x)

    flow.run(name="task1", x=123)
    flow.run(name="task2", x=345)

if __name__ == "__main__":
    main()
