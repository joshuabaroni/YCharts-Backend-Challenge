import sys
from src.python.static import utils, reconparser

def main():
    print(sys.argv, len(sys.argv))
    print(utils.logger_header + "Welcome to YCharts. Now loading testfiles...")
    temp = reconparser.parse_recon_files(sys.argv)
    in_data = temp[0]
    out_data = temp[1]

if __name__ == "__main__":
    main()
