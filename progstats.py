from bs4 import BeautifulSoup
import statistics

with open('progstats.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
    table3 = soup.find_all('tr')
    lst = []

    for td in table3:
        newtd = td.text.split('Y')
        lst.append(len(newtd) - 1)

    lst.sort()
    print(lst)
    print(sum(lst)/len(lst))
    print(statistics.stdev(lst))