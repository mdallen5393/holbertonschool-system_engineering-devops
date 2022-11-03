# PROJECT: 0x01. Web server
### AUTHOR: Matthew Allen

## TASKS:
### 0. Transfer a file to your server - 0-transfer_file
Bash script that transfers a file from our client to a server.

### 1. Install nginx web server - 1-install_nginx_web_server
Bash script that configures a new Ubuntu machine to respect requirements:
- install `nginx` on the `web-01` server
- Nginx should be listening on port 80
- When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World`.

### 2. Setup a domain name - 2-setup_a_domain_name
Document containing the domain name of a `.tech` domain (e.g. `foobar.tech`).

### 3. Redirection - 3-redirection
Bash script containing commands to automatically configure a Ubuntu machine to respect the following requirements:
- Configure the Nginx server so that `/redirect_me` is redirecting to another page.
- The redirection must be a "301 Moved Permanently"

### 4. Not found page 404 - 4-not_found_page_404
Bash script that configures a brand new Ubuntu machine that has a custom 404 page containing the string `Ceci n'est pas une page`.
