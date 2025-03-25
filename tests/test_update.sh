#!/bin/bash

# Update OMNI data
python -c "import pyomnidata; pyomnidata.UpdateLocalData()"
if [ $? -ne 0 ]; then
  echo "UpdateLocalData() failed, exiting."
  exit 1
fi

echo "UpdateLocalData() succeeded."


# Check if there are files in $HOME/omnidata/5
# This is obviously not foolproof, but better than nothing
if [ -z "$(ls -A "$HOME/omnidata/5" 2>/dev/null)" ]; then
  echo "No files found in $HOME/omnidata/5. Exiting."
  exit 1
fi

echo "Files found in $HOME/omnidata/5."


# Check if there are files in $HOME/omnidata/1
# This is obviously not foolproof, but better than nothing
if [ -z "$(ls -A "$HOME/omnidata/1" 2>/dev/null)" ]; then
  echo "No files found in $HOME/omnidata/1. Exiting."
  exit 1
fi

echo "Files found in $HOME/omnidata/1."

# Update solar flux data
python -c "import pyomnidata; pyomnidata.UpdateSolarFlux()"
if [ $? -ne 0 ]; then
  echo "UpdateSolarFlux() failed, exiting."
  exit 1
fi

echo "UpdateSolarFlux() succeeded."

if [ ! -f "$HOME/omnidata/F107.bin" ]; then 
  echo "F107 file missing"
  exit 1
fi
echo "Found F107 File"