blockchain-metrics-analyzer/
│── src/
│   ├── metrics.py
│   ├── data_fetcher.py
│   ├── visualization.py
│── tests/
│   ├── test_metrics.py
│── README.md
│── requirements.txt
│── .gitignore
│── LICENSE


import statistics

class BlockchainMetrics:
    def __init__(self, tx_fees, block_times):
        self.tx_fees = tx_fees
        self.block_times = block_times

    def avg_tx_fee(self):
        return round(statistics.mean(self.tx_fees), 8) if self.tx_fees else 0

    def avg_block_time(self):
        return round(statistics.mean(self.block_times), 2) if self.block_times else 0

if __name__ == "__main__":
    sample_fees = [0.0005, 0.0007, 0.0004, 0.0006, 0.0008]
    sample_block_times = [9.8, 10.2, 9.5, 10.1, 9.9]

    metrics = BlockchainMetrics(sample_fees, sample_block_times)
    print(f"Average TX Fee: {metrics.avg_tx_fee()} BTC")
    print(f"Average Block Time: {metrics.avg_block_time()} sec")
