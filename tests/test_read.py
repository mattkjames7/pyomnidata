import pyomnidata
import numpy as np

def main():

    # quick test to check that we can read the data in, pick a year that is not this year!
    year = 1991
    try:
        data = pyomnidata.ReadOMNI(year,5)
    except:
        print("Failed to read data")
        raise RuntimeError

    assert isinstance(data,np.recarray), "Data should be np.recarray"

    assert data.size == 105120, "Incorrect size"

    return 0

if __name__ == "__main__":
    main()