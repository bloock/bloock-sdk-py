# Enchainté SDK -  Python

This SDK offers all the features available in the Enchainté Toolset:
- Write messages
- Get messages proof
- Validate proof
- Get messages details

## Installation

The SDK can be installed with PIP as follows:

```shell
$ pip install --index-url https://test.pypi.org/simple/ enchaintesdk --extra-index-url https://pypi.org/simple/
```

## Usage

The following examples summarize how to access the different functionalities available:

### Prepare data

In order to interact with the SDK data can, but it is not mandatory, be processed through the Message module.

There are several ways to generate a Message:

```python
from enchaintesdk import Message
import numpy as np
import json

# From a JSON
j = json.dumps({
    'data': 'Example Data'
    })
Message.fromJson(j)

# From a message string (hex encoded 64-chars long string)
Message.fromMessage('5ac706bdef87529b22c08646b74cb98baf310a46bd21ee420814b04c71fa42b1')

# From a hex encoded string

Message.fromHex('0123456789abcdef')

# From a string
Message.fromString('Example Data')

# From a Uint8Array with a lenght of 32
u8Array = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype='uint8')
Message.fromUint8Array(u8Array)

# Retrieve the computed message
Message.fromUint8Array(u8Array).getMessage()
```

### Write messages

This example shows how to send data to Enchainté.

```python
from enchaintesdk import EnchainteClient
import os

apiKey = os.getenv("ENCHAINTE_APIKEY", default='apiKey')

client = EnchainteClient(apiKey)

try:
	client.write('Example Data', 
        'str',
        lambda: pass,
        lambda e: print('an error was found: '+ str(e)))
except BaseException:
	raise

```

The accepted data types are: hexadecimal strings as "hex" (without "0x" at the begining), any other kind of string as "str", byte arrays as "u8a", jsons as "json", and Enchainte's Message objects as "message".

Also note that it is required to pass two callbacks to write. They are executed once the message was been recived by the server (the first one), or if any exeption occurs while trying.

### Get and validate messages proof

This example shows how to get a proof for an array of messages and validate it:

```python
from enchaintesdk import EnchainteClient, Message
import os

apiKey = os.getenv("ENCHAINTE_APIKEY", default='apiKey')

client = EnchainteClient(apiKey)

messages = [
    Message.fromString('Example Data 1'),
    Message.fromString('Example Data 2'),
    Message.fromString('Example Data 3')
]

try:
	proof = client.getProof(messages)
	is_valid_boolean = client.verifyProof(proof)
    # or simply: is_valid_boolean = client.verifyMessages(messages)
except BaseException:
	raise
```

### Get messages status

This example shows how to get all the details and status of messages:

```python
from enchaintesdk import EnchainteClient, Message
import os

apiKey = os.getenv("ENCHAINTE_APIKEY", default='apiKey')

client = EnchainteClient(apiKey)

messages = [
    Message.fromString('Example Data 1'),
    Message.fromString('Example Data 2'),
    Message.fromString('Example Data 3')
]

try:
	messages = client.getMessages(messages)
except BaseException:
	raise
```

### Full example

This snippet shows a complete data cycle including: write, message status polling and proof retrieval and validation.

```python
#!/usr/bin/env python3

from enchaintesdk import EnchainteClient, Message
import random
import time
import os

def randHex(l):
    ''' Helper function to generate a random message.'''
    val = [int(random.uniform(0, 256)) for x in range(0,l)]
    result = ''
    for n in val:
        result += ('%x' % n)
    return result


def main():
    apiKey = os.getenv("ENCHAINTE_APIKEY", default='apiKey')

    client = EnchainteClient(apiKey)

    h = Message.fromString(randHex(64))
    try:
        # Writing message
        client.write(h.getMessage(), 
            'hex',
            lambda: pass,
            lambda e: print('An error has occurred: '+ str(e))
        )
        
        # Polling message status
        found = False
        while not found:
            print('Polling message status...')
            time.sleep(0.5)
            messages = client.getMessages([h])
            for m in messages:
                print(m.status)
                found = (m.status == 'success')
        
        print('Message reached Blockchain!')

        # Retrieving message proof
        proof = client.getProof([h])
        
        # Validating message proof
        valid = False
        while not valid:
            time.sleep(0.5)
            valid = client.verifyProof(proof)
            print('Message validation - %s' % valid)
        
        print('Finished!')

    except BaseException as e:
        print(e)


if __name__ == "__main__":
    # execute only if run as a script
    main()
```