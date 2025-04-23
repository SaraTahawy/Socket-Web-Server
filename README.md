

### 📄 README.md

```markdown
# 🧠 Network Security - Assignment 3 - Simple Python Web Server

This project is part of the **Intro to Socket Programming** assignment.
The goal is to implement a basic HTTP web server in Python that can handle one client
request at a time.

---

## 🔧 What This Project Does

This simple Python-based web server can:

1. Open a TCP socket and listen for a connection on port `9090`.
2. Accept an HTTP request from a browser.
3. Parse the request to extract the requested filename.
4. Read the file from the local server directory.
5. Send back an HTTP 200 OK response along with the file content.
6. If the file doesn't exist, send a 404 Not Found response.

---

## 📁 Project Structure

```bash
.
├── Socket.py       # Python script for the web server
├── test.html          # Sample HTML file to serve
└── README.md           # Project documentation
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your system.
2. Save the HTML file (e.g., `test.html`) in the same folder as the Python script.
3. Run the server using this command:

```bash
python Socket.py
```

4. Open your browser and go to:

```
http://localhost:9090/test.html
```

5. You should see your HTML content rendered. If the file doesn't exist, you will see a 404 error page.

---

## 📌 Notes

- This server only handles **one request** at a time and then shuts down.
- Make sure the filename you request in the browser matches exactly with the file on the server (e.g., `test.html`).
- The server listens on port `9090`, which can be changed in the code.

---

## ⚠️ Error Handling

If a user requests a file that doesn't exist on the server, the following response is returned:

```http
HTTP/1.1 404 Not Found
<html><body><h1>404 Not Found</h1></body></html>
```

---
