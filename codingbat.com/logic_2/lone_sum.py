#!/usr/bin/env python3

def lone_sum(a, b, c):
  if a == b:
    if b == c:
      return 0
    else:
      return c
  else:
    if a == c:
      return b
    elif b == c:
      return a
    else:
      return a + b + c

def main():
    """Test function"""
    print (lone_sum(1, 2, 3))

if __name__ == '__main__':
    main()