# pyChat

This program supports chat rooms where users can send text messages to other users in the same chat room. Each chat room has one admin - the person who created the room - who can block and unblock other occupants, as well as delete the chat room. 

Starting up the server:

    $ python3 launch_server.py

Starting up a client:

    $ python3 client.py

Commands:
    
    /help
    /create [chat room name]
    /join [chat room name]
    /leave 
    /set_alias
    /set_admin [alias]
    /delete
    /block [alias]
    /unblock [alias]

Features to implemented:

    - Registered Users
    - Database integration (passwords, user info, etc)
    - Security Measures (currently there are none)
    - GUI
