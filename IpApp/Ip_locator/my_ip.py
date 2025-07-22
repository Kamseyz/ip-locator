import argparse
import ipapi

def get_ip_location(ip_address=None):
    # if you dont pass any ip address is passed it will show yours
    data = ipapi.location(ip=ip_address, output='json')
    if data:
        print(f"IP Address: {data.get('ip')}")
        print(f"City: {data.get('city')}")
        print(f"Region: {data.get('region')}")
        print(f"Country: {data.get('country_name')}")
        print(f"Latitude: {data.get('latitude')}")
        print(f"Longitude: {data.get('longitude')}")
    else:
        print("Could not retrieve data. Check the IP address or your internet connection.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Locate an IP address using ipapi.")
    parser.add_argument('--ip', type=str, help='IP address to locate (leave empty to use your own IP)')
    args = parser.parse_args()

    get_ip_location(args.ip)

