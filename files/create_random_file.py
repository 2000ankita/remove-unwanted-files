import os
import random
import string

def generate_random_filename():
    """Generate a random filename."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.txt'

def create_random_file():
    """Create a random file with random content."""
    filename = generate_random_filename()
    content = ''.join(random.choices(string.ascii_letters + string.digits, k=100))  # Random content
    with open(os.path.join(os.getcwd(), filename), 'w') as f:  # Ensure it's in the current directory (repo root)
        f.write(content)
    print(f"Random file created: {filename}")

create_random_file()
