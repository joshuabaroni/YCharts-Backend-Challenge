import sys
from src.python.static import utils, reconparser

def main():
    print(sys.argv, len(sys.argv))
    print(utils.logger_header + "Welcome to YCharts. Now loading testfiles...")
    # access tags (DO-POS, D1-TRN, D1-POS, out)
    portfolio = reconparser.parse_recon_files(sys.argv)

    print(utils.logger_header + "Thank you for using YCharts")

if __name__ == "__main__":
    main()
