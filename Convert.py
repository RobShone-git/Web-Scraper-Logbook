import Data
import openpyxl
import os.path
from datetime import datetime

path = os.path.normpath("C:/Users/rshon/Documents/Etherbridge/Hurts/Logs.xlsx")
book = openpyxl.load_workbook(path.strip())

def setEtherbridge():
    eth_sheet = book["Etherbridge"]
    eth_sheet["B2"], eth_sheet["C2"] = Data.getBitcoin()
    eth_sheet["B3"], eth_sheet["C3"] = Data.getEthereum()
    eth_sheet["B4"], eth_sheet["C4"], eth_sheet["D4"], eth_sheet["E4"] = Data.getUniswap()
    eth_sheet["B5"], eth_sheet["C5"], eth_sheet["D5"] = Data.getMaker()
    eth_sheet["B6"], eth_sheet["C6"], eth_sheet["D6"] = Data.getAave()
    eth_sheet["B7"], eth_sheet["C7"] = Data.getYearn()
    eth_sheet["F2"] = Data.get7DayRevenue()["btc"]
    eth_sheet["F3"] = Data.get7DayRevenue()["eth"]
    eth_sheet["F4"] = Data.get7DayRevenue()["uniswap-v3"] + Data.get7DayRevenue()["uniswap-v2"] + Data.get7DayRevenue()["uniswap-v1"]
    eth_sheet["F5"] = Data.get7DayRevenue()["maker"]
    eth_sheet["F6"] =Data.get7DayRevenue()["aave"]

def setExchanges():
    Exch = book["Exchanges"]
    Exch["B2"], Exch["C2"], Exch["D2"],  Exch["G2"] = Data.getUniswap()
    Exch["B3"], Exch["C3"] = Data.getThorchain()
    Exch["B4"], Exch["C4"], Exch["D4"], Exch["G4"] = Data.getSushi()
    Exch["B5"], Exch["C5"], Exch["G5"] = Data.getZRX()
    Exch["B6"], Exch["C6"], Exch["D6"], Exch["G6"] = Data.getBancor()
    Exch["B7"], Exch["C7"], Exch["D7"], Exch["G7"] = Data.getCurve()
    Exch["B8"], Exch["C8"], Exch["D8"], Exch["G8"] = Data.get1Inch()
    Exch["B9"], Exch["C9"], Exch["D9"], Exch["G9"] = Data.getloopring()
    Exch["B10"], Exch["C10"], Exch["D10"], Exch["G10"] = Data.getKyber()
    Exch["B11"], Exch["C11"], Exch["D11"], Exch["G11"] = Data.getBalancer()
    Exch["B12"], Exch["C12"], Exch["G12"] = Data.getSerum()
    Exch["J2"] = Data.get7DayRevenue()["uniswap-v3"] + Data.get7DayRevenue()["uniswap-v2"] + Data.get7DayRevenue()["uniswap-v1"]
    Exch["J4"] = Data.get7DayRevenue()["sushiswap"]
    Exch["J5"] = Data.get7DayRevenue()["zerox"]
    Exch["J6"] = Data.get7DayRevenue()["bancor"]
    #Exch["J7"] = Data.get7DayRevenue()["curve"]
    Exch["J11"] = Data.get7DayRevenue()["balancer"]

def setDerivatives():
    der = book["Derivatives"]
    der["B2"], der["C2"], der["D2"], der["G2"] = Data.getSynthetix()
    der["B3"], der["C3"], der["D3"] = Data.getBarnbridge()
    der["B4"], der["C4"], der["D4"] = Data.getHegic()
    der["B5"], der["C5"] = Data.getUma()
    der["B6"], der["C6"] = Data.getInjective()
    der["B7"], der["C7"] = Data.getPerpetual()
    der["B8"], der["C8"] = Data.getSaffron()
    der["J2"] = Data.get7DayRevenue()["synthetix"]
    der["J4"] = Data.get7DayRevenue()["hegic"]

def setLending():
    lend = book["Lending"]
    lend["B2"], lend["C2"], lend["E2"] = Data.getAave()
    lend["B3"], lend["C3"], lend["E3"] = Data.getMaker()
    lend["D2"] = Data.getBV()["aave"]
    lend["D3"] = Data.getBV()["maker"]
    lend["J2"] = Data.get7DayRevenue()["aave"]
    lend["J3"] = Data.get7DayRevenue()["maker"]

def newRatioSheet():
    date = datetime.date(datetime.now())
    book.create_sheet("Ratios "+str(date))
    ratio = book["Ratios "+str(date)]
    ratio["B3"], ratio["C3"], ratio["D3"], ratio["E3"], ratio["B4"], ratio["C4"],  ratio["D4"], ratio["E4"], ratio["B5"], ratio["C5"], ratio["D5"], ratio["E5"], ratio["B6"], ratio["C6"], ratio["D6"], ratio["E6"], ratio["B7"], ratio["C7"], ratio["D7"], ratio["E7"], ratio["B8"], ratio["C8"], ratio["D8"], ratio["E8"], ratio["B9"], ratio["C9"], ratio["D9"], ratio["E9"], ratio["B10"], ratio["C10"], ratio["D10"], ratio["E10"], ratio["D11"], ratio["E11"], ratio["D12"], ratio["E12"], ratio["F3"], ratio["G3"], ratio["F4"], ratio["G4"], ratio["F5"], ratio["G5"], ratio["F10"], ratio["G10"], ratio["F11"], ratio["G11"] = Data.getExchangesRatio()
    ratio["B17"], ratio["C17"], ratio["D17"], ratio["E17"], ratio["B18"], ratio["C18"], ratio["D18"], ratio["E18"], ratio["F17"], ratio["G17"], ratio["F18"], ratio["G18"] = Data.getLendingRatio()
    ratio["K3"], ratio["L3"], ratio["M3"], ratio["N3"], ratio["K4"], ratio["L4"], ratio["K5"], ratio["L5"], ratio["O3"], ratio["P3"], ratio["O5"], ratio["P5"] = Data.getDerivativesRatio()
    ratio["B2"], ratio["K2"], ratio["B16"] = "MC/TVL", "MC/TVL", "MC/TVL"
    ratio["C2"], ratio["L2"], ratio["C16"] = "FD/TVL", "FD/TVL", "FD/TVL"
    ratio["D16"] = "MC/BV"
    ratio["E16"] = "FD/BV"
    ratio["B1"] = "Exchanges"
    ratio["K1"] = "Derivatives"
    ratio["B15"] = "Lending"
    ratio["A3"] = "Uniswap"
    ratio["A4"] = "Sushi"
    ratio["A5"] = "Bancor"
    ratio["A6"] = "Curve"
    ratio["A7"] = "1Inch"
    ratio["A8"] = "Loopring"
    ratio["A9"] = "Kyber"
    ratio["A10"] = "Balancer"
    ratio["A11"] = "ZRX"
    ratio["A12"] = "Serum"
    ratio["J3"] = "Synthetix"
    ratio["J4"] = "Barnbridge"
    ratio["J5"] = "Hegic"
    ratio["A17"] = "Aave"
    ratio["A18"] = "Maker"
    ratio["D2"], ratio["E2"], ratio["M2"], ratio["N2"] = "MC / Exch Vol", "FD / Exch Vol", "MC / Exch Vol", "FD / Exch Vol"
    ratio["F2"], ratio["G2"], ratio["F16"], ratio["G16"], ratio["O2"], ratio["P2"] = "MC /REV-year est", "FD/REV-year est", "MC /REV-year est", "FD/REV-year est", "MC /REV-year est", "FD/REV-year est"


setEtherbridge()
setExchanges()
setDerivatives()
setLending()
newRatioSheet()

book.save("Logs.xlsx")