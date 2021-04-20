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

In order to interact with the SDK data must be processed through the Message module.

There are several ways to generate a Message:

```python
from enchaintesdk import Message

# From a dict
d = {'data': 'Example Data'}
Message.fromDict(d)

# From a hash string (hex encoded 64-chars long string with no "0x" prefix)
Message.fromHash('5ac706bdef87529b22c08646b74cb98baf310a46bd21ee420814b04c71fa42b1')

# From a hex encoded string (with no "0x" prefix)
Message.fromHex('0123456789abcdef')

# From a string
Message.fromString('Example Data')

# From a bytes
Message.fromBytes(b'Example Data')

# Retrieve the computed message
Message.fromBytes(b'Example Data').getMessage()
```

### Send messages

This example shows how to send data to Enchainté.

```python
from enchaintesdk import EnchainteClient, Message
from enchaintesdk.exceptions import EnchainteSDKException
import os

api_key = os.getenv("ENCHAINTE_APIKEY", default='api_key')
client = EnchainteClient(api_key)
messages = [Message.fromString('Example Data 1')]

try:
	send_receipt = client.sendMessages(messages)
    print('sendReceipt status: {}', send_receipt.status)
except EnchainteSDKException:
	raise
```

### Get messages status

This example shows how to get all the details and status of messages:

```python
from enchaintesdk import EnchainteClient, Message
from enchaintesdk.exceptions import EnchainteSDKException
import os

apiKey = os.getenv("ENCHAINTE_APIKEY", default='apiKey')

client = EnchainteClient(apiKey)

messages = [
    Message.fromString('Example Data 1'),
    Message.fromString('Example Data 2'),
    Message.fromString('Example Data 3')
]

try:
	m_receipts = client.getMessages(messages)
    print("MessageReceipt: \{anchor_id: {}, client:{}, message:{}, status:{}\}".format(
        m_receipts.anchor, m_receipts.client, m_receipts.message, m_receipts.status))
except EnchainteSDKException:
	raise
```


### Wait for messages to process

This example shows how to wait for a message to be processed by Enchainté after sending i:

```python
from enchaintesdk import EnchainteClient, Message
from enchaintesdk.exceptions import EnchainteSDKException
import os

api_key = os.getenv("ENCHAINTE_APIKEY", default='api_key')
client = EnchainteClient(api_key)
messages = [Message.fromString('Example Data 1')]

try:
	send_receipt = client.sendMessages(messages)
    anchor = sdk.waitAnchor(send_receipt[0].anchor)
    print("Anchor: {{id: {}, blocks:{}, network:{}, root: {}, status:{}}}".format(
        anchor.id, anchor.blocks, anchor.network, anchor.root, anchor.status))
except EnchainteSDKException:
	raise
```

### Get and validate messages proof

This example shows how to get a proof for an array of messages and validate it:

```python
from enchaintesdk import EnchainteClient, Message
from enchaintesdk.exceptions import EnchainteSDKException
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
    print('Are our messages found in blockchain? : {}'.format(is_valid_boolean))
except EnchainteSDKException:
	raise
```

### Full example

This snippet shows a complete data cycle including: write, message status polling and proof retrieval and validation.

```python
#!/usr/bin/env python3

from enchaintesdk import EnchainteClient, Message
from enchaintesdk.exceptions import EnchainteSDKException
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
        messages = [Message.fromString(randHex(64))]
        send_receipt = client.sendMessages(messages)

        client.waitAnchor(send_receipt[0].anchor)

        proof = client.getProof(messages)
        
        timestamp = client.verifyProof(proof)
        
        if timestamp <= 0:
            print('Data not registered on blockchain.')
        
        print('Finished!')

    except EnchainteSDKException as e:
        print(e)


if __name__ == "__main__":
    # execute only if run as a script
    main()
```
