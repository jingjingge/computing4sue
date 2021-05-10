
# dictionary to change DF column names
AGE_GROUPS = {
    "DP05_0005PE": "PrecentAgeUnder5",
    "DP05_0006PE": "PrecentAge5to9",
    "DP05_0007PE": "PrecentAge10to14",
    "DP05_0008PE": "PrecentAge15to19",
    "DP05_0009PE": "PrecentAge20to24",
    "DP05_0010PE": "PrecentAge25to34",
    "DP05_0011PE": "PrecentAge35to44",
    "DP05_0012PE": "PrecentAge45to54",
    "DP05_0013PE": "PrecentAge55to59",
    "DP05_0014PE": "PrecentAge60to64",
    "DP05_0015PE": "PrecentAge65to74",
    "DP05_0016PE": "PrecentAge75to84",
    "DP05_0017PE": "PrecentAge85andOlder"
}

# list for census API
AGE = 'DP05_0005PE,DP05_0006PE,DP05_0007PE,DP05_0008PE,DP05_0009PE,DP05_0010PE,DP05_0011PE,DP05_0012PE,DP05_0013PE,DP05_0014PE,DP05_0015PE,DP05_0016PE,DP05_0017PE'


#dicitonary to change DF column names

RACE_GROUPS = {
    "DP05_0037PE": "PercentWhite",
    "DP05_0038PE": "PercetnBlack",
    "DP05_0039PE": "PercentAmericanIndianandAlaskaNative",
    "DP05_0044PE": "PercentAsian",
    "DP05_0052PE": "PercentNativeHawaiianandOtherPacificIslander",
    "DP05_0057PE": "PercentSomeOtherRace",
    "DP05_0070PE": "PercentHispanicOrLatino"
}

# list for census API 
RACE= 'DP05_0037PE,DP05_0038PE,DP05_0039PE,DP05_0044PE,DP05_0052PE,DP05_0057PE,DP05_0070PE'




##
# List for percentage household income API
INCOME = 'DP03_0076PE,DP03_0077PE,DP03_0078PE,DP03_0079PE,DP03_0080PE,DP03_0081PE,DP03_0082PE,DP03_0083PE,DP03_0084PE,DP03_0085PE'

#dicitonary to change DF column names
INCOME_GROUPS = {
    "DP03_0076PE": "PercentUnder$10,000",
    "DP03_0077PE": "Percent$10,000to$14,999",
    "DP03_0078PE": "Percent$15,000to$24,999",
    "DP03_0079PE": "Percent$25,000to$34,999",
    "DP03_0080PE": "Percent$35,000to$49,999",
    "DP03_0081PE": "Percent$50,000to$74,999",
    "DP03_0082PE": "Percent$75,000to$99,999",
    "DP03_0083PE": "Percent$100,000to$149,999",
    "DP03_0084PE": "Percent$150,000to$199,999",
    "DP03_0085PE": "Percent$200,000ormore",
}



##
# list for unemployment rate API
UNEMPLOYRATE = 'DP03_0009PE'

#dicitonary to change DF column names

UNEMPLOY_GROUPS = {
    "DP03_0009PE": "Unemployment Rate",
}



##
# list for median household income API
MEDIANINCOME = 'DP03_0062E'

#dicitonary to change DF column names

MEDIANINCOME_GROUPS = {
    "DP03_0062E": "Median household income"
}



##
# list for percentage paying gross rent API
PAIDGROSSRENT = 'DP04_0127PE,DP04_0128PE,DP04_0129PE,DP04_0130PE,DP04_0131PE,DP04_0132PE,DP04_0133PE'

#dicitonary to change DF column names

GROSSRENT_GROUPS = {
    "DP04_0127PE": "PercentLessThan500",
    "DP04_0128PE": "Percent500to999",
    "DP04_0129PE": "Percent1000to1499",
    "DP04_0130PE": "Percent1500to1999",
    "DP04_0131PE": "Percent2000to2499",
    "DP04_0132PE": "Percent2500to2999",
    "DP04_0133PE": "Percent3000ormore",
}
