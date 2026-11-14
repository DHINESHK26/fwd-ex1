from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
<head>
    <title>Computer Network Protocols</title>
</head>
<body>

    <h2>List of Computer Network Protocols</h2>

    <table border="1" cellpadding="10" cellspacing="0">
        <tr>
            <th>S.No.</th>
            <th>Protocol</th>
            <th>Full Form</th>
            <th>Main Use</th>
        </tr>

        <tr>
            <td>1</td>
            <td>HTTP</td>
            <td>Hypertext Transfer Protocol</td>
            <td>Transfers web pages</td>
        </tr>

        <tr>
            <td>2</td>
            <td>HTTPS</td>
            <td>Hypertext Transfer Protocol Secure</td>
            <td>Secure website communication</td>
        </tr>

        <tr>
            <td>3</td>
            <td>FTP</td>
            <td>File Transfer Protocol</td>
            <td>Transfers files</td>
        </tr>

        <tr>
            <td>4</td>
            <td>TCP</td>
            <td>Transmission Control Protocol</td>
            <td>Reliable data transmission</td>
        </tr>

        <tr>
            <td>5</td>
            <td>UDP</td>
            <td>User Datagram Protocol</td>
            <td>Fast data transmission</td>
        </tr>

        <tr>
            <td>6</td>
            <td>IP</td>
            <td>Internet Protocol</td>
            <td>Routes data packets</td>
        </tr>

        <tr>
            <td>7</td>
            <td>DNS</td>
            <td>Domain Name System</td>
            <td>Converts domain names into IP addresses</td>
        </tr>

        <tr>
            <td>8</td>
            <td>DHCP</td>
            <td>Dynamic Host Configuration Protocol</td>
            <td>Assigns IP addresses automatically</td>
        </tr>

        <tr>
            <td>9</td>
            <td>SMTP</td>
            <td>Simple Mail Transfer Protocol</td>
            <td>Sends emails</td>
        </tr>

        <tr>
            <td>10</td>
            <td>SSH</td>
            <td>Secure Shell</td>
            <td>Secure remote access</td>
        </tr>
    </table>

</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()