# PROJECT: 0x03. Firewall
### AUTHOR: Matthew Allen

## TASKS:
### 0. Block all incoming traffic but - `0-block_all_incoming_traffic_but`
Install the `ufw` firewall and setup rules on server `web-01`.
Requirements:
* Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
    - `22` (SSH)
    - `443` (HTTPS SSL)
    - `80` (HTTP)
* Share the `ufw` commands that you used in the answer file `0-block_all_incoming_traffic_but`.
