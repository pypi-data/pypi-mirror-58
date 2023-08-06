# SSLER


Easily test with SSL in your localhost.

> Might be a bit slow for now

### Usage

- Run your server as normal
- Call `ssler` with your localhost server address

```bash
ssler
Easily redirect your localhost server though an a server with self signed certificate

usage: ssler '<domain>' '<ssler_port(optional)>'
examples:
    - ssler 'localhost:8080'
    - ssler 'http://33.22.22.88'
    - ssler 'localhost:8080' 8888
```
