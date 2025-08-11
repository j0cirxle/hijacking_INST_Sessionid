from string import Template
import os

def create_server(ip,port, template_path='server_template.py.tpl', output_path='server.py'):
    with open(template_path, 'r') as f:
        src = Template(f.read())
    result = src.substitute(ip=ip,port=port,ip_i = ip)
    with open(output_path, 'w') as f:
        f.write(result)
    print(f"Generated {output_path} with IP {ip}\n")
    print(f"Generated {output_path} with Port {port}\n")
    f.close()

def create_client(ip,port, template_path='client_template.py.tpl', output_path='client.py'):
    with open(template_path, 'r',encoding="utf-8") as f:
        src = Template(f.read())
    result = src.substitute(ip=ip,port=port)
    with open(output_path, 'w',encoding="utf-8") as f:
        f.write(result)
    print(f"Generated {output_path} with IP {ip}\n")
    print(f"Generated {output_path} with Port {port}")
    f.close()
    
if __name__ == "__main__":
    ip = input("Enter IP: ")
    port = int(input("Enter Port:"))
    
    create_server(ip,port)
    create_client(ip,port)
