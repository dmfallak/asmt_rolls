#!/usr/bin/python3

import re
import sys

def output(parcel_id, parcel_address, city, owner_name, owner_address, property_class, school_district, parcel_size, grid_coord_east, grid_coord_north, deed_book, market_value, county_tax, city_tax, school_tax, year_built):
    print(f'{parcel_id}\t{parcel_address}\t{city}\t{owner_name}\t{owner_address}\t{property_class}\t{school_district}\t{parcel_size}\t{grid_coord_east}\t{grid_coord_north}\t{deed_book}\t{market_value}\t{county_tax}\t{city_tax}\t{school_tax}\t{year_built}')

def main():
    parcel_id = ""
    parcel_address = ""
    city = "Mount Vernon"
    owner_name = ""
    owner_address = ""
    property_class = ""
    school_district = "MT VERNONCENTRAL"
    parcel_size = "0"
    grid_coord_east = "0"
    grid_coord_north = "0"
    deed_book = ""
    market_value = "0"
    county_tax = "0"
    city_tax = "0"
    school_tax = "0"
    year_built = "0"

    in_parcel = False
    address_next = False
    property_class_next = False
    owner_next = False
    owner_lines = []

    for line in sys.stdin:
        if "***" in line:
            if in_parcel:
                output(parcel_id, parcel_address, city, owner_name, owner_address, property_class, school_district, parcel_size, grid_coord_east, grid_coord_north, deed_book, market_value, county_tax, city_tax, school_tax, year_built)
                parcel_id = ""
                parcel_address = ""
                owner_name = ""
                owner_address = ""
                property_class = ""
                deed_book = ""
                parcel_size = "0"
                grid_coord_east = "0"
                grid_coord_north = "0"
                market_value = "0"
                county_tax = "0"
                city_tax = "0"
                school_tax = "0"
                year_built = "0"

                owner_lines = []
            if "-" in line:
                in_parcel = True
                x = re.search("\S+-\S+-\S+", line)
                if x:
                    parcel_id = x.group()
                    address_next = True
                    continue
            else:
                in_parcel = False
        elif address_next:
            parcel_address = line[0:75].strip()
            address_next = False
            property_class_next = True
        elif property_class_next:
            property_class = line[27:70].strip()
            property_class_next = False
            owner_next = True
        elif owner_next:
            if line[:5] == "     ":
                owner_next = False
                owner_name = ", ".join(owner_lines[:-2])
                owner_address = ", ".join(owner_lines[-2:])
            else:
                owner_lines.append(line[:27].strip())

        
        if "FULL MKT VAL" in line:
            market_value = line[line.index("FULL MKT VAL") + 12:].strip().split(" ")[0].replace(",", "") or "0"

        if "COUNTY TAXABLE" in line:
            county_tax = line[line.index("COUNTY TAXABLE") + 14:].strip().split(" ")[0].replace(",", "") or "0"

        if "CITY TAXABLE" in line:
            city_tax = line[line.index("CITY TAXABLE") + 12:].strip().split(" ")[0].replace(",", "") or "0"

        if "SCHOOL TAXABLE" in line:
            school_tax = line[line.index("SCHOOL TAXABLE") + 14:].strip().split(" ")[0].replace(",", "") or "0"

        #if "Built:" in line:
        #    year_built = line[line.index("Built:") + 7:][:4].strip() or "0"

        if "ACREAGE" in line:
            parcel_size = line[line.index("ACREAGE") + 7:].strip().split(" ")[0] or "0"
        
        if "EAST " in line:
            grid_coord_east = line[line.index("EAST ") + 5:][:6].strip() or "0"
        
        if "NRTH " in line:
            grid_coord_north = line[line.index("NRTH ") + 5:][:6].strip() or "0"
        
        if "DEED BOOK" in line:
            deed_book = line[line.index("DEED BOOK") + 9:].strip().split(" ")
            deed_book = deed_book[0] + " " + deed_book[1]


if __name__ == "__main__":
    main()
