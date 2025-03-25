import pyomnidata
import numpy as np


def get_date():

    try:
        data = pyomnidata.GetOMNI(2010,5)
    except:
        print("Failed to read data")
        raise RuntimeError
    
    assert isinstance(data,np.recarray), "Data should be np.recarray"

    assert data.size == 105120, f"Unexpected amount of data: {data.size}"

    assert all(data.Date // 10000 == 2010), "Unexpected date found"

    return 0

def get_date_range():

    try:
        data = pyomnidata.GetOMNI([2010,2013],5)
    except:
        print("Failed to read data")
        raise RuntimeError
    
    assert isinstance(data,np.recarray), "Data should be np.recarray"

    assert data.size == 420768, f"Unexpected amount of data: {data.size}"

    assert all((data.Date >= 20100101) & (data.Date <= 20131231)), "Unexpected date found"

    return 0


def main():

    get_date()
    get_date_range()
    return 0

if __name__ == "__main__":
    main()