# -*- coding: utf-8 -*-
"""01_add_many_number.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jhEGpEBRjagffORq9HujwEpf9d6iNMiU
"""

def add_numbers(numbers):
  total = 0
  for i in numbers:
    total += i
  return total


def main():
   numbers = [1, 2, 3, 4, 5]
   result = add_numbers(numbers)
   print(result)

if __name__ == '__main__':
    main()