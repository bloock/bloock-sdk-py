# Enchainté SDK -  Python

This SDK offers all the features available in the Enchainté Toolset:
- Write messages
- Get messages proof
- Validate proof
- Get messages details

## Installation

The SDK can be installed with PIP as follows:

```shell
$ pip install --index-url https://test.pypi.org/simple/ enchaintesdk
```

## Usage

The following examples summarize how to access the different functionalities available:

### Prepare data

In order to interact with the SDK and keep track of the information sent to it, the data should be processed through the Hash module.

There are several ways to generate a Hash:

```python
from enchaintesdk.entity.hash import Hash
import numpy as np

# From a JSON
Hash.fromJson({
    data: 'Example Data'
})

# From a hash string (hex encoded 64-chars long string)
Hash.fromHash('5ac706bdef87529b22c08646b74cb98baf310a46bd21ee420814b04c71fa42b1')

# From a hex encoded string
Hash.fromHex('123456789abcdef')

# From a string
Hash.fromString('Example Data')

# From a Uint8Array with a lenght of 32
u8Array = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype='uint8')
Hash.fromUint8Array(u8Array)
```

### Write messages

This example shows how to send data to Enchainté.

```python
from enchaintesdk.enchainteClient import EnchainteClient

apiKey = os.getenv("ENCHAINTE_APIKEY", default='apiKey')

client = EnchainteClient(apiKey)

try:
	deferred_data = client.write('Example Data', 'str')
except BaseException:
	raise

```

The accepted data types are: hexadecimal strings as "hex" (without "0x" at the begining), any other kind of string as "str", byte arrays as "u8a", jsons as "json", and enchainte's hash objects as "hash".

### Get and validate messages proof

This example shows how to get a proof for an array of messages and validate it:

```python
from enchaintesdk.enchainteClient import EnchainteClient
from enchaintesdk.entity.hash import Hash

apiKey = os.getenv("ENCHAINTE_APIKEY", default='apiKey')

client = EnchainteClient(apiKey)

const hashes = [
    Hash.fromString('Example Data 1'),
    Hash.fromString('Example Data 2'),
    Hash.fromString('Example Data 3')
]

try:
	proof = client.getProof(hashes)
	is_valid_boolean = client.verify(proof)
except BaseException:
	raise
```

### Get messages status

This example shows how to get all the details and status of messages:

```python
from enchaintesdk.enchainteClient import EnchainteClient
from enchaintesdk.entity.hash import Hash

apiKey = os.getenv("ENCHAINTE_APIKEY", default='apiKey')

client = EnchainteClient(apiKey)

const hashes = [
    Hash.fromString('Example Data 1'),
    Hash.fromString('Example Data 2'),
    Hash.fromString('Example Data 3')
]

try:
	messages = client.getMessages(hashes)
except BaseException:
	raise
```