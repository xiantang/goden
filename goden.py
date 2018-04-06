import requests
from lxml import etree
import xlwt
# headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
# }
# def get_content():
#     for i in range(1,101):
#
#         # content=requests.get('https://www.jinfuzi.com/simu/list_d1_w1_p{}.html'.format(i),headers=headers).text
#         print(len(content))
#
# get_content()
header={
    'Cookie': 'authTag=15868759135; authLoginSwitch=false; JRECORD_UID=923f3a7014857cbc51d1658d9b72ef4e; JRECORD_FTIME=1522816805; _smt_uid=5ac45725.b425bfb; MEIQIA_EXTRA_TRACK_ID=11tsY6J7VfGiBw1KAm6APgcpRrf; gr_user_id=cec12375-10b1-48fa-8ba0-081e3c185fd1; JRECORD_SIGN=bdsem-gq; JRECORD_LTIME=1522829374; JRECORD_SRC=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Kf0000jA5uApXoP2PEOn2peRtbGd8agTSCiyep4fz03Wibe2cYIi3z-NKrVS6YOssYL_9iJX_h9MX9EoptX055AWB94xTk3xdW0Uz88WsIKj2pYPxQ-rwB2r1comw4wSyR7AsUmmmq94PdqG1irHckMXpCKEQTPhc7cOFy4fX5NcMoQ4f6.7R_NR2Ar5Od663rj6t_o3VXj9XBjAMlcm2Ao5xPsqPxuLsRP5Qjn-h6OlD_uQPhz1GLerMI_l32AM-BHf3ZHIo7xgKfYtEpMwsrh8mLUPOH3q-IxHb_l32AM-kYymRlRkRAr_UqRH7qYpIrxNe7PHV2XgZJyAp7WubzNJ0.U1Yk0ZDqExa3JqxH0ZKGm1Ys0ZfqExa3JqxH0A-V5HczPfKM5yF-TZnk0ZNG5yF9pywd0ZKGujY1n6KWpyfqnWT30AdY5HDsnHIxnH0krNtznjmzg1DsnWPxn1msnfKopHYs0ZFY5HbznfK-pyfqnHfzndtznH03n-tkrjRdrNtznWDdr0KBpHYznjf0UynqP1nzrjm1P1m4g1T1n1n4Pj6dP7tYnW63PWR4rjDdg17xn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5HcvPWmvP1TvPW00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0ZwdT1Y3PjR3n1b3rHRzPj0YrHDdrjD0ThNkIjYkPHczrHb1PWmsP1b10ZPGujd-rH0dujIBrj0snjc4PHfs0AP1UHYznRRvnjmkfRf3PjNDrjfd0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tsg1Kxn0Ksmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5HDv0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0APzm1YznWf4n0%26ck%3D5187.5.94.295.557.340.647.418%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.1.0.1.300.0%26wd%3D%25E9%2587%2591%25E6%2596%25A7%25E5%25AD%2590%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26oq%3DOS%252526gt%25253Brror%25253A%252520cannot%252520open%252520resource%26inputT%3D4725%26bc%3D110101; Hm_lvt_b04011eadf1ee1966efd5b52abff3db9=1522816805,1522993675; gr_session_id_9907c51ef09823c8d5b98c511e30a866=2a0951cf-c161-4dae-bb11-942bbc8d92d7; Hm_lvt_0e44f16a6038f64ca0035afb889fd197=1522816805,1522993676; gr_cs1_2a0951cf-c161-4dae-bb11-942bbc8d92d7=user_id%3A7377436006; compare_index=0%26%261%26%262%26%263; Hm_lpvt_b04011eadf1ee1966efd5b52abff3db9=1522998188; Hm_lpvt_0e44f16a6038f64ca0035afb889fd197=1522998188; JRECORD_CTIME=1522998188; JRECORD_LANDPAGE=https%3A%2F%2Fwww.jinfuzi.com%2Fsimu%2Flist_d1_w1_p1.html; PHPSESSID=547vt2iu5b0c9n0hmoqf6m0ts1; jfzWebUser=c4b93daa9c12964c4ef5e08961d95a2997ff75e4a%3A4%3A%7Bi%3A0%3Bs%3A10%3A%227377436006%22%3Bi%3A1%3Bs%3A11%3A%2215868759135%22%3Bi%3A2%3Bi%3A86400%3Bi%3A3%3Ba%3A0%3A%7B%7D%7D; jfz_login_id=7377436006; accessToken=a6460f3f4e42b3c26484a335c478be6e; jfz_user_type=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
} #作为参数传入 request。get

import xlwt
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet=book.add_sheet('goden')
list=['name','investment_strategy','company','fund_manager','run_time','net','total','year']
for i in  range(len(list)):
    sheet.write(0, i, list[i])  # 第一个参数代表行 第二个代表列
# sheet.write(1,0,'sdfdsdfvdfgvdf') #第一个参数代表行 第二个代表列


def  get_content():

    for i in range(1,101):
        content=requests.get('https://www.jinfuzi.com/simu/list_d1_w1_p{}.html'.format(i),headers=header).text#不带浏览器头
        analysis_content(content)

        #获取的text是string

def analysis_content(content):
    # print(content)
    selector=etree.HTML(content)#content 转换为selector
    #/html/body/div[6]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]
    sel=selector.xpath('/html/body/div[6]/div/div[1]/div[3]/table/tbody/tr')

    for item in sel:
        #/html/body/div[6]/div/div[1]/div[3]/table/tbody/tr[1]/td[3]/a
        # ./td[3]/a/text()
        num=''.join(item.xpath('./td[2]/text()'))
        name=''.join(item.xpath('./td[3]/a/text()'))
        investment_strategy =''.join(item.xpath('./td[4]/text()'))
        company = ''.join(item.xpath('./td[5]/a/text()'))
        fund_manager = ''.join(item.xpath('./td[6]/a/text()'))
        run_time=''.join(item.xpath('./td[7]/text()'))
        net = ''.join(item.xpath('./td[8]/text()[1]'))
        #/html/body/div[6]/div/div[1]/div[3]/table/tbody/tr[1]/td[9]/span
        total=''.join(item.xpath('./td[9]/span/text()'))
        #/html/body/div[6]/div/div[1]/div[3]/table/tbody/tr[1]/td[10]/span
        year=''.join(item.xpath('./td[@class="t-year"]/span/text()'))
        net=net.replace(' ','')
        data=[name,investment_strategy,company,fund_manager,run_time,net,total,year]
        write_to_excel(int(num),data)

def write_to_excel(num,data):
    for i in range(len(data)):
        sheet.write(num, i, data[i])
    print("第{}写入成功".format(num))
    book.save(r'C:\Users\战神皮皮迪\Documents\GitHub\goden\goden\test1.xls')

get_content()