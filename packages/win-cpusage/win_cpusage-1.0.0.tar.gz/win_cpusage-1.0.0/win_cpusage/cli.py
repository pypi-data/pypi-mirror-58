import os
import psutil


def main():

	pid = os.getpid()
	py = psutil.Process(pid)
	memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
	print('memory use:', memoryUse)


if __name__ == "__main__":
	main()