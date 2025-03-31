import pyomnidata
import numpy as np


def get_date():

    try:
        data = pyomnidata.GetOMNI(1990,5)
    except:
        print("Failed to read data")
        raise RuntimeError
    
    assert isinstance(data,np.recarray), "Data should be np.recarray"

    assert data.size == 105120, f"Unexpected amount of data: {data.size}"

    assert all(data.Date // 10000 == 1990), "Unexpected date found"

    return 0

def get_date_range():

    try:
        data = pyomnidata.GetOMNI([1990,1992],5)
    except:
        print("Failed to read data")
        raise RuntimeError
    
    assert isinstance(data,np.recarray), "Data should be np.recarray"

    assert data.size == 315648, f"Unexpected amount of data: {data.size}"

    assert all((data.Date >= 19900101) & (data.Date <= 19921231)), "Unexpected date found"

    return 0


def main():

    get_date()
    get_date_range()
    return 0

if __name__ == "__main__":
    main()