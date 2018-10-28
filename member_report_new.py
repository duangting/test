import xml.etree.ElementTree as ET
import json

tree = ET.parse("member_rest.jtl")
root = tree.getroot()
data = []
times = []
spend_time = 0
beginTime = 0
testPass = ''
testSkip = 0
all_case = []
fail_case = []
resultData = []
mess=[]
fail_xiabiao=[]
# 总用例个数
def All_case():
    for count in root.iter("failure"):
        all_case.append(count.text)


# 失败个数
def Fail_casess():
    for i in range(len(all_case)):
        if all_case[i] == 'true':
            fail_case.append(all_case[i])
        else:
            pass


def TestPass():
    return len(all_case) - len(fail_case)


def BeginTime():
    for child in root:
        times.append(child.attrib["ts"])


def Spend_time():
    x = int(times[0])
    y = int(times[-1])
    return y - x


def Result_data():
    All_case()
    Fail_casess()
    BeginTime()


    for respondata in root.iter("responseData"):
        pass

    for head in root.iter("responseHeader"):
        pass

    for message in root.iter("failureMessage"):
        pass
    for child in root:
        mess.append(child.attrib["s"])
        if child.attrib["s"] == "true":
            status = "成功"

        else:
            status = "失败"
            for message in root.iter("failureMessage"):
                pass



        resultData.append({
            "name": child.attrib["tn"],
            "className": child.attrib["tn"],
            "methodName": child.attrib["lb"],
            "description": "暂无",
            "spendTime": child.attrib["t"],
            "status": status,
            "beginTime": child.attrib["ts"],
            "log": [
                "<div><B>请求方式/Url:<br></div>"+head.text,
                "<div><B>响应信息:</B><br></div>"+respondata.text,
                "<div><B>断言结果:</B><br></div>"+message.text]



                # [
                #     "<B>请求方式/Url:<br>"+head.text,
                #      "<B>响应信息:</B><br>"+heads.text]

                    })

    data.append(
        {
            "testName": "会员联盟接口测试报告",
            "testPass": TestPass(),
            "testSkip": 0,
            "totalTime": Spend_time(),
            "testAll": len(all_case),
            "beginTime": times[0],
            "testResult": resultData,
            "testFail": len(fail_case),

        })


def repla():
    Result_data()
    lines = open('template', 'r', encoding='UTF-8').readlines()
    with open('template_NEW2.html', "w", encoding='utf-8') as fp:
        for s in lines:
            fp.write(s.replace('${resultData}', json.dumps(data[0], indent=2)))


if __name__ == '__main__':
    # Result_data()
    # print(Result_data())

    repla()

    # print(json.dumps(data[0],indent=2))
