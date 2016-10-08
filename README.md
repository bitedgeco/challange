# challange
special "whiteboard" challange

##Task

"""Mock CDN.

You work for a company trying to start their own Content Delivery Network.
However, the company isn't rich.
They can only afford to put one direct connection between each pair of continents.
Additionally they can only afford to put 
AT MOST two incoming connections on each city and 
AT MOST three outgoing connections.
They want you to decide which connections to make.
These are the cities they're considering:

-North America-   
New York, US
Chicago, US
San Francisco, US
Seattle, US
Washington D.C., US
Austin, US
Montreal, CAN
Mexico City, MEX

-Europe-   
London, UK
Paris, FRA
Moscow, RUS
Berlin, GER
Rome, ITA

-Africa-   
Cairo, EG
Johannesburg, ZA

-Asia-   
Tokyo, JAP
Beijing, CHI
Bangkok, TH
Mumbai, IND
Sydney, AUS
Seoul, KR

-South America-   
Buenos Ares, ARG
Sao Paulo, BRZ

Once those connections are made, they want you to write an API for the CDN.
This API should use HTTP verbs to...

* distribute content across the network
* read content
* update it
* remove it from the CDN

For every action, you should specify a city to start the action from.
For example:

    >>> distribute_action("some_filename", "New York, US")

If an action is successful, a 200 status code should be returned.

    >>> read_action("some_filename", "Johannesburg, ZA")
    Status: 200
    Retrieved some_filename.

If a user tries to access/remove the content and it doesn't exist, a 404 status
code should be returned.

    >>> remove_action("some_filename", "Rome, ITA")
    Status: 404
    some_filename does not exist.

Each status code should be accompanied with an appropriate message relating to
the action that was attempted.

Each action should accomplish its task using the connections between cities.

##Additional info

Conections are one way

you don’t need tests but you should show that your code works put an `if __name__ == "__main__":` block in there
"""

##Sources/Appreciation
https://www.python.org/doc/essays/graphs/