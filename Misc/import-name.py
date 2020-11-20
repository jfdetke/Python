#!/usr/bin/env python3
import name

def main():
    print(f"DEBUG main hello")
    print(__name__)
    print("Calling name.doit:")
    name.doit()

if __name__ == "__main__":
    print(f"DEBUG __main__ module")
    main()
