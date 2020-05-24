# BTC Graph
Tool to represent Bitcoin transaction graph in Giraph format 

# Table Of Contents
1. Background(#Background)
2. How To Run(#how-to-run)


# Background
Our BTC graph analysis adapts https://github.com/alecalve/python-bitcoin-blockchain-parser to parse the blockchain stored locally by the bitcoin daemon. Using the Python library, we have developed a parser that parses each block in the blockchain and looks for transactions. Bitcoin transactions can have m inputs and n outputs. For each transaction, we identify the sender and receiver by matching the sender address and sender amount in the transaction input/output.

The parser then represents the graph in the format 
[sender_id,sent_value,[[receiver_id, received_value],...]] 
for each sent amount in the transaction. This is one of the supported formats of Apache Giraph. Using this graph, we can analyze the transactions using various graph processing algorithms like BFS, DFS, PageRank, ShortestPath, etc.. 

# How To Run
1. Install Bitcoin blockchain parser: https://github.com/alecalve/python-bitcoin-blockchain-parser
2. Make sure the parser is in your `PYTHONPATH` OR copy the parser to the package’s folder `cp fti.py <python-bitcoin-blockchain-parser>`
3. Install `bitcoind` by following instructions for your setup here: https://bitcoin.org/en/full-node
4. Run `bitcoind` with `bitcoind -daemon`. It might take a while for the daemon to get transactions
5. Run `python fti.py <output_filename>`
6. You will find the graph in the output file specified above
