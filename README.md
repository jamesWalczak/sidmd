# SIDMD

Automated code generation.

> [!IMPORTANT]\
> This is a **template** repository. To use its functionalities, use this template to create own repository.

## Connecting an LLM

The system is designed to enable connecting different kinds of Large Language Models. To successfully connect an LLM, the following actions need to be taken:
  - The file `.sidmd/generate_code.py` should be updated with implementation-specific connection and request details.
  - If the LLM usage requires installing specific Python libraries, they should be listed in `.sidmd/install_dependencies.sh`.
  - For security reasons, if an API token is necessary, it should be defined under a name `AI_API_KEY` in repository's secrets (`Settings`>`Secrets and variabless`>`Actions`>`Secrets`).

## Using the system

1. Start by choosing a suitable issue template:
    - **`Initiation`** — for creating initial file structure.
    - **`Feature`** — for implementing a new feature.
    - **`Bug`** — for fixing a bug.
2. Wait for the AI to finish generating code. This will be confirmed by a comment under the issue, together with a link to a branch where the change was made.
3. Follow the link to review changes made on a branch. If any problems arises or there is a need to further modify the code, indicate the expected changes by a comment under the original issue. Repeat the process until the results are satisfactory.
4. When the result meets expectations, close the issue. This will trigger an automatic creation of a pull request to the main branch.
