import requests
import json
from bs4 import BeautifulSoup

def clean(x): ## Takes out rubbish and "."
    cur = str(x)[24:-6]
    out = ""
    for idx in range(len(cur)):
        if cur[idx] != ".":
            out += cur[idx]
    return out + symbol(x)

def symbol(y): ## Adds amount of '0' depending on symbol
    cur = str(y)[-6]
    if "." not in str(y):
        decimal = 0
    else:
        decimal = (str(y).index(cur)) - (str(y).index(".") + 1)
    out = ""
    if cur == "B":
        while 9 - decimal != 0:
            out += "0"
            decimal += 1
        return out
    elif cur == "M":
        while 6 - decimal != 0:
            out += "0"
            decimal += 1
        return out
    elif cur == "K":
        while 3 - decimal != 0:
            out += "0"
            decimal += 1
        return out
    else:
        return " New symbol"

def getBitcoin():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    return dic["market_cap"], dic["fully_diluted_valuation"]

def getBitcoinPrice():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    return dic["current_price"]

def getEthereum():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    return dic["market_cap"], dic["fully_diluted_valuation"]

def getUniswap():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=uniswap"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    url = "https://defipulse.com/uniswap"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.findAll("td")
    num = 0
    url = "https://www.coingecko.com/en/exchanges/uniswap"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    trade = soup.findAll("div", attrs={"class": "trade-vol-amount"})
    num += float(str(trade)[47:-35]) * getBitcoinPrice()
    url = "https://www.coingecko.com/en/exchanges/uniswap_v2"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    trade = soup.findAll("div", attrs={"class": "trade-vol-amount"})
    num += float(str(trade)[47:-35]) * getBitcoinPrice()
    return dic["market_cap"], dic["fully_diluted_valuation"], clean(title[1]), num

def getMaker():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=maker"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    url = "https://defipulse.com/maker"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.findAll("td")
    return dic["market_cap"], dic["fully_diluted_valuation"], clean(title[1])

def getAave():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=aave"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    url = "https://defipulse.com/aave"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.findAll("td")
    return dic["market_cap"], dic["fully_diluted_valuation"], clean(title[1])

def getYearn():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=yearn-finance"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    return dic["market_cap"], dic["fully_diluted_valuation"]

def getThorchain():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=thorchain"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    return dic["market_cap"], dic["fully_diluted_valuation"]

def getSushi():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=sushi"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    url = "https://defipulse.com/sushiswap"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.findAll("td")
    num = 0
    url = "https://www.coingecko.com/en/exchanges/sushiswap"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    trade = soup.findAll("div", attrs={"class": "trade-vol-amount"})
    num += float(str(trade)[47:-35]) * getBitcoinPrice()
    return dic["market_cap"], dic["fully_diluted_valuation"], clean(title[1]), num

def getZRX():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=0x"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    num = 0
    url = "https://www.coingecko.com/en/exchanges/0x-protocol"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    trade = soup.findAll("div", attrs={"class": "trade-vol-amount"})
    num += float(str(trade)[47:-35]) * getBitcoinPrice()
    return dic["market_cap"], dic["fully_diluted_valuation"], num

def getBancor():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bancor"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    url = "https://defipulse.com/bancor"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.findAll("td")
    num = 0
    url = "https://www.coingecko.com/en/exchanges/bancor"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    trade = soup.findAll("div", attrs={"class": "trade-vol-amount"})
    num += float(str(trade)[47:-35]) * getBitcoinPrice()
    return dic["market_cap"], dic["fully_diluted_valuation"], clean(title[1]), num

def getCurve():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=curve-dao-token"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    url = "https://defipulse.com/curve-finance"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.findAll("td")
    num = 0
    url = "https://www.coingecko.com/en/exchanges/curve"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    trade = soup.findAll("div", attrs={"class": "trade-vol-amount"})
    num += float(str(trade)[47:-35]) * getBitcoinPrice()
    return dic["market_cap"], dic["fully_diluted_valuation"], clean(title[1]), num

def get1Inch():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=1inch"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    url = "https://defipulse.com/1inch-liquidity-protocol"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.findAll("td")
    num = 0
    url = "https://www.coingecko.com/en/exchanges/1inch"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    trade = soup.findAll("div", attrs={"class": "trade-vol-amount"})
    num += float(str(trade)[47:-35]) * getBitcoinPrice()
    return dic["market_cap"], dic["fully_diluted_valuation"], clean(title[1]), num

def getloopring():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=loopring"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    url = "https://defipulse.com/loopring"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.findAll("td")
    num = 0
    url = "https://www.coingecko.com/en/exchanges/loopring"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    trade = soup.findAll("div", attrs={"class": "trade-vol-amount"})
    num += float(str(trade)[47:-35]) * getBitcoinPrice()
    return dic["market_cap"], dic["fully_diluted_valuation"], clean(title[1]), num

def getKyber():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=kyber-network"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    url = "https://defipulse.com/kyber"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.findAll("td")
    num = 0
    url = "https://www.coingecko.com/en/exchanges/kyber_network"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    trade = soup.findAll("div", attrs={"class": "trade-vol-amount"})
    num += float(str(trade)[47:-35]) * getBitcoinPrice()
    return dic["market_cap"], dic["fully_diluted_valuation"], clean(title[1]), num

def getBalancer():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=balancer"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    url = "https://defipulse.com/balancer"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.findAll("td")
    num = 0
    url = "https://www.coingecko.com/en/exchanges/balancer_v1"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    trade = soup.findAll("div", attrs={"class": "trade-vol-amount"})
    num += float(str(trade)[47:-35]) * getBitcoinPrice()
    url = "https://www.coingecko.com/en/exchanges/balancer"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    trade = soup.findAll("div", attrs={"class": "trade-vol-amount"})
    num += float(str(trade)[47:-35]) * getBitcoinPrice()
    return dic["market_cap"], dic["fully_diluted_valuation"], clean(title[1]), num

def getSerum():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=serum"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    num = 0
    url = "https://www.coingecko.com/en/exchanges/serum_dex"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    trade = soup.findAll("div", attrs={"class": "trade-vol-amount"})
    num += float(str(trade)[47:-35]) * getBitcoinPrice()
    return dic["market_cap"], dic["fully_diluted_valuation"], num

def getUma():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=uma"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    return dic["market_cap"], dic["fully_diluted_valuation"]

def getInjective():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=injective-protocol"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    return dic["market_cap"], dic["fully_diluted_valuation"]

def getPerpetual():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=perpetual-protocol"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    return dic["market_cap"], dic["fully_diluted_valuation"]

def getBarnbridge():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=barnbridge"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    url = "https://defipulse.com/barnbridge"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.findAll("td")
    return dic["market_cap"], dic["fully_diluted_valuation"], clean(title[1])

def getSaffron():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=saffron-finance"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    return dic["market_cap"], dic["fully_diluted_valuation"]

def getHegic():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=hegic"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    url = "https://defipulse.com/hegic"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.findAll("td")
    return dic["market_cap"], dic["fully_diluted_valuation"], clean(title[1])

def getSynthetix():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=havven"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup = str(soup)[1:-1]
    dic = json.loads(soup)
    url = "https://defipulse.com/synthetix"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.findAll("td")
    num = 0
    url = "https://www.coingecko.com/en/exchanges/synthetix-exchange"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    trade = soup.findAll("div", attrs={"class": "trade-vol-amount"})
    num += float(str(trade)[47:-35]) * getBitcoinPrice()
    return dic["market_cap"], dic["fully_diluted_valuation"], clean(title[1]), num

def getHref(cur):
    out = ""
    for x in range(39, 100):
        if str(cur)[x] == "\"":
            break
        else:
            out += str(cur)[x]
    return out

def symbol1(y, amount): ## Adds amount of '0' depending on symbol
    out = ""
    cur = str(y)[-1]
    if cur == "B":
        while 9-amount != 0:
            out+="0"
            amount+=1
        return out
    elif cur == "M":
        while 6 - amount != 0:
            out += "0"
            amount += 1
        return out
    elif cur == "K":
        while 3 - amount != 0:
            out += "0"
            amount += 1
        return out
    else:
        return " New symbol"

def getValue(cur):
    out = ""
    start = 0
    end = 0
    num = str(cur).index("$")
    for x in range(num+1, 100):
        if str(cur)[x] == "<":
            end = x-1
            break
        elif str(cur)[x] == ".":
            start = x+1
            pass
        else:
            out += str(cur)[x]
    decimal = end - start
    return out[:-1]+symbol1(out, decimal)

def getBV():
    url = "https://defipulse.com/defi-lending"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    bv = {}
    title = soup.findAll("td", attrs={'class': "defi-outstanding"})
    for x in range(len(title) - 1):
        bv[getHref(title[x])] = getValue(title[x])
    return bv

def getLendingRatio():
    my_dict = get7DayRevenue()
    mc, fd, tvl = getAave()
    mc2, fd2, tvl2 = getMaker()
    bv = getBV()["aave"]
    bv2 = getBV()["maker"]
    return int(mc)/int(tvl), int(fd)/int(tvl), int(mc)/int(bv), int(fd)/int(bv), int(mc2)/int(tvl2), int(fd2)/int(tvl2), int(mc2)/int(bv2), int(fd2)/int(bv2), int(mc)/(int(my_dict["aave"])*52), int(fd)/(int(my_dict["aave"])*52), int(mc2)/(int(my_dict["maker"])*52), int(fd2)/(int(my_dict["maker"])*52)

def getExchangesRatio():
    my_dict = get7DayRevenue()
    uni = getUniswap()
    uni1, uni2, uni3, uni4, uni_rev, uni_rev2 = int(uni[0])/int(uni[2]), int(uni[1])/int(uni[2]), int(uni[0]) / uni[3], int(uni[1]) / uni[3], int(uni[0])/((int(my_dict["uniswap-v3"])+int(my_dict["uniswap-v2"])+int(my_dict["uniswap-v1"]))*52), int(uni[1])/((int(my_dict["uniswap-v3"])+int(my_dict["uniswap-v2"])+int(my_dict["uniswap-v1"]))*52)
    sushi = getSushi()
    sushi1, sushi2, sushi3, sushi4, sushi_rev, sushi_rev2 = int(sushi[0]) / int(sushi[2]), int(sushi[1]) / int(sushi[2]), int(sushi[0]) / sushi[3], int(sushi[1]) / sushi[3], int(sushi[0])/(int(my_dict["sushiswap"])*52), int(sushi[1])/(int(my_dict["sushiswap"])*52)
    bancor = getBancor()
    bancor1, bancor2, bancor3, bancor4, bancor_rev, bancor_rev2 = int(bancor[0]) / int(bancor[2]), int(bancor[1]) / int(bancor[2]), int(bancor[0]) / bancor[3], int(bancor[1]) / bancor[3], int(bancor[0])/(int(my_dict["bancor"])*52), int(bancor[1])/(int(my_dict["bancor"])*52)
    curve = getCurve()
    curve1, curve2, curve3, curve4 = int(curve[0]) / int(curve[2]), int(curve[1]) / int(curve[2]), int(curve[0]) / curve[3], int(curve[1]) / curve[3]
    inch = get1Inch()
    inch1, inch2, inch3, inch4 = int(inch[0]) / int(inch[2]), int(inch[1]) / int(inch[2]), int(inch[0]) / inch[3], int(inch[1]) / inch[3]
    loop = getloopring()
    loop1, loop2, loop3, loop4 = int(loop[0]) / int(loop[2]), int(loop[1]) / int(loop[2]), int(loop[0]) / loop[3], int(loop[1]) / loop[3]
    kyber = getKyber()
    kyber1, kyber2, kyber3, kyber4 = int(kyber[0]) / int(kyber[2]), int(kyber[1]) / int(kyber[2]), int(kyber[0]) / kyber[3], int(kyber[1]) / kyber[3]
    balancer = getBalancer()
    balancer1, balancer2, balancer3, balancer4, balancer_rev, balancer_rev2 = int(balancer[0]) / int(balancer[2]), int(balancer[1]) / int(balancer[2]), int(balancer[0]) / balancer[3], int(balancer[1]) / balancer[3], int(balancer[0])/(int(my_dict["balancer"])*52), int(balancer[1])/(int(my_dict["balancer"])*52)
    zrx = getZRX()
    zrx1, zrx2, zrx_rev, zrx_rev2 = int(zrx[0])/int(zrx[2]), int(zrx[1])/int(zrx[2]), int(zrx[0])/(int(my_dict["zerox"])*52), int(zrx[1])/(int(my_dict["zerox"])*52)
    serum = getSerum()
    ser1, ser2 = int(serum[0])/int(serum[2]), int(serum[1])/int(serum[2])
    return uni1, uni2, uni3, uni4, sushi1, sushi2, sushi3, sushi4, bancor1, bancor2, bancor3, bancor4, curve1, curve2, curve3, curve4, inch1, inch2, inch3, inch4, loop1, loop2, loop3, loop4, kyber1, kyber2, kyber3, kyber4, balancer1, balancer2, balancer3, balancer4, zrx1, zrx2, ser1, ser2, uni_rev, uni_rev2, sushi_rev, sushi_rev2, bancor_rev, bancor_rev2, balancer_rev, balancer_rev2, zrx_rev, zrx_rev2

def getDerivativesRatio():
    my_dict = get7DayRevenue()
    syn =getSynthetix()
    syn_rev_mc, syn_rev_fd = int(syn[0])/(int(my_dict["synthetix"])*52), int(syn[1])/(int(my_dict["synthetix"])*52)
    syn1, syn2, syn3, syn4 = int(syn[0]) / int(syn[2]), int(syn[1]) / int(syn[2]), int(syn[0]) / syn[3], int(syn[1]) / syn[3]
    barn =getBarnbridge()
    barn1, barn2 = int(barn[0]) / int(barn[2]), int(barn[1]) / int(barn[2])
    hegic =getHegic()
    hegic_rev_mc, hegic_rev_fd = int(hegic[0]) / (int(my_dict["hegic"]) * 52), int(hegic[1]) / (int(my_dict["hegic"]) * 52)
    hegic1, hegic2 = int(hegic[0]) / int(hegic[2]), int(hegic[1]) / int(hegic[2])
    return syn1, syn2, syn3, syn4, barn1, barn2, hegic1, hegic2, syn_rev_mc, syn_rev_fd, hegic_rev_mc, hegic_rev_fd

def get7DayRevenue():
    my_dict = {}
    url = "https://cryptofees.info/api/v1/fees"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    cur = json.loads(str(soup))
    tokens = cur["protocols"]
    for x in range(len(tokens)):
        tok = tokens[x]
        id = tok["id"]
        df = tok["fees"]
        seven_day = 0
        for x in range(len(df)):
            seven_day += df[x]["fee"]
        my_dict[id] = seven_day
    return my_dict

print(get7DayRevenue())
