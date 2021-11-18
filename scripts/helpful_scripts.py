from brownie import (
    network, accounts,
    config
)

DECIMALS = 8
INITIAL_VALUE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local', 'mainnet-fork']


def get_account(index=None, id=None):
    # ganache account accounts[0]
    # accounts.add(".env")
    # accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    return None
