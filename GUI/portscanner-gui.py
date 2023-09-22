#!/bin/python3

from flask import Flask, render_template, request
import socket
import datetime as dt
import sys

app = Flask(__name__)

def scan_ports(target, p1, p2):
    open_ports = []
    try:
        for port in range(p1, p2 + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            s.close()
    except KeyboardInterrupt:
        pass
    return open_ports

@app.route("/", methods=["GET", "POST"])
def scanner():
    if request.method == "POST":
        ip_addr = request.form["ip_addr"]
        p1 = int(request.form["start_port"])
        p2 = int(request.form["end_port"])
        target = socket.gethostbyname(ip_addr)
        open_ports = scan_ports(target, p1, p2)
        current_time = dt.datetime.now()
        return render_template("index.html", target=target, open_ports=open_ports, now=current_time)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
