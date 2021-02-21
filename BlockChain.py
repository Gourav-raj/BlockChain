#BlockChain is a data structure which ensure the security of transations 
#on which we can relay to use it for bitcoin tansaction 
#consit of block 
# blocks consist transcation
# blocks are connected through hashing and each block has a unique fingerPrint and
# it is based on transaction and previous block fingerprint

import hashlib #produces uniue hashes for our blocks
from Block import Block

blockchain= []
#						V-- this is previous hash  ,this is transcation array
genesis_block=Block("Chancellor on the brink ....",["satoshi send 1 bitcoin to ivan","Maria sent 5 bitcoin to Finney"]) #this is the first ever block (satoshi create this first ever bitcoin block)

second_block= Block(genesis_block.block_hash,["gourav send 4 bitcoin to satoshi","ram sent 54 bitcoin to shyam"])

print("Block Hash:genesis_block")
print(genesis_block.block_hash)

print("Block Hash:second_block")
print(second_block.block_hash)
