import time
import json
import web3
from eth_account import Account
from web3.auto import w3
from web3.providers.websocket import WebsocketProvider
from web3 import Web3
from solc import compile_standard

with open("contract.sol") as c:
  contractText=c.read()
with open(".pk") as pkfile:
  privateKey=pkfile.read()
with open(".infura") as infurafile:
  infuraKey=infurafile.read()

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "Greeter.sol": {
            "content": contractText
        }
    },
    "settings":
        {
            "outputSelection": {
                "*": {
                    "*": [
                        "metadata", "evm.bytecode"
                        , "evm.bytecode.sourceMap"
                    ]
                }
            }
        }
})
bytecode = compiled_sol['contracts']['Greeter.sol']['Greeter']['evm']['bytecode']['object']
abi = json.loads(compiled_sol['contracts']['Greeter.sol']['Greeter']['metadata'])['output']['abi']
W3 = Web3(WebsocketProvider('wss://ropsten.infura.io/ws/v3/%s'%infuraKey))
account1=Account.from_key(privateKey);
address1=account1.address
Greeter = W3.eth.contract(abi=abi, bytecode=bytecode)

nonce = W3.eth.getTransactionCount(address1)
tx_dict = Greeter.constructor().buildTransaction({
  'chainId': 3,
  'gas': 1400000,
  'gasPrice': w3.toWei('40', 'gwei'),
  'nonce': nonce,
  'from':address1
})

signed_txn = W3.eth.account.sign_transaction(tx_dict, private_key=privateKey)
print("Deploying the Smart Contract")
result = W3.eth.sendRawTransaction(signed_txn.rawTransaction)
tx_receipt = None#W3.eth.getTransactionReceipt(result)

count = 0
while tx_receipt is None and (count < 30):
  time.sleep(10)
  try:
    tx_receipt = W3.eth.getTransactionReceipt(result)
  except:
    print('.')

if tx_receipt is None:
  print (" {'status': 'failed', 'error': 'timeout'} ")
#diagnostics
#print (tx_receipt)

print("Contract address is:",tx_receipt.contractAddress)

greeter = W3.eth.contract(
  address=tx_receipt.contractAddress,
  abi=abi
)


print("Output from greet()")
print(greeter.functions.greet().call())

def my_Authentication():
  print("Hi Paul, bellow will be the function Ive added to the Code")
  print("I need your full name for authentication porposes")
  firstName = ""
  lastName = ""
  print("Please enter your first name:")
  firstName = input(" ").lower()
  print("Please enter your last name:")
  lastName = input(" ").lower()
  print("Hi "+ firstName +" "+ lastName + " you are authorised! Thanks")


nonce = W3.eth.getTransactionCount(address1)
tx_dict = greeter.functions.setOwnerName(my_Authentication()).buildTransaction({
  'chainId': 3,
  'gas': 1400000,
  'gasPrice': w3.toWei('40', 'gwei'),
  'nonce': nonce,
  'from':address1
  
 
  
})

signed_txn = W3.eth.account.sign_transaction(tx_dict, private_key=privateKey)
result = W3.eth.sendRawTransaction(signed_txn.rawTransaction)
tx_receipt = None#W3.eth.getTransactionReceipt(result)

count = 0
while tx_receipt is None and (count < 100):
  time.sleep(2)
  try:
    tx_receipt = W3.eth.getTransactionReceipt(result)
  except:
    print('.')

if tx_receipt is None:
  print (" {'status': 'failed', 'error': 'timeout'} ")

print("Output from greet()")
print(greeter.functions.greet().call({"from":account1.address}))

