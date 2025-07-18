# Heap Data Structure in Python
This project implements a **min-heap** in Python, starting with a basic class structure and gradually building functionality via development tickets.

## Features
- Min-heap implementation using a Python list as the internal data container.
- Simple, testable structure with iterative enhancements.

## Getting Started

### Installation
No installation required. Just clone the repo and run with Python 3.

```bash
git clone https://github.com/The-Cooler-King/practice.git
cd practice/heap
```

### Usage
You can run the class directly:

```python
from heap import Heap

heap = Heap()
print(heap._data)  # []
```

## Development Plan
1. ✅ Initialize the Heap class with an empty internal container.
2. ✅ Add basic heap operations (push, pop, peek, etc.).
3. ✅ Add internal helper methods (e.g., _heapify_up, _heapify_down).
4. ⏳ Add support for max-heap toggle
5. ⏳ Benchmark against heapq

## Documentation
See [heap.md](heap.md) for in-depth documentation.