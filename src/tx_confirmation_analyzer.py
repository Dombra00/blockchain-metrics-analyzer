import statistics

def calculate_avg_confirmation_time(tx_times):
    if not tx_times:
        return None
    return round(statistics.mean(tx_times), 2)

if __name__ == "__main__":
    sample_tx_times = [12, 15, 10, 20, 18, 14, 11, 13, 17, 16]
    avg_time = calculate_avg_confirmation_time(sample_tx_times)
    
    if avg_time is not None:
        print(f"Average Transaction Confirmation Time: {avg_time} seconds")
    else:
        print("No transaction data available.")
