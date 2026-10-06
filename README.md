# Ticket-Bench — Reproducible IT-Ticket Agent Benchmark

Python/FastAPI benchmark harness for password reset, VPN fault, and access-request tasks.
Includes deterministic grading, optional OpenAI API agent, Docker/PostgreSQL scaffold, pytest, and GitHub Actions.

Run: `pip install -r requirements.txt && uvicorn app.main:app --reload`
Test: `pytest -q`
Benchmark: `python -m app.benchmark --episodes 25`

The resume metrics supplied with the project are specification claims; this demo does not fabricate those results.
