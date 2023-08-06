## Open Source Visa API
This requires you to sign up with Visa at [https://developer.visa.com/](https://developer.visa.com/).

This library currently only provides DPS (pre-paid card monitoring services) since that's all I need.   

If you need something else for your project and can't do it yourself I can do it pretty easily probably - just send me a message and I'll help out if I can. 


## Requirements.

Python 3.5+ - this probably works in Python 2 with compatiblity libs but it's 2020 peeps. :) 

## Installation & Usage
### pip install

````python
pip install visa-api
````

### You want to directly integrate the source?

Execute the below command.

```sh
pip install -r requirements.txt
```
(you may need to run `pip` with root permission: `sudo pip install -r requirements.txt`)

Then import the package:
```python
from visa_dps.VisaSession import VisaSession
from config import Config


active_session = VisaSession(
    Config.username, Config.password, be_noisy=True, use_sandbox=True,
    client_cert="../client_private_key.pem", client_key="../key_file.pem")        



```

## Tests
- Edit the file **config.py** to set the user, password, and pem fields. Please refer the [Visa Getting Started Guide](https://developer.visa.com/vdpguide#get-started-overview) to get the credentials.

Don't sent me pull requests without tests for them please.  

## Getting Started

It's pretty easy yo.  You need to get a project password and username from Visa, and have them create a PEM to encrypt traffic.

Create a VisaSession:
```python
my_session = VisaSession(Config.username, Config.password, be_noisy=True, use_sandbox=True,
                                 client_cert="../cert.pem", client_key="../rosarius.pem")
```

And then use you use this session with each library call.

```python
card_details = dps_get_card_details(my_session, "7a353971-l4uo-9877-algd-lz1fe25349i9")
```

There are very verbose docs under the html directory and there is full Google-style docs in the source code itself.   Your editor should display help/notes while typing.


##License
**Copyright (c) Lee Preimesberger / Caprica LLC**

This is all MIT licensed - you are welcome to use, include, and hack.   You may not though roll this code into a paid-library and claim it's yours.   Just be nice and go make something awesome. :) 
