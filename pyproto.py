from web3 import Web3, HTTPProvider
import json

local_web3 = Web3(HTTPProvider('http://192.168.1.24:8556'))

print(local_web3.eth.accounts)

balance = local_web3.eth.getBalance(local_web3.eth.accounts[-1])

print (local_web3.fromWei(balance,'ether'))

account = local_web3.eth.accounts[-1]

local_web3.personal.unlockAccount(account, 'kovankovan')

myContract = local_web3.eth.contract()
myContract.abi = json.loads('[{"constant":false,"inputs":[{"name":"_address","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"statemutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"statemutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_tenthOfPercent","type":"uint16"}],"name":"setPercent","outputs":[],"payable":false,"statemutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"statemutability":"nonpayable","type":"constructor"},{"payable":true,"statemutability":"payable","type":"fallback"}]')

myContract.bytecode = '6060604052341561000f57600080fd5b5b336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550610320600060146101000a81548161ffff021916908361ffff1602179055505b5b6103b2806100806000396000f30060606040523615610055576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806313af40351461015657806341c0e1b51461018f578063e71bf860146101a4575b5b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc6103e8600060149054906101000a900461ffff1661ffff1634028115156100b557fe5b049081150290604051600060405180830381858888f1935050505015156100db57600080fd5b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f19350505050151561015357600080fd5b5b005b341561016157600080fd5b61018d600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506101cb565b005b341561019a57600080fd5b6101a261026d565b005b34156101af57600080fd5b6101c9600480803561ffff16906020019091905050610307565b005b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff168073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561022757600080fd5b816000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505b5b5050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff168073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156102c957600080fd5b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16ff5b5b50565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff168073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561036357600080fd5b81600060146101000a81548161ffff021916908361ffff1602179055505b5b50505600a165627a7a7230582019a84ed5df92bf410515236d4352236cf0508ffec93f1984292556f8d86d1d5a0029'



myContract.deploy()