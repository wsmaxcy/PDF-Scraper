################################################################################
# Will Maxcy
# Created: 6/30/2022
# Last Updated: 7/1/2022
# Task: Captures health data points, rates these data fileds, then prints these
#      data fields and classification to an output file.
################################################################################

import PyPDF2
import os
import sys
import re

# global variables
path, dirs, files = os.walk(sys.path[0]+'/Input/').__next__()
output = ""

# compare function, input reference number and output print code
def compare(reference,low,high):
    if(reference < low):
        result = 0
    elif(reference > high):
        result = 2
    else:
        result = 1

    return result
# compares reference to see if it is less than the low variable
def lessthan(reference,low):
    if(reference < low):
        result = 1
    else:
        result = 0
    return result

# compares reference to see if it is greater than the low varaible
def greaterthan(reference,low):
    if(reference > low):
        result = 1
    else:
        result = 0
    return result

# compare function to see if it is between two numbers, lower than low, higher than high
def compare3(reference,low,high):
    if(reference < low):
        result = 3
    elif(reference >=low and reference <=high):
        result = 4
    else:
        result = 2
    return result

# check to see if reference matches comparable variable
def match(reference,comp):
    if(reference == comp):
        result = 1
    else:
        result = 5
    return result

# placeholder function
def percentage(reference):
    return 1

# checks rating, prints name and print code to "output"    
def printer(name, rating):
    
    global output
    if(rating == -1):
        text = "NON APPLICABLE"
    elif(rating == 0):
        text = "LOW"
    elif(rating == 1):
        text = "NORMAL"
    elif(rating == 2):
        text = "HIGH"
    elif(rating == 3):
        text = "OPTIMAL"
    elif(rating == 4):
        text = "MODERATE"
    else:
        text = "NOT NORMAL"
    
    out = (name + " is rated as " + text + "\n")
    output += out

# Scans first page
def page0(text):
    
    # regex to find variables on first page
    irontotal = int(str.split(re.search("IRON,TOTAL.*",text)[0].replace("L", " "))[1])# 40-190
    ironbinding = int(str.split(re.search("IRONBINDINGCAPACITY.*",text)[0].replace("L", " "))[1])# 150-450
    saturation = int(str.split(re.search("%SATURATION.*",text)[0].replace("L", " "))[1])# 16-45
    ferritin = int(str.split(re.search("FERRITIN .*",text)[0].replace("L", " "))[1])# 16-154
    testosteronetotal = int(str.split(re.search("TESTOSTERONE,TOTAL.*",text)[0].replace("MS", " "))[1])# 2-45
    testosteronefree = float(str.split(re.search("\(DIALYSIS\)TESTOS.*",text)[0].replace("L", " "))[3])# 0.1-6.4
    lipoprotein = int(str.split(re.search("LIPOPROTEIN\(a\).*",text)[0].replace("L", " "))[1][1:])# <75 - optiomal, 75-125 - moderate, > 125 = high
    apolipoprotein = int(str.split(re.search("APOLIPOPROTEINB.*",text)[0].replace("H", " "))[1])# <90 optimal, 90 - 119 moderate, >=120 high
    
    # finds print code for regex captures
    irontotalR = compare(irontotal,40,190)
    ironbindingR = compare(ironbinding,150,450)
    saturationR = compare(saturation,16,45)
    ferritinR = compare(ferritin,16,154)
    testosteronetotalR = compare(testosteronetotal,2,45)
    testosteronefreeR = compare(testosteronefree,.1,6.4)
    lipoproteinR = compare3(lipoprotein,75,125)
    apolipoproteinR = compare3(apolipoprotein,90,119)

    # prints captured variables to output
    printer("IRON, TOTAL",irontotalR)
    printer("IRON BINDING CAPACITY",ironbindingR)
    printer("PERCENT SATURATION",saturationR)
    printer("FERRITIN",ferritinR)
    printer("TESTOSTERONE, TOTAL",testosteronetotalR)
    printer("TESTOSTERONE, FREE",testosteronefreeR)
    printer("LIPOPROTEIN",lipoproteinR)
    printer("APOLIPOPROTEINB",apolipoproteinR)

# scans second page
def page1(text):
    
    # regex to find variables on second page
    glucose = int(str.split(re.search("GLUCOSE.*",text)[0])[1]) # 65—99mg/dL
    bun = int(str.split(re.search("UREANITROGEN.*",text)[0])[1]) # 7—25mg/dL
    creatinine = float(str.split(re.search("CREATININE.*",text)[0])[1]) # 0.50—1.10mg/dL
    egfrnon = int(str.split(re.search("eGFRNON.*",text)[0])[1]) # >OR=60mL/min/l.73m2
    egfr = int(str.split(re.search("eGFRAFRICANAMERICAN.*",text)[0])[1]) # >OR=60mL/min/l.73m2
    bcratio = str.split(re.search("BUN/CREAT.*",text)[0])[1] # 6—22(calc)
    sodium = int(str.split(re.search("SODIUM.*",text)[0])[1]) # 135—146mmol/L
    potassium = float(str.split(re.search("POTASSIUM.*",text)[0])[1]) # 3.5—5.3mmol/L
    chloride = int(str.split(re.search("CHLORIDE.*",text)[0])[1]) # 98—110mmol/L
    carbondioxide = int(str.split(re.search("CARBONDIOXIDE.*",text)[0])[1]) # 20—32rnmol/L
    calcium = float(str.split(re.search("CALCIUM.*",text)[0])[1]) # 8.6—10.2mg/dL
    protein = float(str.split(re.search("PROTEIN.*",text)[0])[1]) # 6.1—8.1g/dL
    albumin = float(str.split(re.search("ALBUMIN.*",text)[0])[1]) # 3.6—5.1g/dL
    globulin = float(str.split(re.search("GLOBULIN.*",text)[0])[1]) # 1.9—3.7g/dL(calc)
    agratio = float(str.split(re.search("ALBUMIN/GLOBULIN.*",text)[0])[2]) # 1.0—2.5(calc)
    bilirubin = float(str.split(re.search("BILIRUBIN.*",text)[0])[1]) # 0.2—1.2mg/dL
    alkalinephosphate = int(str.split(re.search("ALKALINEPHOSPHATASE.*",text)[0])[1]) # 31—125U/L
    ast = int(str.split(re.search("AST.*",text)[0])[1]) # 10—30U/L
    alt = int(str.split(re.search("ALT.*",text)[0])[1]) # 6—29U/L
    hemoglobin = float(str.split(re.search("HEMOGLOBINA10.*",text)[0])[1]) # <5.7%oftotalHgbEN
    uricacid = float(str.split(re.search("URICACID.*",text)[0])[1]) # 2.5—7.0mg/dL EN
    tsh = float(str.split(re.search("TSH.*",text)[0])[1]) # <6.0mg/dL

    # finds print code for variables
    glucoseR = compare(glucose,65,95)
    bunR = compare(bun,7,25)
    creatinineR = compare(creatinine,.5,1.1)
    egfrnonR = greaterthan(egfrnon,60)
    egfrR = greaterthan(egfr,60)
    
    if(bcratio == "NOTAPPLICABLE"):
        bcratioR = -1
    elif(bcratio > 22):
        bcratioR = 2
    elif(bcratio < 6 ):
        bcratioR = 0
    else:
        bcratioR = 1
    
    sodiumR = compare(sodium,135,146)
    potassiumR = compare(potassium,3.5,5.3)
    chlorideR = compare(chloride,98,110)
    carbondioxideR = compare(carbondioxide,20,32)
    calciumR = compare(calcium,8.6,10.2)
    proteinR = compare(protein,6.1,8.1)
    albuminR = compare(albumin,3.6,5.1)
    globulinR = compare(globulin,1.9,3.7)
    agratioR = compare(agratio,1,2.5)
    bilirubinR = compare(bilirubin,0.2,1.2)
    alkalinephosphateR = compare(alkalinephosphate,31,125)
    astR = compare(ast,10,30)
    altR = compare(alt,6,29)
    hemoglobinR = lessthan(hemoglobin,5.7)
    uricacidR = compare(uricacid,2.5,7)
    
    # prints captured variables to output
    printer("GLUCOSE", glucoseR)
    printer("BUN", bunR)
    printer("CREATININE", creatinineR)
    printer("eGFR NON AFR. AMERICAN", egfrnonR)
    printer("eGFR AFR. AMERICAN", egfrR)
    printer("BUN/CREATININE RATIO", bcratioR)
    printer("SODIUM", sodiumR)
    printer("POTASSIUM", potassiumR)
    printer("CHLORIDE", chlorideR)
    printer("CARBON DIOXIDE", carbondioxideR)
    printer("CALCIUM", calciumR)
    printer("PROTEIN", proteinR)
    printer("ALBUMIN", albuminR)
    printer("GLOBULIN", globulinR)
    printer("ALBUMIN/GLOBULIN RATIO", agratioR)
    printer("BILIRUBIN", bilirubinR)
    printer("ALKALINE PHOSPHATASE", alkalinephosphateR)
    printer("AST", astR)
    printer("ALT", altR)
    printer("HEMOGLOBIN", hemoglobinR)
    printer("URIC ACID", uricacidR)

# scans thrid page
def page2(text):

    # 
    t4 = float(str.split(re.search("T4,FREE.*",text)[0].replace("L", " "))[1])# 40-190
    t3 = float(str.split(re.search("T3,FREE.*",text)[0].replace("L", " "))[1]) # 65—99mg/dL
    zscore = float(str.split(re.search("ZSCORE.*",text)[0].replace("L", " ").replace("—","-"))[2]) # 65—99mg/dL
    wblood = float(str.split(re.search("SQUAMOUSEPITHELIALCELLS.*",text)[0].replace("L", " "))[4]) # 65—99mg/dL
    rblood = float(text.splitlines()[64])
    hemoglobin = float(text.splitlines()[65])
    hematocrit = float(text.splitlines()[66])
    mcv = float(text.splitlines()[67])
    mch = float(text.splitlines()[68])
    mchc = float(text.splitlines()[69])
    rdw = float(text.splitlines()[70])
    plateletcount = int(text.splitlines()[71])
    mpv = float(text.splitlines()[72])
    absoluteneutrophils = int(text.splitlines()[73])
    absolutelymphocytes = int(text.splitlines()[74])
    absolutemonocytes = int(text.splitlines()[75])
    absoluteeosinophils = "ERROR"
    absolutebasophils = int(text.splitlines()[76])
    neutrophils = float(text.splitlines()[77])
    lymphocytes = float(text.splitlines()[78])
    monocytes = float(text.splitlines()[79])
    eosinophils = float(text.splitlines()[80])
    basophils = text.splitlines()[81]
    color = text.splitlines()[82]
    appearance = text.splitlines()[83]
    specificgravity = float(text.splitlines()[84])
    ph = float(text.splitlines()[85])
    glucose = text.splitlines()[86]
    bilirubin = text.splitlines()[87]
    ketones = text.splitlines()[88]
    occultblood = text.splitlines()[89]
    protein = text.splitlines()[90]
    nitrite = text.splitlines()[91]
    leukocyteesterase = text.splitlines()[92]
    wbc = text.splitlines()[93]
    rbc = text.splitlines()[94]
    squamousepithelialcells = str.split(text.splitlines()[95])[0]
    
    # finds print codes
    t4R = compare(t4,.8,1.8)# .8-1.8
    t3R = compare(t3,2.3,4.2)#2.3-4.2
    zscoreR = compare(zscore,63,373)# 63-373
    wbloodR = compare(wblood,3.8,10.8)# 3.8-10.8
    rbloodR = compare(rblood,3.8,5.1)# 3.8-5.10
    hemoglobinR = compare(hemoglobin,11.7,15.5)# 11.7-15.5
    hematocritR = compare(hematocrit,35,45)# 35.0-45.0
    mcvR = compare(mcv,80,100)# 80-100
    mchR = compare(mch,27,33)# 27-33
    mchcR = compare(mchc,32,36)# 32-36
    rdwR = compare(rdw,11,15)# 11-15
    plateletcountR = compare(plateletcount,140,400)# 140-400
    mpvR = compare(mpv,7.5,12.5)# 7.5-12.5
    absoluteneutrophilsR = compare(absoluteneutrophils,1500,7800)# 1500-7800
    absolutelymphocytesR = compare(absolutelymphocytes,850,3900)# 850-3900
    absolutemonocytesR = compare(absolutemonocytes,200,950)# 200-950
    absoluteeosinophilsR = absoluteeosinophils
    absolutebasophilsR = compare(absolutebasophils,0,200)# 0-200
    neutrophilsR = percentage(neutrophils)# %
    lymphocytesR = percentage(lymphocytes)# %
    monocytesR = percentage(monocytes)# %
    eosinophilsR = percentage(eosinophils)# %
    basophilsR = percentage(basophils)# %
    colorR = match(color, "YELLOW")# YELLOW
    appearanceR = match(appearance,"CLEAR")# CLEAR
    specificgravityR = compare(specificgravity,1.001,1.035)# 1.001-1.035
    phR = compare(ph,5,8)# 5-8
    glucoseR = match(glucose,"NEGATIVE")# NEGATIVE
    bilirubinR = match(bilirubin,"NEGATIVE")# NEGATIVE
    ketonesR = match(ketones,"NEGATIVE")# NEGATIVE
    occultbloodR = match(occultblood,"NEGATIVE")# NEGATIVE
    proteinR = match(protein,"NEGATIVE")# NEGATIVE
    nitriteR = match(nitrite,"NEGATIVE")# NEGATIVE
    leukocyteesteraseR = match(leukocyteesterase,"NEGATIVE")# NEGATIVE
    wbcR = wbc
    rbcR = rbc
    squamousepithelialcellsR = squamousepithelialcells

    # prints varaibles and print codes
    printer("T4",t4R)
    printer("T3",t3R)
    printer("ZSCORE",zscoreR)
    printer("WBLOOD",wbloodR)
    printer("RBLOOD",rbloodR)
    printer("HEMOGLOBIN",hemoglobinR)
    printer("HEMATOCRIT",hematocritR)
    printer("MCV",mcvR)
    printer("MCH",mchR)
    printer("MCHC",mchcR)
    printer("RDW",rdwR)
    printer("PLATELETCOUNT",plateletcountR)
    printer("MPV",mpvR)
    printer("ABSOLUTENEUTROPHILS",absoluteneutrophilsR)
    printer("ABSOLUTELYMPHOCYTES",absolutelymphocytesR)
    printer("ABSOLUTEMONOCYTES",absolutemonocytesR)
    printer("ABSOLUTEBASOPHILS",absolutebasophilsR)
    printer("NEUTROPHILS",neutrophilsR)
    printer("LYMPHOCYTES",lymphocytesR)
    printer("MONOCYTES",monocytesR)
    printer("EOSINOPHILS",eosinophilsR)
    printer("BASOPHILS",basophilsR)
    printer("COLOR",colorR)
    printer("APPEARANCE",appearanceR)
    printer("SPECIFICGRAVITY",specificgravityR)
    printer("PH",phR)
    printer("GLUCOSE",glucoseR)
    printer("BILIRUBIN",bilirubinR)
    printer("KETONES",ketonesR)
    printer("OCCULTBLOOD",occultbloodR)
    printer("PROTEIN",proteinR)
    printer("NITRITE",nitriteR)
    printer("LEUKOCYTEESTERASE",leukocyteesteraseR)


def load():
    # walk through Input file and read in all files
    for file in files:
        cur = path + file

        # PyPDF2 scanning of PDF files
        pdfFileObj = open(cur, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
        
        # scan each page
        pageObj0 = pdfReader.getPage(0)
        pageObj1 = pdfReader.getPage(1)
        pageObj2 = pdfReader.getPage(2)

        # save text from scanned PDFs
        text0 = pageObj0.extractText()
        text1 = pageObj1.extractText()
        text2 = pageObj2.extractText()
        
        # scan each page, then close scanner
        page0(text0)
        page1(text1)
        page2(text2)
        pdfFileObj.close()

        # save file in Output folder with same name as Input file
        textpath = open(sys.path[0]+"/Output/"+file[:4]+".txt", "w")
        textpath.write(output)
        textpath.close()
load()
