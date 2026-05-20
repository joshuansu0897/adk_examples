# ADK

this repository contains examples of Agent Deployment Kit (ADK) implementations/projects.

## Getting Started
To get started with ADK, you can follow these steps:
1. Install Python
    ```
    used:
    - pyenv 2.6.26
    - Python 3.14.3
    - pip 25.3
    - uv 0.11.3
    ```

# How to Create a New ADK Projects
1. Create a **new directory** for your project and **navigate to it**.
2. Initialize a new Python project using `uv`:
    ```bash
    uv init
    ```
3. Install the ADK packages:
    ```bash
    uv add google-adk
    uv add google-cloud-resource-manager
    ```
4. Activate the virtual environment:
    ```bash
    # For Unix/Linux/MacOS
    source .venv/bin/activate

    # For Windows
    .venv/Scripts/activate
    .venv\\Scripts\\activate
    ```
5. Create your agent implementation by following the ADK documentation and examples provided in this repository.
    ```bash
    adk create agent
    ```
6. To execute/test your agent, use the following command:
    ```bash
    adk web
    ```

## Examples
- `travel_planner`: A simple travel planner agent that helps users plan their trips. **_(single-agent example)_**
- `customer_service`: A customer service agent that can handle common customer inquiries and provide support. **_(multi-agent example)_**

