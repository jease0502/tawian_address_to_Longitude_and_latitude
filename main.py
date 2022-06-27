from address_scripy import Address_scripy
from csv_to_data import CsvToData


if __name__ == '__main__':
    address_scripy = Address_scripy()
    Factory_addr = CsvToData.get_data_address(
        "工廠地址", CsvToData.read_data("data.csv"))

    address_longitude = []
    address_latitude = []
    with open("error.txt", "w") as f:
        for i in Factory_addr:
            try:
                lat, log = address_scripy.get_address(i)
                address_longitude.append(log)
                address_latitude.append(lat)
                address_scripy.quiz_browser()
                print(i, lat, log)
    except:
        f.write(str(i) + "\n")
