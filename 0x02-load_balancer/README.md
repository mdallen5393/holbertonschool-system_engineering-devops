# PROJECT: 0x02. Load balancer
### AUTHOR: Matthew Allen

## TASKS:
### 0. Double the number of webservers - 0-custom_http_response_header
Configures server `web-02` to be identical to `web-02` using the bash script created previously.  Adds custom Nginx response header.
- Configures Nginx so that its HTTP response contains a header (on both `web-01` and `web-02`), including the name `X-served-By` and the value being the hostname of the server Nginx is running on.
- `0-custom_http_response_header` is written so that it configures a brand new Ubuntu machine to these requirements, ignoring SC2154 for `shellcheck`.

### 1. Install your load balancer - 1-install_load_balancer
Configures HAproxy on the `1b-01` server.
- Configured so that it sends traffic to `web-01` and `web-02`.
- Distributes requests using a roundrobin algorithm.
- ensures that HAproxy can be managed via an init script.
- Script configures a new ubuntu machine to respect the above requirements.
