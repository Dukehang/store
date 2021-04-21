riqi1 = "1号"
name1 = "羽绒服"
price1 = 253.6
stock1 = 500
sale1 = 10

riqi2 = "2号"
name2 = "牛仔裤"
price2 = 86.3
stock2 = 600
sale2 = 60

riqi3 = "3号"
name3 = "风衣"
price3 = 96.8
stock3 = 335
sale3 = 43

riqi4 = "4号"
name4 = "皮草"
price4 = 135.9
stock4 = 855
sale4 = 63

riqi5 = "5号"
name5 = "T恤"
price5 = 65.8
stock5 = 632
sale5 = 63

riqi6 = "6号"
name6 = "衬衫"
price6 = 49.3
stock6 = 562
sale6 = 120

riqi7 = "7号"
name7 = "牛仔裤"
price7 = 86.3
stock7 = 600
sale7 = 72

riqi8 = "8号"
name8 = "羽绒服"
price8 = 253.6
stock8 = 500
sale8 = 69

riqi9 = "9号"
name9 = "牛仔裤"
price9 = 86.3
stock9 = 600
sale9 = 35

riqi10 = "10号"
name10 = "羽绒服"
price10 = 253.6
stock10 = 500
sale10 = 140

riqi11 = "11号"
name11 = "牛仔裤"
price11 = 86.3
stock11 = 600
sale11 = 90

riqi12 = "12号"
name12 = "皮草"
price12 = 135.9
stock12 = 855
sale12 = 24

riqi13 = "13号"
name13 = "T恤"
price13 = 65.8
stock13 = 632
sale13 = 45

riqi14 = "14号"
name14 = "风衣"
price14 = 96.8
stock14 = 335
sale14 = 25

riqi15 = "15号"
name15 = "牛仔裤"
price15 = 86.3
stock15 = 600
sale15 = 60

riqi16 = "16号"
name16 = "T恤"
price16 = 65.8
stock16 = 632
sale16 = 129

riqi17 = "17号"
name17 = "羽绒服"
price17 = 253.6
stock17 = 500
sale17 = 10

riqi18 = "18号"
name18 = "风衣"
price18 = 96.8
stock18 = 335
sale18 = 43

riqi19 = "19号"
name19  = "T恤"
price19 = 65.8
stock19 = 632
sale19 = 63

riqi20 = "20号"
name20 = "牛仔裤"
price20 = 86.3
stock20 = 600
sale20 = 60

riqi21 = "21号"
name21 = "皮草"
price21 = 135.9
stock21 = 855
sale21 = 63

riqi22 = "22号"
name22 = "风衣"
price22 = 96.8
stock22 = 335
sale22 = 60

riqi23 = "23号"
name23 = "T恤"
price23 = 65.8
stock23 = 632
sale23 = 58

riqi24 = "24号"
name24 = "牛仔裤"
price24 = 86.3
stock24 = 600
sale24 = 140

riqi25 = "25号"
name25 = "T恤"
price25 = 65.8
stock25 = 632
sale25 = 48

riqi26 = "26号"
name26 = "风衣"
price26 = 96.8
stock26 = 335
sale26 = 43

riqi27 = "27号"
name27 = "皮草"
price27 = 135.9
stock27 = 855
sale27 = 57

riqi28 = "28号"
name28 = "羽绒服"
price28 = 253.6
stock28 = 500
sale28 = 10

riqi29 = "29号"
name29 = "T恤"
price29 = 65.8
stock29 = 632
sale29 = 63

riqi30 = "30号"
name30 = "风衣"
price30 = 96.8
stock30 = 335
sale30 = 78

zxse=round(price1 * sale1 + price2 * sale2 + price3 * sale3 + price4 * sale4 + price5 * sale5 + price6 * sale6 + price7 * sale7 + price8 * sale8 + price9 * sale9 + price10 * sale10 + price11 * sale11 + price12 * sale12+ price13 * sale13 + price14 * sale14 + price15 * sale15 + price16 * sale16 + price17 * sale17 + price18 * sale18  + price19 * sale19 + price20 * sale20
+ price21 * sale21 + price22 * sale22 + price23 * sale23 + price24 * sale24  + price25 * sale25 + price26 * sale26 + price27 * sale27+ price28 * sale28 + price29 * sale29 + price30 * sale30,2)

zxssl=sale1+sale2+sale3+sale4+sale5+sale6+sale7+sale8+sale9+sale10+sale11+sale12+sale13+sale14+sale15+sale16+sale17+sale18+sale19+sale20+sale21+sale22+sale23+sale24+sale25+sale26+sale27+sale28+sale29+sale30

YRF=round((sale1+sale8+sale10+sale17+sale28)/zxssl*100,2)
YRF1=round(((sale1+sale8+sale10+sale17+sale28)*price1)/zxse*100,2)

NZK=round((sale2+sale7+sale9+sale11+sale15+sale20+sale24)/zxssl*100,2)
NZK1=round(((sale2+sale7+sale9+sale11+sale15+sale20+sale24)*price2)/zxse*100,2)

FY=round((sale3+sale18+sale14+sale22+sale26+sale30)/zxssl*100,2)
FY1=round(((sale3+sale18+sale14+sale22+sale26+sale30)*price3)/zxse*100,2)

PC=round((sale4+sale12+sale21+sale27)/zxssl*100,2)
PC1=round(((sale4+sale12+sale21+sale27)*price4)/zxse*100,2)

TX=round((sale5+sale13+sale16+sale19+sale23+sale25+sale29)/zxssl*100,2)
TX1=round(((sale5+sale13+sale16+sale19+sale23+sale25+sale29)*price5)/zxse*100,2)

CX=round(sale6/zxssl*100,2)
CX1=round(sale6*price6*100,2)

print("------------------------12月衣服销售数据-------------------------")
print("日期\t\t\t服装名称\t\t价格/件\t\t库存数量\t  销售量/每日\t\t")
print(riqi1,"\t\t",name1,"\t\t",price1,"\t\t",stock1,"\t\t",sale1,"\t\t",)
print(riqi2,"\t\t",name2,"\t\t",price2,"\t\t",stock2,"\t\t",sale2,"\t\t",)
print(riqi3,"\t\t",name3,"\t\t",price3,"\t\t",stock3,"\t\t",sale3,"\t\t")
print(riqi4,"\t\t",name4,"\t\t",price4,"\t\t",stock4,"\t\t",sale4,"\t\t")
print(riqi5,"\t\t",name5,"\t\t",price5,"\t\t",stock5,"\t\t",sale5,"\t\t")
print(riqi6,"\t\t",name6,"\t\t",price6,"\t\t",stock6,"\t\t",sale6,"\t\t")
print(riqi7,"\t\t",name7,"\t\t",price7,"\t\t",stock7,"\t\t",sale7,"\t\t")
print(riqi8,"\t\t",name8,"\t\t",price8,"\t\t",stock8,"\t\t",sale8,"\t\t")
print(riqi9,"\t\t",name9,"\t\t",price9,"\t\t",stock9,"\t\t",sale9,"\t\t")
print(riqi10,"\t\t",name10,"\t\t",price10,"\t\t",stock10,"\t\t",sale10,"\t\t")
print(riqi11,"\t\t",name11,"\t\t",price11,"\t\t",stock11,"\t\t",sale11,"\t\t")
print(riqi12,"\t\t",name12,"\t\t",price12,"\t\t",stock12,"\t\t",sale12,"\t\t")
print(riqi13,"\t\t",name13,"\t\t",price13,"\t\t",stock13,"\t\t",sale13,"\t\t")
print(riqi14,"\t\t",name14,"\t\t",price14,"\t\t",stock14,"\t\t",sale14,"\t\t")
print(riqi15,"\t\t",name15,"\t\t",price15,"\t\t",stock15,"\t\t",sale15,"\t\t")
print(riqi16,"\t\t",name16,"\t\t",price16,"\t\t",stock16,"\t\t",sale16,"\t\t")
print(riqi17,"\t\t",name17,"\t\t",price17,"\t\t",stock17,"\t\t",sale17,"\t\t")
print(riqi18,"\t\t",name18,"\t\t",price18,"\t\t",stock18,"\t\t",sale18,"\t\t")
print(riqi19,"\t\t",name19,"\t\t",price19,"\t\t",stock19,"\t\t",sale19,"\t\t")
print(riqi20,"\t\t",name20,"\t\t",price20,"\t\t",stock20,"\t\t",sale20,"\t\t")
print(riqi21,"\t\t",name21,"\t\t",price21,"\t\t",stock21,"\t\t",sale21,"\t\t")
print(riqi22,"\t\t",name22,"\t\t",price22,"\t\t",stock22,"\t\t",sale22,"\t\t")
print(riqi23,"\t\t",name23,"\t\t",price23,"\t\t",stock23,"\t\t",sale23,"\t\t")
print(riqi24,"\t\t",name24,"\t\t",price24,"\t\t",stock24,"\t\t",sale24,"\t\t")
print(riqi25,"\t\t",name25,"\t\t",price25,"\t\t",stock25,"\t\t",sale25,"\t\t")
print(riqi26,"\t\t",name26,"\t\t",price26,"\t\t",stock26,"\t\t",sale26,"\t\t")
print(riqi27,"\t\t",name27,"\t\t",price27,"\t\t",stock27,"\t\t",sale27,"\t\t")
print(riqi28,"\t\t",name28,"\t\t",price28,"\t\t",stock28,"\t\t",sale28,"\t\t")
print(riqi29,"\t\t",name29,"\t\t",price29,"\t\t",stock29,"\t\t",sale29,"\t\t")
print(riqi30,"\t\t",name30,"\t\t",price30,"\t\t",stock30,"\t\t",sale30,"\t\t")

print("------------------------------十二月份销售数据------------------------------------")
print("\t\t\t\t""  羽绒服\t\t  牛仔裤\t\t  风衣\t\t  皮草\t\t  T恤\t\t  衬衫")
print("销售占比:","\t\t",YRF,"%","\t",NZK,"%","\t",FY,"%","\t",PC,"% ","\t",TX,"% ","\t",CX,"%")
print("销售额占比:","\t\t",YRF1,"% ","\t",NZK1,"% ","\t",FY1,"% ","\t",PC1,"% ","\t",TX1,"% ","\t",CX,"%")
print("总销售额：￥",zxse,"元整")
print("-----------------------------------------------------")