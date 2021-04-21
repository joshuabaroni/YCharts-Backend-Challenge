import sys
from src.python.static import utils, reconparser


def main():
    print(utils.logger_header + "Python file main=[" + sys.argv[0] + "] input_loc=[" + sys.argv[1] + "] output_loc=[" +
          sys.argv[2] + "]")
    print(utils.logger_header + "Now loading testfiles...")
    # access tags (DO-POS, D1-TRN, D1-POS, out)
    reconparser.parse_recon_files(sys.argv)

    print(utils.logger_header + "Processing Completed. You can find your output file at [" + sys.argv[2] + "]")


if __name__ == "__main__":
    main()
