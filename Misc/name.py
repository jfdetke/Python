#!/usr/bin/env python3

def doit():
    print(f"DEBUG doit hello")
    print(f"__name__ is {__name__}")

def main():
    print(f"DEBUG main hello")
    print(f"__name__ is {__name__}")
    doit()

if __name__ == "__main__":
    print(f"DEBUG __main__ module")
    main()
