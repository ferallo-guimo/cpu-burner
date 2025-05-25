import multiprocessing

def burn_cpu():
    x = 0
    while True:
        x += 1  # endless loop doing math

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"Starting {num_cores} processes to max out CPU")

    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=burn_cpu)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
