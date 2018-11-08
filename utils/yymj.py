import requests

from lxml import etree


def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        return html
    return None


def pares_html(content):
    etree_html = etree.HTML(content)
    names = []
    war = []
    menpai = []
    daqu = []
    server = []
    score = []
    for i in range(2, 202):
        # id
        result = etree_html.xpath('//table//tr[' + str(i) + ']/td[2]/text()')
        if not result:
            result = etree_html.xpath('//table//tr[' + str(i) + ']/td[2]//span/text()')
            if not result:
                result = etree_html.xpath('//table//tr[' + str(i) + ']/td[2]/font/strong/text()')
        names.append(result)

        # 阵营
        result_war = etree_html.xpath('//table//tr[' + str(i) + ']/td[3]/img/@src')
        if not result_war:
            result_war = etree_html.xpath('//table//tr[' + str(i) + ']/td[3]/text()')
        war.append(result_war)

        # 门派
        result_menpai = etree_html.xpath('//table//tr[' + str(i) + ']/td[4]/img/@src')
        menpai.append(result_menpai)

        # 大区
        result_daqu = etree_html.xpath('//table//tr[' + str(i) + ']/td[5]/text()')
        if not result_daqu:
            result_daqu = etree_html.xpath('//table//tr[' + str(i) + ']/td[5]/strong/span/text()')
            if not result_daqu:
                result_daqu = etree_html.xpath('//table//tr[' + str(i) + ']/td[5]/font/strong/text()')
        daqu.append(result_daqu)

        # 服务器
        result_server = etree_html.xpath('//table//tr[' + str(i) + ']/td[6]/text()')
        if not result_server:
            result_server = etree_html.xpath('//table//tr[' + str(i) + ']/td[6]//span/text()')
            if not result_server:
                result_server = etree_html.xpath('//table//tr[' + str(i) + ']/td[6]//strong/text()')
        server.append(result_server)

        # 资历
        result_score = etree_html.xpath('//table//tr[' + str(i) + ']/td[7]/text()')
        if not result_score:
            result_score = etree_html.xpath('//table//tr[' + str(i) + ']/td[7]//span/text()')
        #     if not result_score:
        #         result_score = etree_html.xpath('//table//tr[' + str(i) + ']/td[6]//strong/text()')
        score.append(result_score)
    return names


def main():
    html = get_page(url)
    result = pares_html(html)

    return result


if __name__ == '__main__':
    url = 'http://jx3yymj.com/index.php?mid=bd'
    print(main())
    print(len(main()))