#!/usr/bin/python3
import sys, getopt

SKIP_EMPTY_LINES = True
def process_line(line, input_file_name, line_number):
    return line




def process_files(inputfile, outputfile):
  line_number = 0
  for line in inputfile:
    if line == '\n' and SKIP_EMPTY_LINES:
      continue
    processed_line = process_line(line, inputfile, line_number)
    if processed_line:
      outputfile.write(processed_line)
    line_number+=1


def main(argv):
    inputfile = sys.stdin
    outputfile = sys.stdout

    try:
      opts,args = getopt.getopt(argv[1:],"i:o:", ["inputfile=", "outputfile="])
    except getopt.GetoptError:
      print(argv[0], "-i <inputfile> -o <outputfile>")
      sys.exit(2)
    for opt, arg in opts:
      if opt in ("-i", "--inputfile"):
        inputfile = open(arg, "r")
      elif opt in ("-o", "--outputfile"):
        outputfile = open(arg, "w")

    process_files(inputfile, outputfile)

    inputfile.close()
    outputfile.close()

if __name__ == "__main__":
  main(sys.argv)
