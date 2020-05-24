import os
import sys
from blockchain_parser.blockchain import Blockchain
from blockchain_parser.transaction import Transaction
import subprocess
import json

graph = []
graph_file=sys.argv[1]
myfile = open(graph_file, 'a')
# Instantiate the Blockchain by giving the path to the directory
# containing the .blk files created by bitcoind
blockchain = Blockchain(os.path.expanduser('../bitcoin-blk/'))
counter=5
print("block_height,block_header_timestamp,tx_hash,no,input_transaction_hash,input_transaction_index")
for block in blockchain.get_unordered_blocks():
    for tx in block.transactions:
        nI = nO = 0

        #import ipdb ; ipdb.set_trace()
        try:
            bc_str = subprocess.check_output(['bitcoin-cli', 'getrawtransaction', tx.hash, "1", block.hash])
            bc_jsn = json.loads(bc_str)
        except:
            #print("genesis")
            continue

        try:
            vout_id = bc_jsn['vin'][0]['vout'] # todo: potentially multiple vins and coinbase!
            #import ipdb ; ipdb.set_trace()
            #vout_id = [i['vout'] for i in bc_jsn['vin']]
        except:
            #print("coinbase")
            continue

        sender = ""
        for vout in bc_jsn['vout']:
            #if vout['n'] in vout_id:
            if vout_id == vout['n']:
                # todo: handle multiple senders
                try:
                    sender = vout['scriptPubKey']['addresses'][0] # todo: why is this addresse_s_
                except:
                    import ipdb ; ipdb.set_trace()

        
        #if len(tx.inputs) > 1 and len(tx.outputs) > 1:
        #    import ipdb ; ipdb.set_trace()
        #for no, input in enumerate(tx.inputs):
            #print("%s,%s,%s,%s,%s,%s" % (block.height,block.header.timestamp,tx.hash, no,(input.transaction_hash),input.transaction_index))
            #if int(input._transaction_hash or 0):
            #    import ipdb ; ipdb.set_trace()
        #    nI += 1
        vertex = [sender, 0]
        edges = []
        for no, output in enumerate(tx.outputs):
            #print("%s,%s,%s,%d,%s,%s,%s" % (block.height,block.header.timestamp,tx.hash, no, output.type, output.addresses[0].address if output.addresses else output.addresses , output.value))
            if output.addresses[0].address != sender:
                edges.append([output.addresses[0].address, output.value])

            nO += 1

        vertex.append(edges)

        myfile.write(str(vertex) + '\n')
        myfile.flush()


        #counter -= 1
        #if not counter:
        #    myfile.close()
        #    sys.exit(0)

        #if not sender:
        #    import ipdb ; ipdb.set_trace()
        print("tx=%s Inputx=%d, Outputx=%d, Sender=%s" % (tx, nI, nO, sender))


    #stop
    #sys.exit()

