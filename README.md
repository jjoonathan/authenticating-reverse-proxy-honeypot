# ARP Honeypot

Honeypot for the [Authenticating Reverse Proxy](https://bitbucket.org/jonathandewerdxylem/authenticating_reverse_proxy/src/master/) (not the Address Resolution Protocol). The ARP is designed to secure a "squishy" (no https, no authentication) dashboard server. No request should ever make it through the ARP without authenticating, and this honeypot is designed to constantly check that assumption by sounding a warning (sending a SNS notification) if it receives any request.

Visit the production server here: https://hp.xds.sensus-sa.net/git
