# ForgeShift

AI-powered daily operations planner for retail professionals that improves over time through real usage feedback.

## Problem & Motivation
Retail professionals operate in fast-paced, constantly shifting environments where priorities change throughout the day. An unexpected truck, staffing gaps, backroom issues, claims, and customer needs can all force rapid replanning. Creating and maintaining an effective daily plan under these conditions is time-consuming and mentally taxing.

Effective daily planning directly impacts execution quality. The less time spent figuring out what to do and when, the more time is available for actually leading the team and getting work done.

While general-purpose LLMs like ChatGPT or Claude can generate plans from a prompt, they lack persistent memory of an individual’s or store’s specific patterns. Every interaction starts from scratch. ForgeShift is designed to remember context across shifts and improve its time estimates by learning from actual task durations logged by the user. This creates a tool that gets more useful the more it is used in a specific retail environment.

## Goals & Approach

The goal of ForgeShift is to empower retail professionals with a tool that helps them plan and adapt their day more quickly and accurately, freeing up more time to focus on execution and serving customers. At the same time, this project serves as an opportunity for me to develop practical full-stack and LLM engineering skills.

The project will be delivered in two stages to manage scope effectively:

**Stage 1 (MVP):** A fully functional CLI application that can generate time-blocked daily plans, handle mid-day updates, and improve time estimates based on logged actual durations.
**Stage 2:** A web application (using React) that provides the same core functionality through a user-friendly interface suitable for daily use in a retail environment.

A key architectural decision is to keep all scheduling and duration-estimation logic inside dedicated Python modules, separate from the CLI. This allows the same core logic to be reused without changes when we later add a React frontend.

## Tech Stack

- **Python** - Primary programming language for the entire backend and core logic.
- **FastAPI** - Modern backend framework used to build the API layer.
- **Pydantic** - Used to define and validate all data structures throughout the application.
- **Instructor** - Library that enables reliable structured output from the LLM using Pydantic models.
- **Ollama** - Runs LLMs locally during development (free and private).
- **SQLite** - Lightweight database used to store plans and user feedback for learning.
- **Typer** - Used to create a clean, professional command-line interface.

## Architecture

ForgeShift is designed with a clear separation between the core business logic and the user interface. This allows the planning and time-estimation intelligence to remain independent regardless of if it's being accessed by a CLI or future web frontend.    

### Main Components 

- **Core Logic** (`core/`): Contains all scheduling/prioritization and duration-estimation logic. This is the "brain" of the app and is written in plain Python modules.
- **Interface** (`cli/`): The command-line interface that users interact with in Stage 1. It calls into the Core Logic.
- **Data Layer**: Uses Pydantic models for all data structures and SQLite to persist plans and feedback.
- **LLM Integration**: Uses the Instructor library to communicate with Ollama for generating plans and improving estimates over time.

Data flows from the user -> CLI -> Core Logic -> LLM (through Instructor) -> back through the Core Logic -> stored in SQLite -> returned to the user.

## Getting Started
Coming soon.