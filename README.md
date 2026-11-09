# HelloActions-JustinMehl

# Lab 11: Build Your First GitHub Actions Workflow

## Project Description

This project demonstrates how to create and execute a simple Python Hello World program using GitHub Actions.

The workflow automatically runs when code is pushed to the `main` branch. It can also be started manually through the GitHub Actions interface.

## Repository Structure

```text
HelloActions-YourName/
├── .github/
│   └── workflows/
│       └── hello.yml
├── hello.py
└── README.md
```

## Program Description

The Python program reads a name from an environment variable called `WHO_TO_GREET`. If the variable is unavailable, it uses a default value.

The program prints a greeting and a second message confirming that it is running inside GitHub Actions.

## Workflow Explanation

**1. What is the purpose of the `on` section?**

The `on` section specifies which events trigger the workflow. In this project, the workflow runs when code is pushed to the `main` branch or when manually started.

**2. What does `workflow_dispatch` do?**

`workflow_dispatch` allows a user to manually start the workflow from the GitHub Actions tab.

**3. What does `runs-on` specify?**

`runs-on` specifies the virtual machine environment used to execute the workflow. This project uses `ubuntu-latest`.

**4. Why is `actions/checkout` needed?**

`actions/checkout` downloads the repository files onto the virtual machine so the workflow can access and execute the Python program.

**5. What does the language setup action do?**

The `actions/setup-python` action configures Python on the virtual machine so that the Python program can run.

**6. What is the difference between compiling and running a program?**

Compiling converts source code into another executable form. Running executes the program. Python does not require a separate compilation step in this workflow because it can execute the Python source file directly.

**7. Where can you see the program output?**

The program output can be viewed in the GitHub Actions tab by opening a workflow run and expanding the Python program execution step.

**8. What is the difference between a workflow, a job, and a step?**

- A workflow is an automated process defined in a YAML file.
- A job is a group of steps that execute on a runner.
- A step is an individual task within a job, such as checking out the repository or running the Python program.

## Expected Output

```text
Hello GitHub Actions Student!
This program is running inside GitHub Actions.
```

## Execution Methods

This project supports two execution methods:

1. **Automatic execution:** The workflow runs whenever changes are pushed to the `main` branch.
2. **Manual execution:** The workflow can be started manually using the Run workflow option in the GitHub Actions tab.

## AI Usage Statement

AI assistance was used to write the Python program and prepare the project documentation. The project was reviewed and tested through GitHub Actions.
Actions workflow was done manually.
