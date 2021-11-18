from scripts.helpful_scripts import get_account
from brownie import interface, network, config


def get_weth():
    """
    Mints WETH by depositing ETH
    :return:
    """
    # ABI
    # Address
    account = get_account()
    print('the account',account)
    weth = interface.IWeth(config['networks'][
                               network.show_active()]['weth_token'])
    print('the weth',weth)
    tx = weth.deposit({'from': account, 'value': 0.1 * 10 ** 18})
    tx.wait(1)
    print('the tx',tx)
    print(f"Received 0.1 WETH")
    return tx


def main():
    get_weth()
