import socket
import os
import requests

def get_ip_from_hostname(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror:
        return "Error: Could not resolve hostname"

def ping_ip(ip):
    response = os.system(f"ping -n 1 {ip}")
    
    if response == 0:
        return f"{ip} is online!"
    else:
        return f"{ip} is offline."

def reverse_dns_lookup(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return f"Invalid IP: {ip}"

    try:
        socket.setdefaulttimeout(3)
        domain = socket.gethostbyaddr(ip)
        return f"IP: {ip} → Domain: {domain[0]}"
    except socket.herror:
        return f"No PTR record found for {ip}"
    except socket.timeout:
        return f"DNS lookup timed out for {ip}"
    except Exception as e:
        return f"Error: {e}"

def check_service_port(ip, port):
    try:
        port = int(port)
        if not 0 <= port <= 65535:
            return "Port number must be between 0 and 65535"
            
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        
        result = s.connect_ex((ip, port))
        if result == 0:
            s.close()
            return f"Port {port} is open on {ip}"
        else:
            s.close()
            return f"Port {port} is closed on {ip}"
    except ValueError:
        return "Port must be a number"
    except socket.gaierror:
        return "Invalid IP address or hostname"
    except socket.error as e:
        return f"Connection error: {e}"

def ip_geolocation(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        
        if data.get("bogon"):
            return f"{ip} is a private/internal IP. Try a public IP."
        else:
            info = {
                'IP': data.get('ip'),
                'City': data.get('city'),
                'Region': data.get('region'),
                'Country': data.get('country'),
                'ISP': data.get('org')
            }
            return info
    except Exception as e:
        return f"Error: {e}"

def get_target_info(target):
    result = {}

    if not target.replace('.', '').isdigit():
        result['IP from Hostname'] = get_ip_from_hostname(target)

    else:
        result['Ping Result'] = ping_ip(target)
        result['Reverse DNS Lookup'] = reverse_dns_lookup(target)

        common_ports = [80, 443, 21, 22, 25, 53, 110]
        port_results = {}
        for port in common_ports:
            port_results[port] = check_service_port(target, port)
        result['Port Check'] = port_results

        result['IP Geolocation'] = ip_geolocation(target)
    
    return result

if __name__ == "__main__":
    target = input("Enter the target (hostname or IP): ")
    info = get_target_info(target)
    
    print("\nResult Summary:")
    for key, value in info.items():
        print(f"{key}: {value}")
