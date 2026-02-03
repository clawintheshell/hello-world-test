#!/usr/bin/env python3
"""
Hello World Python Script
A simple demonstration script for the test repository.
"""

def main():
    """Print a friendly greeting."""
    print("Hello, World! 👋")
    print("This is a test repository created by MegaPonzuClaw.")
    print("Repository: https://github.com/clawintheshell/hello-world-test")
    
    # Get some system info
    import platform
    import datetime
    
    print(f"\nSystem Information:")
    print(f"  Python: {platform.python_version()}")
    print(f"  System: {platform.system()} {platform.release()}")
    print(f"  Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")

if __name__ == "__main__":
    main()
