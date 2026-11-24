PLATFORM="PC" # PC

try:
  import sys
except ImportError:
  # assume we are on casio if no sys module is available
  PLATFORM="CASIO"  # pyright: ignore[reportConstantRedefinition]
