# Python Async Comprehension Project

## Project Overview

This project focuses on Python's asynchronous features, specifically using `async` and `await` keywords. It covers generating asynchronous values, using async comprehensions, and measuring runtime with `asyncio.gather`.

## Project Structure

- `0-async_generator.py`: Defines a coroutine `async_generator` that yields a random number between 0 and 10, ten times.
- `0-main.py`: Tests the `async_generator` coroutine.
- `1-async_comprehension.py`: Defines a coroutine `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator`.
- `1-main.py`: Tests the `async_comprehension` coroutine.
- `2-measure_runtime.py`: Defines a coroutine `measure_runtime` that measures the total runtime of executing `async_comprehension` four times in parallel.
- `2-main.py`: Tests the `measure_runtime` coroutine.

## How to Run

1. **Task 0: Async Generator**
   ```bash
   chmod +x 0-main.py
   ./0-main.py

