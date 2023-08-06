# buddyns-python

A python client library to easily consume [BuddyNS](https://www.buddyns.com)'s [API](https://www.buddyns.com/support/api/v2/).

# Installation and compatibility

Simply install the library from PyPI:

    pip install buddyns

The library supports **Python 2.7+ and 3+** natively.

# Quick start

    from BuddyNS import BuddyNSAPI

    # initialize the API object with your BuddyNS API token (from your BuddyBoard)
    bd = BuddyNSAPI(key='api_token_from_BuddyNS_account')

    # list domain names currently hosted on my account
    l = bd.list_domains()
    print(l)

    # add new domain 'testdomain1761826433.com' using '1.2.3.4' as primary address
    bd.add_domain('testdomain1761826433.com', '1.2.3.4')

    # remove a domain
    bd.remove_domain('testdomain1761826433.com')

    # get status of a domain
    s = bd.get_domain_status('testdomain1761826433.com')
    print(s)

# How to get your account key

Get your API key from your BuddyNS account:

1. Log into your [BuddyNS account](https://www.buddyns.com/buddyboard/account/)
1. Reach your settings by clicking the respective button
1. Reach section "Integration", and generate or copy your API key

If you do not have an account on BuddyNS already, create one at [BuddyNS](https://www.buddyns.com/activation/).

# Bugs, enhancements and feedback

Pull requests, bug reports, enhancement proposals and any feedback are welcome on the [project](https://gitlab.com/BuddyNS/buddyns-python)'s page.

# Support and further information

Do **not** contact BuddyNS for developer support with this library. Rely on this further documentation instead:

- [API documentation](https://www.buddyns.com/support/api/v2/)
- [interactive API documentation](https://app.swaggerhub.com/apis-docs/buddyns/BuddyNS/)
- [BuddyNS FAQ](https://www.buddyns.com/faq/)

You can get general support on Python from the great people of the `#python` channel on the [freenode IRC network](https://webchat.freenode.net).