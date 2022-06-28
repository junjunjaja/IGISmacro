# informations from KOFIA_BOND
KOFIA_BOND_INFO = """https://www.kofiabond.or.kr/websquare/websquare.html?w2xPath=/xml/bondint/lastrop/BISLastAskPrcDay.xml&divisionId=MBIS01010010000000&divisionNm=%25EC%259D%25BC%25EC%259E%2590%25EB%25B3%2584&tabIdx=1&w2xHome=/xml/&w2xDocumentRoot="""
ROW = "/html/body/div[1]/div[4]/div/div[1]/div/table/tbody/tr[{}]"
ASSET = {
    "KR1Y": "국고채권(1년)",
    "KR2Y": "국고채권(2년)",
    "KR3Y": "국고채권(3년)",
    "KR5Y": "국고채권(5년)",
    "KR10Y": "국고채권(10년)",
    "KR20Y": "국고채권(20년)",
    "KR30Y": "국고채권(30년)",
    "KR50Y": "국고채권(50년)",
    "K1MBS5Y": "국민주택1종(5년)",
    "MSB91D": "통안증권(91일)",
    "MSB1Y": "통안증권(1년)",
    "MSB2Y": "통안증권(2년)",
    "KELEC3Y": "한전채(3년)",
    "IFB1Y": "산금채(1년)",
    "CORPBOND3YAA": "회사채(무보증3년)AA-",
    "CORPBOND3YBBB": "회사채(무보증3년)BBB-",
    "CD91D": "CD(91일)",
    "CP91D": "CP(91일)",
}

# information from kfb | datetime style YYYY.MM.DD
KFB_KORIBOR = """https://portal.kfb.or.kr/fingoods/koribor.php?SEARCH_START_DT={}&SEARCH_END_DT={}"""

# shinhan
SHINHAN_FIN = """https://oldm.shinhan.com/pages/financialInfo/itoday/itoday_market_rate.jsp"""
T = '//*[@id="table"]/tbody/tr[1]'

