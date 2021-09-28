# Bloock SDK -  Python

This SDK offers all the features available in the Bloock Toolset:
- Write records
- Get records proof
- Validate proof
- Get records details

## Installation

The SDK can be installed with PIP as follows:

```shell
$ pip install bloock
```

## Usage

The following examples summarize how to access the different functionalities available:

### Prepare data

In order to interact with the SDK data must be processed through the Record module.

There are several ways to generate a Record:

```python
from bloock import Record

# From a dict
d = {'data': 'Example Data'}
Record.fromDict(d)

# From a hash string (hex encoded 64-chars long string with no "0x" prefix)
Record.fromHash('5ac706bdef87529b22c08646b74cb98baf310a46bd21ee420814b04c71fa42b1')

# From a hex encoded string (with no "0x" prefix)
Record.fromHex('0123456789abcdef')

# From a string
Record.fromString('Example Data')

# From a bytes
Record.fromBytes(b'Example Data')

# Retrieve the computed record
Record.fromBytes(b'Example Data').getHash()
```

### Send records

This example shows how to send data to Bloock.

```python
from bloock import BloockClient, Record, BloockException
import os

api_key = os.getenv("BLOOCK_APIKEY", default='api_key')
client = BloockClient(api_key)

records = [Record.fromString('Example Data 1')]

try:
    send_receipt = client.sendRecords(records)
    print('sendReceipt status: ', send_receipt[0].status)
except BloockException:
	raise
```

### Get records status

This example shows how to get all the details and status of records:

```python
from bloock import BloockClient, Record, BloockException
import os

api_key = os.getenv("BLOOCK_APIKEY", default='apiKey')
client = BloockClient(api_key)

records = [
    Record.fromString('Example Data 1'),
    Record.fromString('Example Data 2'),
    Record.fromString('Example Data 3')
]

try:
    m_receipts = client.getRecords(records)
    for mr in m_receipts:
        print("RecordReceipt: {{anchor_id: {}, client:{}, record:{}, status:{}}}".format(
            mr.anchor, mr.client, mr.record, mr.status))
except BloockException:
	raise
```


### Wait for records to process

This example shows how to wait for a record to be processed by Bloock after sending it:

```python
from bloock import BloockClient, Record, BloockException
import os

api_key = os.getenv("BLOOCK_APIKEY", default='api_key')
client = BloockClient(api_key)
records = [Record.fromString('Example Data 1')]

try:
    send_receipt = client.sendRecords(records)
    anchor = client.waitAnchor(send_receipt[0].anchor)
    print("Anchor: {{id: {}, blocks:{}, network:{}, root: {}, status:{}}}".format(
        anchor.id, anchor.block_roots, anchor.networks, anchor.root, anchor.status))
except BloockException:
	raise
```

### Get and validate records proof

There are basically two ways to validate some records had been pushed to the blockchain: combining calls to *getProof* and *verifyProof*, or calling directly *verifyRecords*.

The method *getProof* will, by default, return an integrity proof of the requested data in any of the compatible blockchain networks. It is possible to specify in which network and from which date it must, at least, be valid using the optional parameters *network* and *date*:

```python
from bloock import BloockClient, Record, BloockException, Network
import os, time

api_key = os.getenv("BLOOCK_APIKEY", default='apiKey')

client = BloockClient(api_key)

# records already sent and anchored by Bloock 
records = [
    Record.fromString('Example Data 1'),
    Record.fromString('Example Data 2'),
    Record.fromString('Example Data 3')
]

try:
    proof = client.getProof(records, network = Network.BLOOCK_CHAIN, date = time.time())
    timestamp = client.verifyProof(proof)   
    print('When were our records sent to Bloockchain? : {}'.format(0<timestamp))
except BloockException:
    raise
```

For ease of use, there is also the wrapper method *verifyRecords* that will do the same as the two calls before, but this time around will only check proofs sent to Ethereum mainnet be default:

```python
from bloock import BloockClient, Record, BloockException
import os

api_key = os.getenv("BLOOCK_APIKEY", default='apiKey')

client = BloockClient(api_key)

# records already sentand anchored by Bloock 
records = [
    Record.fromString('Example Data 1'),
    Record.fromString('Example Data 2'),
    Record.fromString('Example Data 3')
]

try:
    timestamp = client.verifyRecords(records)
    print('When were our records sent to Ethereum mainnet? : {}'.format(0<timestamp))
except BloockException:
    raise
```

Keep in mind despite having Ethereum mainnet and Rinkeby available, only Bloockchain is
usable when working with test api keys. 



### Full example

This snippet shows a complete data cycle including: write, record status polling, proof retrieval and validation.

```python
#!/usr/bin/env python3

from bloock import BloockClient, Record, BloockException
import os, random


def randHex(l):
    ''' Helper function to generate a random record.'''
    val = [int(random.uniform(0, 256)) for x in range(0, l)]
    result = ''
    for n in val:
        result += ('%x' % n)
    return result


def main():
    api_key = os.getenv("API_KEY", default='apiKey')

    client = BloockClient(api_key)

    try:
        records = [Record.fromString(randHex(64))]
        send_receipt = client.sendRecords(records)
        print('Record sent to Bloock. Waiting for anchor to be processed ...')
        client.waitAnchor(send_receipt[0].anchor)

        print('Anchor retrieved. Getting Record proof ...')
        proof = client.getProof(records)

        print('Verifying proof ...')
        
        # verifyProof's optional network parameter must be set to Network.BLOOCK_CHAIN when working with test api keys:
        timestamp = client.verifyProof(proof)

        if timestamp <= 0:
            print('Data not registered on the blockchain.')

        print('Success!')

    except BloockException as e:
        print(e)


if __name__ == "__main__":
    # execute only if run as a script
    main()
```
