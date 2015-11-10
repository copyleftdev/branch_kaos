from faker import Factory
import subprocess

fake = Factory.create()


def git(*args):
    return subprocess.call(['git'] + list(args))


def create_branch(branch_name):
    git("checkout","-b",branch_name)


def main():

    for i in range(1,500000):
        create_branch("branch_test{}".format(i))

if __name__ == "__main__":
    main()
