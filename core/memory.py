# memory.py

import json
import os

MEMORY_FILE = "memory.json"


def load_memory():
    """Load saved memory."""
    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def save_memory(data):
    """Save memory."""
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def remember(key, value):
    """Store one value."""
    memory = load_memory()
    memory[key] = value
    save_memory(memory)


def recall(key, default=None):
    """Get a stored value."""
    memory = load_memory()
    return memory.get(key, default)


def forget(key):
    """Delete a stored value."""
    memory = load_memory()

    if key in memory:
        del memory[key]
        save_memory(memory)


def clear_memory():
    """Delete all memory."""
    save_memory({})