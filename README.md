# cybersecurity-projects

****Network Information Gathering Script***

**Description**

This script is designed to provide various network-related functionalities, including obtaining IP addresses from hostnames, pinging IP addresses, performing reverse DNS lookups, checking open ports for services, and retrieving geolocation information for a given IP address. The script is useful for network administrators, penetration testers, or anyone looking to quickly gather information about a target host or IP.

**Features**
**Get IP from Hostname:** Resolves a hostname to an IP address.

**Ping IP**: Checks if an IP address is reachable over the network by sending a ping request.

**Reverse DNS Lookup:** Performs a reverse DNS lookup on an IP address to find its domain name.

**Service Port Check:** Checks if a specific port is open on a given IP address, useful for identifying accessible services.

**IP Geolocation:** Provides geolocation information (City, Region, Country, ISP) for a given IP address.

**Requirements**

Before running the script, make sure you have Python 3.x installed along with the necessary dependencies.

Required Libraries
requests: For making HTTP requests to the ipinfo.io API for geolocation.

You can install the required library using pip:

bash

Copy

Edit

pip install requests
Installation
Clone or download the repository to your local machine.

Ensure you have Python 3.x installed.

Install the required dependencies by running:

bash

Copy

Edit

pip install requests
Place the script in a directory of your choice.

Usage
Running the Script
To run the script, open a terminal or command prompt, navigate to the directory containing the script, and run the following command:

bash

Copy

Edit

python network_info_gathering.py

**Interaction**

When the script is executed, it will prompt you to enter a target (either a hostname or an IP address). Based on your input, the script will perform the following actions:

**IP from Hostname:** If you enter a hostname, it will resolve and display the corresponding IP address.

**Ping IP:** If you enter an IP address, it will check if the IP is reachable.

**Reverse DNS Lookup:** For IP addresses, it will attempt to find the corresponding domain name.

**Port Check:** The script will check several common ports (like HTTP, HTTPS, FTP, etc.) on the given IP address.

**Geolocation:** The script will fetch geolocation details such as city, region, country, and ISP for the IP address.

Example Output
bash
Copy
Edit
Enter the target (hostname or IP): example.com

**Result Summary:**

IP from Hostname: 93.184.216.34

Ping Result: 93.184.216.34 is online!

Reverse DNS Lookup: IP: 93.184.216.34 → Domain: example.com

Port Check: {80: 'Port 80 is open on 93.184.216.34', 443: 'Port 443 is open on 93.184.216.34', 21: 'Port 21 is closed on 93.184.216.34', ...}

IP Geolocation: {'IP': '93.184.216.34', 'City': 'Los Angeles', 'Region': 'California', 'Country': 'US', 'ISP': 'AS15133 Cloudflare, Inc.'}

**Supported Functions**
Get IP from Hostname: get_ip_from_hostname(hostname)

Ping IP: ping_ip(ip)

Reverse DNS Lookup: reverse_dns_lookup(ip)

Service Port Check: check_service_port(ip, port)

IP Geolocation: ip_geolocation(ip)

Target Info Gathering: get_target_info(target)

**Contributing**

Feel free to fork the repository and contribute by submitting pull requests. Contributions are welcome to improve the functionality of the script, add new features, or improve documentation.

**License**

This script is open-source and available under the MIT License.
