# Algorithm-Visualizer-Time-Series-Simulation-FastAPI-Backend
I built this collection of small Python projects on my own to brush up on basic CS concepts while practicing software development. I split everything into three separate folders so each part stays clean and independent.

## Algorithm-Visualizer
I coded animated visualizations for bubble sort and Dijkstra’s shortest path algorithm here. Watching each step animate made it way easier for me to follow how sorting and graph traversal update values step by step.

## Time-Series-Simulation
This is a custom framework I put together to work with sequential datasets. It has functions to calculate core metrics, run rule-based simulation logic, evaluate outcomes, and draw charts to visualize results. I split each feature into separate modules so I can add new calculation rules later without breaking old code.

## FastAPI-Service
A simple lightweight backend I built using FastAPI. I set up basic data processing pipelines and exposed REST endpoints to handle data lookups and batch calculation jobs.

## How to set up the environment
All packages needed for every module are listed in one requirements file. Open your terminal and run this line to install everything at once:
```bash
pip install -r requirements.txt
