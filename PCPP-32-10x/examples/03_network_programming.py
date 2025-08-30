#!/usr/bin/env python3
"""
Network Programming Examples
PCPP Certification Study Material

This module demonstrates network programming concepts including:
- Socket programming (TCP/UDP)
- HTTP clients and servers
- Async networking with asyncio
- RESTful API clients
- WebSocket communication
- Email handling
"""

import socket
import threading
import asyncio
import aiohttp
import json
import time
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from urllib.parse import urlencode
import websockets


# 1. TCP Socket Programming
class TCPServer:
    """Multi-threaded TCP server"""
    
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.socket = None
        self.clients = []
        self.running = False
    
    def start(self):
        """Start the TCP server"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.host, self.port))
            self.socket.listen(5)
            self.running = True
            
            print(f"TCP Server listening on {self.host}:{self.port}")
            
            while self.running:
                try:
                    client_socket, addr = self.socket.accept()
                    print(f"Connection from {addr}")
                    
                    client_thread = threading.Thread(
                        target=self.handle_client,
                        args=(client_socket, addr),
                        daemon=True
                    )
                    client_thread.start()
                    
                except OSError:
                    if self.running:
                        print("Server socket error")
                    break
                    
        except Exception as e:
            print(f"Server error: {e}")
        finally:
            self.stop()
    
    def handle_client(self, client_socket, addr):
        """Handle individual client connection"""
        try:
            self.clients.append(client_socket)
            
            # Send welcome message
            welcome_msg = f"Welcome to the server! Connected clients: {len(self.clients)}\n"
            client_socket.send(welcome_msg.encode('utf-8'))
            
            while True:
                data = client_socket.recv(1024).decode('utf-8').strip()
                if not data:
                    break
                
                print(f"Received from {addr}: {data}")
                
                # Echo back with timestamp
                timestamp = time.strftime("%H:%M:%S")
                response = f"[{timestamp}] Echo: {data}\n"
                
                try:
                    client_socket.send(response.encode('utf-8'))
                except:
                    break
                    
        except ConnectionResetError:
            print(f"Client {addr} disconnected unexpectedly")
        except Exception as e:
            print(f"Error handling client {addr}: {e}")
        finally:
            if client_socket in self.clients:
                self.clients.remove(client_socket)
            client_socket.close()
            print(f"Client {addr} disconnected. Active clients: {len(self.clients)}")
    
    def stop(self):
        """Stop the server"""
        self.running = False
        if self.socket:
            self.socket.close()
        
        # Close all client connections
        for client in self.clients[:]:
            try:
                client.close()
            except:
                pass
        self.clients.clear()
        print("Server stopped")


class TCPClient:
    """TCP client with reconnection capability"""
    
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.socket = None
        self.connected = False
    
    def connect(self):
        """Connect to server"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.connected = True
            print(f"Connected to {self.host}:{self.port}")
            
            # Start receiving thread
            receive_thread = threading.Thread(target=self.receive_messages, daemon=True)
            receive_thread.start()
            
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
    
    def receive_messages(self):
        """Receive messages from server"""
        try:
            while self.connected:
                data = self.socket.recv(1024).decode('utf-8')
                if data:
                    print(f"Server: {data.strip()}")
                else:
                    break
        except:
            pass
        finally:
            self.connected = False
    
    def send_message(self, message):
        """Send message to server"""
        if self.connected:
            try:
                self.socket.send(message.encode('utf-8'))
                return True
            except Exception as e:
                print(f"Send failed: {e}")
                self.connected = False
                return False
        return False
    
    def disconnect(self):
        """Disconnect from server"""
        self.connected = False
        if self.socket:
            self.socket.close()
        print("Disconnected from server")


# 2. UDP Socket Programming
class UDPServer:
    """UDP server for connectionless communication"""
    
    def __init__(self, host='localhost', port=8081):
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
    
    def start(self):
        """Start UDP server"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.bind((self.host, self.port))
            self.running = True
            
            print(f"UDP Server listening on {self.host}:{self.port}")
            
            while self.running:
                try:
                    data, addr = self.socket.recvfrom(1024)
                    message = data.decode('utf-8')
                    print(f"UDP from {addr}: {message}")
                    
                    # Echo back
                    response = f"UDP Echo: {message}"
                    self.socket.sendto(response.encode('utf-8'), addr)
                    
                except OSError:
                    if self.running:
                        print("UDP server socket error")
                    break
                    
        except Exception as e:
            print(f"UDP server error: {e}")
        finally:
            self.stop()
    
    def stop(self):
        """Stop UDP server"""
        self.running = False
        if self.socket:
            self.socket.close()
        print("UDP Server stopped")


class UDPClient:
    """UDP client"""
    
    def __init__(self, host='localhost', port=8081):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def send_message(self, message):
        """Send UDP message"""
        try:
            self.socket.sendto(message.encode('utf-8'), (self.host, self.port))
            
            # Receive response
            data, addr = self.socket.recvfrom(1024)
            return data.decode('utf-8')
        except Exception as e:
            print(f"UDP send failed: {e}")
            return None
    
    def close(self):
        """Close UDP client"""
        self.socket.close()


# 3. HTTP Client/Server
class HTTPClient:
    """Advanced HTTP client with session management"""
    
    def __init__(self, base_url=None, timeout=30):
        self.base_url = base_url
        self.timeout = timeout
        self.session_headers = {}
        self.cookies = {}
    
    def set_auth_token(self, token):
        """Set authorization token"""
        self.session_headers['Authorization'] = f'Bearer {token}'
    
    def set_user_agent(self, user_agent):
        """Set user agent"""
        self.session_headers['User-Agent'] = user_agent
    
    def get(self, url, params=None, headers=None):
        """HTTP GET request"""
        full_url = self._build_url(url)
        
        if params:
            query_string = urlencode(params)
            full_url += f"?{query_string}"
        
        return self._make_request('GET', full_url, headers=headers)
    
    def post(self, url, data=None, json_data=None, headers=None):
        """HTTP POST request"""
        full_url = self._build_url(url)
        return self._make_request('POST', full_url, data=data, 
                                json_data=json_data, headers=headers)
    
    def put(self, url, data=None, json_data=None, headers=None):
        """HTTP PUT request"""
        full_url = self._build_url(url)
        return self._make_request('PUT', full_url, data=data, 
                                json_data=json_data, headers=headers)
    
    def delete(self, url, headers=None):
        """HTTP DELETE request"""
        full_url = self._build_url(url)
        return self._make_request('DELETE', full_url, headers=headers)
    
    def _build_url(self, url):
        """Build full URL"""
        if self.base_url and not url.startswith('http'):
            return f"{self.base_url.rstrip('/')}/{url.lstrip('/')}"
        return url
    
    def _make_request(self, method, url, data=None, json_data=None, headers=None):
        """Make HTTP request using basic socket programming"""
        from urllib.parse import urlparse
        
        parsed_url = urlparse(url)
        host = parsed_url.hostname
        port = parsed_url.port or (443 if parsed_url.scheme == 'https' else 80)
        path = parsed_url.path or '/'
        
        if parsed_url.query:
            path += f"?{parsed_url.query}"
        
        # Build headers
        request_headers = self.session_headers.copy()
        if headers:
            request_headers.update(headers)
        
        # Handle request body
        body = ""
        if json_data:
            body = json.dumps(json_data)
            request_headers['Content-Type'] = 'application/json'
        elif data:
            if isinstance(data, dict):
                body = urlencode(data)
                request_headers['Content-Type'] = 'application/x-www-form-urlencoded'
            else:
                body = str(data)
        
        if body:
            request_headers['Content-Length'] = str(len(body))
        
        # Build HTTP request
        request_lines = [f"{method} {path} HTTP/1.1"]
        request_lines.append(f"Host: {host}")
        
        for header, value in request_headers.items():
            request_lines.append(f"{header}: {value}")
        
        request_lines.append("")  # Empty line
        if body:
            request_lines.append(body)
        
        request = "\r\n".join(request_lines)
        
        # Send request
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            
            if parsed_url.scheme == 'https':
                import ssl
                context = ssl.create_default_context()
                sock = context.wrap_socket(sock, server_hostname=host)
            
            sock.connect((host, port))
            sock.send(request.encode('utf-8'))
            
            # Read response
            response = b""
            while True:
                chunk = sock.recv(4096)
                if not chunk:
                    break
                response += chunk
                
                # Check if we have complete headers
                if b"\r\n\r\n" in response:
                    header_end = response.find(b"\r\n\r\n")
                    headers_part = response[:header_end].decode('utf-8')
                    
                    # Parse content length
                    content_length = None
                    for line in headers_part.split('\r\n'):
                        if line.lower().startswith('content-length:'):
                            content_length = int(line.split(':')[1].strip())
                            break
                    
                    # If we know content length, read exactly that much
                    if content_length is not None:
                        body_start = header_end + 4
                        body_received = len(response) - body_start
                        
                        while body_received < content_length:
                            chunk = sock.recv(min(4096, content_length - body_received))
                            if not chunk:
                                break
                            response += chunk
                            body_received += len(chunk)
                        break
            
            sock.close()
            
            # Parse response
            return self._parse_response(response.decode('utf-8', errors='ignore'))
            
        except Exception as e:
            return {'error': str(e), 'status_code': 0}
    
    def _parse_response(self, response_text):
        """Parse HTTP response"""
        lines = response_text.split('\r\n')
        status_line = lines[0]
        status_code = int(status_line.split()[1])
        
        # Parse headers
        headers = {}
        body_start = 0
        for i, line in enumerate(lines[1:], 1):
            if line == '':
                body_start = i + 1
                break
            if ':' in line:
                key, value = line.split(':', 1)
                headers[key.strip().lower()] = value.strip()
        
        # Extract body
        body = '\r\n'.join(lines[body_start:])
        
        # Try to parse JSON
        json_data = None
        if headers.get('content-type', '').startswith('application/json'):
            try:
                json_data = json.loads(body)
            except:
                pass
        
        return {
            'status_code': status_code,
            'headers': headers,
            'text': body,
            'json': json_data
        }


# 4. Asynchronous Network Programming
class AsyncHTTPClient:
    """Async HTTP client using aiohttp"""
    
    def __init__(self, base_url=None, timeout=30):
        self.base_url = base_url
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.session = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(timeout=self.timeout)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    def _build_url(self, url):
        """Build full URL"""
        if self.base_url and not url.startswith('http'):
            return f"{self.base_url.rstrip('/')}/{url.lstrip('/')}"
        return url
    
    async def get(self, url, params=None, headers=None):
        """Async GET request"""
        full_url = self._build_url(url)
        async with self.session.get(full_url, params=params, headers=headers) as response:\n            return {\n                'status_code': response.status,\n                'headers': dict(response.headers),\n                'text': await response.text(),\n                'json': await response.json() if response.content_type == 'application/json' else None\n            }\n    \n    async def post(self, url, data=None, json_data=None, headers=None):\n        \"\"\"Async POST request\"\"\"\n        full_url = self._build_url(url)\n        async with self.session.post(full_url, data=data, json=json_data, headers=headers) as response:\n            return {\n                'status_code': response.status,\n                'headers': dict(response.headers),\n                'text': await response.text(),\n                'json': await response.json() if response.content_type == 'application/json' else None\n            }\n    \n    async def fetch_multiple(self, urls):\n        \"\"\"Fetch multiple URLs concurrently\"\"\"\n        tasks = []\n        for url in urls:\n            task = asyncio.create_task(self.get(url))\n            tasks.append(task)\n        \n        results = await asyncio.gather(*tasks, return_exceptions=True)\n        return results\n\n\n# 5. WebSocket Example\nclass WebSocketServer:\n    \"\"\"WebSocket server for real-time communication\"\"\"\n    \n    def __init__(self, host='localhost', port=8765):\n        self.host = host\n        self.port = port\n        self.clients = set()\n    \n    async def register(self, websocket):\n        \"\"\"Register new client\"\"\"\n        self.clients.add(websocket)\n        print(f\"Client connected. Total clients: {len(self.clients)}\")\n    \n    async def unregister(self, websocket):\n        \"\"\"Unregister client\"\"\"\n        self.clients.discard(websocket)\n        print(f\"Client disconnected. Total clients: {len(self.clients)}\")\n    \n    async def broadcast(self, message):\n        \"\"\"Broadcast message to all clients\"\"\"\n        if self.clients:\n            await asyncio.gather(\n                *[client.send(message) for client in self.clients],\n                return_exceptions=True\n            )\n    \n    async def handle_client(self, websocket, path):\n        \"\"\"Handle individual client connection\"\"\"\n        await self.register(websocket)\n        try:\n            # Send welcome message\n            await websocket.send(json.dumps({\n                'type': 'welcome',\n                'message': 'Connected to WebSocket server',\n                'clients': len(self.clients)\n            }))\n            \n            async for message in websocket:\n                try:\n                    data = json.loads(message)\n                    print(f\"Received: {data}\")\n                    \n                    # Echo back to all clients\n                    response = {\n                        'type': 'broadcast',\n                        'message': data.get('message', ''),\n                        'sender': data.get('sender', 'Anonymous'),\n                        'timestamp': time.time()\n                    }\n                    \n                    await self.broadcast(json.dumps(response))\n                    \n                except json.JSONDecodeError:\n                    await websocket.send(json.dumps({\n                        'type': 'error',\n                        'message': 'Invalid JSON format'\n                    }))\n                    \n        except websockets.exceptions.ConnectionClosed:\n            pass\n        finally:\n            await self.unregister(websocket)\n    \n    def start(self):\n        \"\"\"Start WebSocket server\"\"\"\n        print(f\"WebSocket server starting on ws://{self.host}:{self.port}\")\n        return websockets.serve(self.handle_client, self.host, self.port)\n\n\nclass WebSocketClient:\n    \"\"\"WebSocket client\"\"\"\n    \n    def __init__(self, uri):\n        self.uri = uri\n        self.websocket = None\n    \n    async def connect(self):\n        \"\"\"Connect to WebSocket server\"\"\"\n        self.websocket = await websockets.connect(self.uri)\n        print(f\"Connected to {self.uri}\")\n    \n    async def send_message(self, message, sender=\"Client\"):\n        \"\"\"Send message to server\"\"\"\n        if self.websocket:\n            data = {\n                'message': message,\n                'sender': sender\n            }\n            await self.websocket.send(json.dumps(data))\n    \n    async def listen(self):\n        \"\"\"Listen for messages from server\"\"\"\n        if self.websocket:\n            async for message in self.websocket:\n                try:\n                    data = json.loads(message)\n                    print(f\"Received: {data}\")\n                except json.JSONDecodeError:\n                    print(f\"Received non-JSON: {message}\")\n    \n    async def close(self):\n        \"\"\"Close connection\"\"\"\n        if self.websocket:\n            await self.websocket.close()\n\n\n# 6. Email Handling\nclass EmailClient:\n    \"\"\"Email client for sending and receiving emails\"\"\"\n    \n    def __init__(self, smtp_server, smtp_port, imap_server, imap_port, username, password):\n        self.smtp_server = smtp_server\n        self.smtp_port = smtp_port\n        self.imap_server = imap_server\n        self.imap_port = imap_port\n        self.username = username\n        self.password = password\n    \n    def send_email(self, to_email, subject, body, is_html=False):\n        \"\"\"Send email\"\"\"\n        try:\n            # Create message\n            msg = MIMEMultipart()\n            msg['From'] = self.username\n            msg['To'] = to_email\n            msg['Subject'] = subject\n            \n            # Attach body\n            if is_html:\n                msg.attach(MIMEText(body, 'html'))\n            else:\n                msg.attach(MIMEText(body, 'plain'))\n            \n            # Send email\n            server = smtplib.SMTP(self.smtp_server, self.smtp_port)\n            server.starttls()\n            server.login(self.username, self.password)\n            \n            text = msg.as_string()\n            server.sendmail(self.username, to_email, text)\n            server.quit()\n            \n            print(f\"Email sent to {to_email}\")\n            return True\n            \n        except Exception as e:\n            print(f\"Failed to send email: {e}\")\n            return False\n    \n    def fetch_emails(self, mailbox='INBOX', limit=10):\n        \"\"\"Fetch recent emails\"\"\"\n        try:\n            # Connect to IMAP server\n            mail = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)\n            mail.login(self.username, self.password)\n            mail.select(mailbox)\n            \n            # Search for emails\n            result, data = mail.search(None, 'ALL')\n            email_ids = data[0].split()\n            \n            # Get recent emails\n            recent_emails = []\n            for email_id in email_ids[-limit:]:\n                result, data = mail.fetch(email_id, '(RFC822)')\n                \n                raw_email = data[0][1]\n                email_message = email.message_from_bytes(raw_email)\n                \n                # Extract email info\n                email_info = {\n                    'id': email_id.decode(),\n                    'from': email_message['From'],\n                    'to': email_message['To'],\n                    'subject': email_message['Subject'],\n                    'date': email_message['Date'],\n                    'body': self._extract_body(email_message)\n                }\n                \n                recent_emails.append(email_info)\n            \n            mail.close()\n            mail.logout()\n            \n            return recent_emails\n            \n        except Exception as e:\n            print(f\"Failed to fetch emails: {e}\")\n            return []\n    \n    def _extract_body(self, email_message):\n        \"\"\"Extract body from email message\"\"\"\n        body = \"\"\n        \n        if email_message.is_multipart():\n            for part in email_message.walk():\n                if part.get_content_type() == \"text/plain\":\n                    body = part.get_payload(decode=True).decode('utf-8')\n                    break\n        else:\n            body = email_message.get_payload(decode=True).decode('utf-8')\n        \n        return body\n\n\n# Demo functions\ndef demo_tcp_socket():\n    \"\"\"Demo TCP socket programming\"\"\"\n    print(\"=== TCP Socket Demo ===\")\n    \n    # Start server in a thread\n    server = TCPServer()\n    server_thread = threading.Thread(target=server.start, daemon=True)\n    server_thread.start()\n    \n    time.sleep(1)  # Give server time to start\n    \n    # Connect client\n    client = TCPClient()\n    if client.connect():\n        # Send some messages\n        client.send_message(\"Hello, Server!\")\n        time.sleep(1)\n        client.send_message(\"How are you?\")\n        time.sleep(1)\n        client.disconnect()\n    \n    time.sleep(1)\n    server.stop()\n\n\ndef demo_udp_socket():\n    \"\"\"Demo UDP socket programming\"\"\"\n    print(\"\\n=== UDP Socket Demo ===\")\n    \n    # Start server in a thread\n    server = UDPServer()\n    server_thread = threading.Thread(target=server.start, daemon=True)\n    server_thread.start()\n    \n    time.sleep(1)  # Give server time to start\n    \n    # Send UDP messages\n    client = UDPClient()\n    response = client.send_message(\"Hello, UDP Server!\")\n    print(f\"UDP Response: {response}\")\n    \n    client.close()\n    server.stop()\n\n\ndef demo_http_client():\n    \"\"\"Demo HTTP client\"\"\"\n    print(\"\\n=== HTTP Client Demo ===\")\n    \n    client = HTTPClient()\n    \n    # Make HTTP request to httpbin (test service)\n    response = client.get('https://httpbin.org/json')\n    print(f\"Status: {response['status_code']}\")\n    print(f\"Response: {response['json']}\")\n\n\nasync def demo_async_http():\n    \"\"\"Demo async HTTP client\"\"\"\n    print(\"\\n=== Async HTTP Demo ===\")\n    \n    async with AsyncHTTPClient() as client:\n        # Fetch multiple URLs concurrently\n        urls = [\n            'https://httpbin.org/json',\n            'https://httpbin.org/uuid',\n            'https://httpbin.org/ip'\n        ]\n        \n        start_time = time.time()\n        results = await client.fetch_multiple(urls)\n        end_time = time.time()\n        \n        print(f\"Fetched {len(urls)} URLs in {end_time - start_time:.2f} seconds\")\n        for i, result in enumerate(results):\n            if isinstance(result, dict) and 'status_code' in result:\n                print(f\"URL {i+1}: Status {result['status_code']}\")\n\n\nasync def demo_websocket():\n    \"\"\"Demo WebSocket communication\"\"\"\n    print(\"\\n=== WebSocket Demo ===\")\n    \n    # Start WebSocket server\n    server = WebSocketServer()\n    server_task = asyncio.create_task(server.start())\n    \n    await asyncio.sleep(1)  # Give server time to start\n    \n    # Connect client\n    client = WebSocketClient('ws://localhost:8765')\n    await client.connect()\n    \n    # Send messages\n    await client.send_message(\"Hello, WebSocket!\")\n    await client.send_message(\"This is a test message\")\n    \n    # Listen for a short time\n    try:\n        await asyncio.wait_for(client.listen(), timeout=2)\n    except asyncio.TimeoutError:\n        pass\n    \n    await client.close()\n    server_task.cancel()\n\n\ndef run_network_demos():\n    \"\"\"Run all network programming demos\"\"\"\n    print(\"Network Programming Examples\")\n    print(\"=\" * 40)\n    \n    demo_tcp_socket()\n    demo_udp_socket()\n    demo_http_client()\n    \n    # Run async demos\n    asyncio.run(demo_async_http())\n    asyncio.run(demo_websocket())\n    \n    print(\"\\nAll network demos completed!\")\n\n\nif __name__ == \"__main__\":\n    run_network_demos()")
