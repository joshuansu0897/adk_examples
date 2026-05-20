# Custom Service

It's the most simple multi-agent example.

## How to set up

```bash
# Create your .env file (use the .env.example as a template)
cp .env.example .env

```

## How to run locally

this will be executed in the `root` of the repository, not in the customer_service directory
you need to active the `.venv` in the `root` of the repository before running the agent


### Step 1: Create and activate a virtual environment
```bash
python3 -m venv .venv

# CMD
.venv\Scripts\activate.bat

# Bash
source .venv/bin/activate

# PowerShell
.venv\Scripts\Activate.ps1
```

### Step 2: Install dependencies
```bash
pip install google-adk
pip install google-adk
```

### Step 3: Run the customer service agent
```bash
adk web
```
