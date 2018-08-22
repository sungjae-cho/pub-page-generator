'''
This file is to parse the publications page in the BI homepage.
'''

import sys, getopt


# The BI publication pages
url_pub_conf_inter = 'https://bi.snu.ac.kr/Publications/pub_conf_inter.html'
url_pub_jour_inter = 'https://bi.snu.ac.kr/Publications/pub_journal_inter.html'
url_pub_conf_domes = 'https://bi.snu.ac.kr/Publications/pub_journal_domestic.html'
url_pub_jour_domes = 'https://bi.snu.ac.kr/Publications/pub_conf_domestic.html'

def convert_pub2dict(str_pub):
  '''
  Convert a publication line to a dictionary that has authors, title, publishment, and year as keys. 
  Return a dictionary that has authors, title, publishment, and year as keys
  '''

def get_pub_list(str_html):
  '''
  Return a list containing publication lines from a publication page.
  '''

def read_html(url):
  '''
  Return a HTML string of the given URL.
  '''

def main(argv):
  pass

if __name__== "__main__":
  main(sys.argv[1:])

