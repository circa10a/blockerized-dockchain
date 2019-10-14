#!/usr/bin/env python3

import hashlib as hasher
import datetime as date
from time import sleep
from os import environ


# Define what a block is
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()


    def hash_block(self):
        sha = hasher.sha256()
        string = f"{self.index} {self.timestamp} {self.data} {self.previous_hash}".encode('utf-8')
        sha.update(string)
        return sha.hexdigest()


# Generate genesis block
def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")


# Generate all later blocks in the blockchain
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = f"Hey! I'm block {this_index}"
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]


# Define how many seconds before adding a new block
# Define after how many blocks to exit
try:
    wait_period = int(environ.get('WAIT_PERIOD'))
except TypeError:
    wait_period = 1


try:
    exit_count = int(environ.get('EXIT_COUNT'))
except TypeError:
    exit_count = float("inf")  # Infinite


# Add blocks to the chain
while True:
    # Begin adding blocks
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    # Logs
    print(f"Block {block_to_add.index} has been added to the blockchain!")
    print(f"Hash: {block_to_add.hash}")
    print()
    sleep(wait_period)
    # Exit based on threshold
    if block_to_add.index == exit_count:
        exit(0)
