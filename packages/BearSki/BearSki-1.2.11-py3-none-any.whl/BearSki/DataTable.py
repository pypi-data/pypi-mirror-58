from openpyxl import load_workbook
import time
import re
import random
def getRowData(data="",datafile=""):
  datalist=data.split(".")
  wb = load_workbook(filename = datafile)
  sheet_ranges = wb[datalist[0]]
  values=sheet_ranges.values
  clumtitle=next(values)
  for rowdata in values:
      if rowdata[0]==datalist[1]:
        if len(datalist)==2:
          return clumtitle,rowdata
        else:
          i=clumtitle.index(datalist[2])
          return clumtitle[i],rowdata[i]
def generate_json_data(title,RowData):
  re={}
  if type(RowData)==type("str"):
    re[title]=sfun(RowData)
    return re
  else:
    for i in range(0,len(RowData)):
      re[title[i]]=sfun(RowData[i])
    return re

def generate_data(RowData):
  if type(RowData)==type("str"):
    return sfun(RowData)
  else:
    re=[]
    for value in RowData:
      re.append(sfun(value))
    return re

def sfun(re_str):
  pattern = re.compile(r'\$\{.*?\}')
  longstr=pattern.finditer(re_str)
  result=re_str
  for value in longstr:
    newdata=runfun(value.group())
    result=result.replace(value.group(),newdata,1)
  return result

def runfun(cellstr):
  if cellstr.find('time.now') != -1:
      newvalue=time.strftime("\"%Y-%m-%d %H:%M:%S\"", time.localtime())
      return newvalue
  elif cellstr.find('random.int')!= -1:
      newvalue=getRand_int(cellstr[13:][:-2])
      return newvalue
  else:
      return cellstr

def getRand_int(num):
  return str(random.randint(1,10**int(num)))
