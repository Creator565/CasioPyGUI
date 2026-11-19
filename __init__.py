PLATFORM="PC" # PC

try:
  import sys
except ModuleNotFoundError:
  # assume we are on casio if no sys module is available
  PLATFORM="CASIO"  # pyright: ignore[reportConstantRedefinition]
