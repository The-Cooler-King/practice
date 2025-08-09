from datetime import datetime
import timeit
import random
import heapq

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from heap import Heap

# Store all printed outputs for optional markdown export
markdown_sections = []


def print_and_capture(section_title, header, rows):
    """Prints the section to console and stores it for markdown output."""
    # --- Console output ---
    print(section_title)
    print(header)
    print("-" * len(header))
    for row in rows:
        print(row)
    print("")

    # --- Markdown output ---
    # Split header into clean cells
    header_cells = [cell.strip() for cell in header.split("|") if cell.strip()]
    md = [f"## {section_title}", ""]

    # Header row
    md.append("| " + " | ".join(header_cells) + " |")
    # Separator row
    md.append("| " + " | ".join(["---"] * len(header_cells)) + " |")
    # Data rows
    for r in rows:
        cells = [cell.strip() for cell in r.split("|") if cell.strip()]
        md.append("| " + " | ".join(cells) + " |")

    markdown_sections.append("\n".join(md))


# Sizes to test
sizes = [100, 1000, 10000, 100000, 1000000, 10000000]

# Heapify Benchmark
rows = []
section_title = "Heapify"
header = f"{'Size':>8} | {'Heap Time (s)':>15} | {'heapq Time (s)':>15} | {'Multiplier':>15}"

for n in sizes:
    # Setup for Heap
    setup_myheap = f'''
from heap import Heap
import random
data = [random.randint(1, 1000000) for _ in range({n})]
'''

    stmt_myheap = f'''
heap = Heap(data=data)
'''

    # Setup for heapq
    setup_heapq = f'''
import heapq
import random
heap = [random.randint(1, 1000000) for _ in range({n})]
'''

    stmt_heapq = f'''
heapq.heapify(heap)
'''

    time_myheap = timeit.timeit(stmt_myheap, setup=setup_myheap, number=1)
    time_heapq = timeit.timeit(stmt_heapq, setup=setup_heapq, number=1)

    rows.append(f"{n:>8} | {time_myheap:>15.6f} | {time_heapq:>15.6f} | {time_myheap / time_heapq:>15.1f}")

print_and_capture(section_title=section_title,
                  header=header,
                  rows=rows
                  )

# Heap Peek Benchmark
rows = []
section_title = "Heap Peek"

for n in sizes:
    # Setup for MyHeap
    setup_myheap = f'''
from heap import Heap
import random
heap = Heap(data=[1,8,3,7,10])
'''

    stmt_myheap = f'''
for _ in range({n}):
    root = heap.peek()
'''

    # Setup for heapq
    setup_heapq = f'''
import heapq
import random
heap = [1,8,3,7,10]
heapq.heapify(heap)
'''

    stmt_heapq = f'''
for _ in range({n}):
    root = heap[0]
'''

    time_myheap = timeit.timeit(stmt_myheap, setup=setup_myheap, number=1)
    time_heapq = timeit.timeit(stmt_heapq, setup=setup_heapq, number=1)

    rows.append(f"{n:>8} | {time_myheap:>15.6f} | {time_heapq:>15.6f} | {time_myheap / time_heapq:>15.1f}")

print_and_capture(section_title=section_title,
                  header=header,
                  rows=rows
                  )

# Heap Push Benchmark
rows = []
section_title = "Heap Push"

for n in sizes:
    # Setup for MyHeap
    setup_myheap = f'''
from heap import Heap
import random
heap = Heap()
data = [random.randint(1, 1000000) for _ in range({n})]
'''

    stmt_myheap = '''
for x in data:
    heap.push(x)
'''

    # Setup for heapq
    setup_heapq = f'''
import heapq
import random
heap = []
data = [random.randint(1, 1000000) for _ in range({n})]
'''

    stmt_heapq = '''
for x in data:
    heapq.heappush(heap, x)
'''

    time_myheap = timeit.timeit(stmt_myheap, setup=setup_myheap, number=1)
    time_heapq = timeit.timeit(stmt_heapq, setup=setup_heapq, number=1)

    rows.append(f"{n:>8} | {time_myheap:>15.6f} | {time_heapq:>15.6f} | {time_myheap / time_heapq:>15.1f}")

print_and_capture(section_title=section_title,
                  header=header,
                  rows=rows
                  )

# Heap Pop Benchmark
rows = []
section_title = "Heap Pop"

for n in sizes:
    # Setup for MyHeap
    setup_myheap = f'''
from heap import Heap
import random
data = [random.randint(1, 1000000) for _ in range({n})]
heap = Heap(data=data)
'''

    stmt_myheap = f'''
for _ in range({n}):
    heap.pop()
'''

    # Setup for heapq
    setup_heapq = f'''
import heapq
import random
heap = [random.randint(1, 1000000) for _ in range({n})]
heapq.heapify(heap)
'''

    stmt_heapq = f'''
for _ in range({n}):
    heapq.heappop(heap)
'''

    time_myheap = timeit.timeit(stmt_myheap, setup=setup_myheap, number=1)
    time_heapq = timeit.timeit(stmt_heapq, setup=setup_heapq, number=1)

    rows.append(f"{n:>8} | {time_myheap:>15.6f} | {time_heapq:>15.6f} | {time_myheap / time_heapq:>15.1f}")

print_and_capture(section_title=section_title,
                  header=header,
                  rows=rows
                  )

update = input("Would you like to update benchmarks.md? (y/n): ").strip().lower()
if update == "y":
    filename = os.path.join(os.path.dirname(__file__), "benchmarks.md")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n# Benchmark Results — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for section in markdown_sections:
            f.write(section + "\n\n")
    print(f"Benchmarks appended to {filename}")
